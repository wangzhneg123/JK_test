# coding:utf-8
import pytest


@pytest.fixture(scope="session")
def login():
    print("前置条件----->登录")