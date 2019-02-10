# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the functions used during the tests."""

from __future__ import unicode_literals
import os
import random
import string
import sys

import pytest

import rtpy


class RtpyTestMixin(object):
    """
    Main test class with fixtures and tools.

    Used in the tests, Subclassed by pytest classes in tests
    """

    def instantiate_af_object_with_api_key_helpers(self):
        """Configure a Rtpy object using an api key."""
        self.settings = {}
        self.settings["af_url"] = os.environ["AF_TEST_URL"]

        self.settings["username"] = os.environ["AF_TEST_USERNAME"]
        self.settings["password"] = os.environ["AF_TEST_PASSWORD"]
        self.af = rtpy.Rtpy(self.settings)
        try:
            self.af.security.revoke_api_key()
        except (self.af.AfApiError, self.af.MalformedAfApiError):
            pass
        r = self.af.security.create_api_key()
        del self.settings["username"]
        del self.settings["password"]
        self.settings["api_key"] = r["apiKey"]

        self.af = rtpy.Rtpy(self.settings)
        self.py_version = sys.version_info

    @pytest.fixture
    def instantiate_af_object_with_api_key(self):
        """Callable fixture."""
        self.instantiate_af_object_with_api_key_helpers()

    def instantiate_af_object_with_credentials_helpers(self):
        """Configure a Rtpy object using a username and password."""
        self.settings = {}
        self.settings["af_url"] = os.environ["AF_TEST_URL"]
        self.settings["username"] = os.environ["AF_TEST_USERNAME"]
        self.settings["password"] = os.environ["AF_TEST_PASSWORD"]
        self.af = rtpy.Rtpy(self.settings)
        self.py_version = sys.version_info

    @pytest.fixture
    def instantiate_af_object_with_credentials(self):
        """Callable fixture."""
        self.instantiate_af_object_with_credentials_helpers()

    @pytest.fixture(params=["api_key", "credentials"])
    def instantiate_af_objects_credentials_and_api_key(self, request):
        """
        Create a Rtpy object using a api_key or username and password.

        The test will be executed twice if this fixture is called
        due to the params argument in the decorator
        """
        if request.param == "api_key":
            self.instantiate_af_object_with_api_key_helpers()

        if request.param == "credentials":
            self.instantiate_af_object_with_credentials_helpers()

    def set_attribute_and_create_repo(self, package_type):
        """Set a repo key attribute and create a repository."""
        setattr(
            self, package_type + "_repo_key", "rtpy_tests_" + package_type + "_repo"
        )
        params = {
            "key": "rtpy_tests_" + package_type + "_repo",
            "rclass": "local",
            "packageType": package_type,
        }
        self.af.repositories.create_repository(params)

    @pytest.fixture
    def create_and_delete_yum_repo(self):
        """Pytest fixture to create and delete a yum repository."""
        self.set_attribute_and_create_repo("yum")
        yield
        self.af.repositories.delete_repository(self.yum_repo_key)

    @pytest.fixture
    def create_and_delete_nuget_repo(self):
        """Pytest fixture to create and delete a nuget repository."""
        self.set_attribute_and_create_repo("nuget")
        yield
        self.af.repositories.delete_repository(self.nuget_repo_key)

    @pytest.fixture
    def create_and_delete_npm_repo(self):
        """Pytest fixture to create and delete a npm repository."""
        self.set_attribute_and_create_repo("npm")
        yield
        self.af.repositories.delete_repository(self.npm_repo_key)

    @pytest.fixture
    def create_and_delete_maven_repo(self):
        """Pytest fixture to create and delete a maven repository."""
        self.set_attribute_and_create_repo("maven")
        yield
        self.af.repositories.delete_repository(self.maven_repo_key)

    @pytest.fixture
    def create_and_delete_opkg_repo(self):
        """Pytest fixture to create and delete a opkg repository."""
        self.set_attribute_and_create_repo("opkg")
        yield
        self.af.repositories.delete_repository(self.opkg_repo_key)

    @pytest.fixture
    def create_and_delete_bower_repo(self):
        """Pytest fixture to create and delete a bower repository."""
        self.set_attribute_and_create_repo("bower")
        yield
        self.af.repositories.delete_repository(self.bower_repo_key)

    @pytest.fixture
    def create_and_delete_helm_repo(self):
        """Pytest fixture to create and delete a helm repository."""
        self.set_attribute_and_create_repo("helm")
        yield
        self.af.repositories.delete_repository(self.helm_repo_key)

    @pytest.fixture
    def create_and_delete_cran_repo(self):
        """Pytest fixture to create and delete a cran repository."""
        self.set_attribute_and_create_repo("cran")
        yield
        self.af.repositories.delete_repository(self.cran_repo_key)

    @pytest.fixture
    def create_and_delete_conda_repo(self):
        """Pytest fixture to create and delete a conda repository."""
        self.set_attribute_and_create_repo("conda")
        yield
        self.af.repositories.delete_repository(self.conda_repo_key)

    @pytest.fixture
    def create_and_delete_docker_repo(self):
        """Pytest fixture to create and delete a docker repository."""
        self.set_attribute_and_create_repo("docker")
        yield
        self.af.repositories.delete_repository(self.docker_repo_key)

    @staticmethod
    def assert_isinstance_dict(r):
        """Assert that the input is a dict."""
        assert isinstance(r, dict), "Invalid output, not a dict!"

    @staticmethod
    def assert_isinstance_str(py_version, r):
        """Assert that the input is a str."""
        if py_version < (3, 4):
            assert isinstance(r, (str, unicode)), "Invalid output, not a str!"
        else:
            assert isinstance(r, (str)), "Invalid output, not a str!"

    @staticmethod
    def assert_isinstance_list(r):
        """Assert that the input is a list."""
        assert isinstance(r, list), "Invalid output, not a list!"

    @staticmethod
    def generate_random_string():
        """Generate a random string."""
        # 64 characters total
        return "rtpy_tests_" + "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(53)
        )

    @staticmethod
    def genererate_random_list_of_random_strings():
        """Generate a random list of random strings."""
        random_list = []
        for i in range(0, 10):
            random_list.append(generate_random_string())
        return random_list

    class RtpyTestError(AssertionError):
        """Raised in tests in case of failure or missing expected result."""

        pass
