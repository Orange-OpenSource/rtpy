# coding: utf-8

# Author: Guillaume Renault
# Author email: grenault.ext@orange.com
# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the tests for the functions defined in rtpy/tools.py."""

from __future__ import unicode_literals
import os

import pytest
import requests

import rtpy
from .mixins import RtpyTestMixin


class TestsTools(RtpyTestMixin):
    """Tools class tests."""

    def test_instantiate_rtpy_with_credentials(self):
        """Instantiate an Rtpy object with credential tests."""
        self.instantiate_af_object_with_credentials_helpers()

    def test_instantiate_rtpy_with_api_key(self):
        """.Instantiate an Rtpy object with api key tests."""
        self.instantiate_af_object_with_api_key_helpers()

    def test_json_to_dict(self):
        """Json to dict tests."""
        original_dict = {"key": "my_value"}
        json_content = """
        {
        "key" : "my_value"
        }
        """

        with open("j_file.json", "w") as j_file:
            j_file.write(json_content)

        myparams = rtpy.json_to_dict("j_file.json")
        os.remove("j_file.json")

        if myparams != original_dict:
            message = "Created dictionary doesn't match original dictionary !"
            raise self.RtpyTestError(message)

    def test_raise_user_settings_error(self):
        """Raise UserSettingsError tests."""
        my_settings = {}
        my_settings["af_url"] = os.environ["AF_TEST_URL"]

        # Missing authentication key(s)
        with pytest.raises(rtpy.UserSettingsError):
            my_settings["username"] = "admin"
            af = rtpy.Rtpy(my_settings)

        # Supplying api key and credentials
        with pytest.raises(rtpy.UserSettingsError):
            my_settings["password"] = "password"
            my_settings["api_key"] = "1234..."
            af = rtpy.Rtpy(my_settings)

        # Supplying incorrect keys
        with pytest.raises(rtpy.UserSettingsError):
            my_settings["my_custom_field"] = "custom_value"
            af = rtpy.Rtpy(my_settings)

        del my_settings["api_key"]
        del my_settings["my_custom_field"]

        # Incorrect raw response value
        with pytest.raises(rtpy.UserSettingsError):
            my_settings["raw_response"] = 2
            af = rtpy.Rtpy(my_settings)

        # Incorrect verbose level value
        with pytest.raises(rtpy.UserSettingsError):
            del my_settings["raw_response"]
            my_settings["verbose_level"] = 5
            af = rtpy.Rtpy(my_settings)

    def test_raise_malformed_af_api_error(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Raise MalformedAfApiError tests."""
        with pytest.raises(self.af.MalformedAfApiError):
            # Providing a bad license key to get an error from the API
            # This error is currently malformed
            params = {"licenseKey": "QWERTY123"}
            self.af.system_and_configuration.install_license(params)

    def test_raise_af_api_error(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_docker_repo,
    ):
        """Raise AfApiError tests."""
        try:
            r = self.af.searches.list_docker_tags(self.docker_repo_key, "my_image")
        except self.af.AfApiError as error:
            raised = True
            try:
                error.api_method,
                error.url,
                error.verb,
                error.status_code,
                error.message,
                error.print_message,
                all_attributes_exist = True
            except Exception as error:
                raise error
        if not raised and not all_attributes_exist:
            raise Exception("Error was not raised, or some attributes are missing")

    def test_raise_rtpy_error(self, instantiate_af_objects_credentials_and_api_key):
        """Raise RtpyError tests."""
        # Empy path
        with pytest.raises(self.af.RtpyError):
            self.af.artifacts_and_storage.retrieve_artifact("repo_key", "")
        with pytest.raises(self.af.RtpyError):
            r = self.af.artifacts_and_storage.artifact_sync_download("repo_key", "")

        # Incorrect archive type
        with pytest.raises(self.af.RtpyError):
            self.af.artifacts_and_storage.retrieve_folder_or_repository_archive(
                "repo_key", "path", "easygz", include_checksums=True
            )

        # Incorrect sha_type
        with pytest.raises(self.af.RtpyError):
            self.af.artifacts_and_storage.deploy_artifact_by_checksum(
                "my_repo", "my_remote_artifact", "sha_9k", "123"
            )

    def test_optional_keys_in_settings(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Optional keys in settings tests."""
        my_settings = {"raw_response": True}
        r = self.af.system_and_configuration.system_health_ping(settings=my_settings)

        if not r.status_code:
            message = "raw response setting did not apply properly!"
            raise self.RtpyTestError(message)
        my_settings = {"verbose_level": 1}
        r = self.af.system_and_configuration.system_health_ping(settings=my_settings)
        session = requests.Session()
        my_settings = {"session": session}
        r = self.af.system_and_configuration.system_health_ping(settings=my_settings)

    def test_self_call(self, instantiate_af_objects_credentials_and_api_key):
        """Test the __call__ dunder (binding to System health ping)."""
        assert self.af() == "OK"
