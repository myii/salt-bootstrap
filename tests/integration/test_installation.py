# -*- coding: utf-8 -*-
import json
import pytest
import logging
import pprint
# from contextlib import nullcontext

log = logging.getLogger(__name__)

# if needs_with():
#     cm = get_stuff()
# else:
#     cm = nullcontext()
#
# with cm as gs:
#     # Do stuff

def test_ping(host):
    # with host.sudo():
    # with nullcontext():
    assert host.salt("test.ping", "--timeout=5")


def test_target_python_version(host, target_python_version):
    # with host.sudo():
    # with nullcontext():
    ret = host.salt("grains.item", "pythonversion", "--timeout=5")
    assert ret["pythonversion"][0] == target_python_version


def test_target_salt_version(host, target_salt_version):
    # with host.sudo():
    # with nullcontext():
    ret = host.salt("grains.item", "saltversion", "--timeout=5")
    if target_salt_version.endswith(".0"):
        assert ret["saltversion"] == ".".join(target_salt_version.split(".")[:-1])
    else:
        assert ret["saltversion"].startswith(target_salt_version)
