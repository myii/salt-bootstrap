import os
import pprint
import pytest
import testinfra
import logging

log = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def host():
    # log.info("KITCHEN_USERNAME: {}".format(os.environ.get("KITCHEN_USERNAME", "")))
    # log.info("KITCHEN_INSTANCE: {}".format(os.environ.get("KITCHEN_INSTANCE", "")))
    # log.info("KITCHEN_PASSWORD: {}".format(os.environ.get("KITCHEN_PASSWORD", "")))
    # log.info("KITCHEN_HOSTNAME: {}".format(os.environ.get("KITCHEN_HOSTNAME", "")))
    # log.info("KITCHEN_PORT: {}".format(os.environ.get("KITCHEN_PORT", "")))
    # log.info("KITCHEN_SSH_KEY: {}".format(os.environ.get("KITCHEN_SSH_KEY", "")))
    # log.info("KITCHEN_CONTAINER_ID: {}".format(os.environ.get("KITCHEN_CONTAINER_ID", "")))
    # INFO     KITCHEN_USERNAME: kitchen
    # INFO     KITCHEN_INSTANCE: py3-stable-3002-windows-2019
    # INFO     KITCHEN_PASSWORD: Pass@word1
    # INFO     KITCHEN_HOSTNAME: localhost
    # INFO     KITCHEN_PORT: 5985
    # INFO     KITCHEN_SSH_KEY:
    # INFO     KITCHEN_CONTAINER_ID:
    return testinfra.get_host(
        "winrm://{KITCHEN_USERNAME}:{KITCHEN_PASSWORD}@{KITCHEN_HOSTNAME}:{KITCHEN_PORT}".format(
            **os.environ
        ),
        no_ssl=True,
    )
# def host():
#     if os.environ.get("KITCHEN_USERNAME") == "vagrant":
#         if "windows" in os.environ.get("KITCHEN_INSTANCE"):
#             return testinfra.get_host(
#                 "winrm://{KITCHEN_USERNAME}:{KITCHEN_PASSWORD}@{KITCHEN_HOSTNAME}:{KITCHEN_PORT}".format(
#                     **os.environ
#                 ),
#                 no_ssl=True,
#             )
#         return testinfra.get_host(
#             "paramiko://{KITCHEN_USERNAME}@{KITCHEN_HOSTNAME}:{KITCHEN_PORT}".format(
#                 **os.environ
#             ),
#             ssh_identity_file=os.environ.get("KITCHEN_SSH_KEY"),
#         )
#     return testinfra.get_host(
#         "docker://{KITCHEN_USERNAME}@{KITCHEN_CONTAINER_ID}".format(**os.environ)
#     )


@pytest.fixture(scope="session")
def target_python_version():
    target_python = os.environ["KITCHEN_SUITE"].split("-", 1)[0]
    if target_python == "latest":
        pytest.skip(
            "Unable to get target python from {}".format(os.environ["KITCHEN_SUITE"])
        )
    return int(target_python.replace("py", ""))


@pytest.fixture(scope="session")
def target_salt_version():
    target_salt = os.environ["KITCHEN_SUITE"].split("-", 2)[-1].replace("-", ".")
    if target_salt in ("latest", "master"):
        pytest.skip("Don't have a specific salt version to test against")
    return target_salt
