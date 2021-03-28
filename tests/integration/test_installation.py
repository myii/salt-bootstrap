# -*- coding: utf-8 -*-
import json
import os
import pytest
import logging
import pprint
from contextlib import nullcontext

log = logging.getLogger(__name__)

# https://stackoverflow.com/questions/27803059/conditional-with-statement-in-python
if "windows" in os.environ.get("KITCHEN_INSTANCE"):
    cm = nullcontext()
else:
    cm = host.sudo()

def test_ping(host):
    with cm:
        assert host.salt("test.ping", "--timeout=5")


def test_target_python_version(host, target_python_version):
    with cm:
        ret = host.salt("grains.item", "pythonversion", "--timeout=5")
        assert ret["pythonversion"][0] == target_python_version


def test_target_salt_version(host, target_salt_version):
    with cm:
        ret = host.salt("grains.item", "saltversion", "--timeout=5")
        if target_salt_version.endswith(".0"):
            assert ret["saltversion"] == ".".join(target_salt_version.split(".")[:-1])
        else:
            assert ret["saltversion"].startswith(target_salt_version)
