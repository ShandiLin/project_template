# -*-coding:utf-8-*-
import sys


def pytest_configure(config):

    sys._called_from_test = True


def pytest_unconfigure(config):

    del sys._called_from_test
