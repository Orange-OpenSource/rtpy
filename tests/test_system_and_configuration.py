# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""
Definitions of the tests for SYSTEM AND CONFIGURATION.

(SYSTEM AND CONFIGURATION REST API Methods category.)
"""

from __future__ import unicode_literals
import os

from .mixins import RtpyTestMixin


class TestsSystemAndConfiguration(RtpyTestMixin):
    """SYSTEM AND CONFIGURATION methods category tests."""

    def test_system_info(self, instantiate_af_objects_credentials_and_api_key):
        """System Info tests."""
        r = self.af.system_and_configuration.system_info()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_system_health_ping(self, instantiate_af_objects_credentials_and_api_key):
        """System Health Ping tests."""
        r = self.af.system_and_configuration.system_health_ping()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    # Unsupported method
    # def test_verify_connection(self):

    def test_general_configuration(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """General Configuration tests."""
        r = self.af.system_and_configuration.general_configuration()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_save_general_configuration(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Save General Configuration tests."""
        r = self.af.system_and_configuration.general_configuration()
        with open("new_conf.xml", "w") as xml_file:
            xml_file.write(r)

        r = self.af.system_and_configuration.save_general_configuration("new_conf.xml")
        os.remove("new_conf.xml")

    # Unsupported method
    # def test_update_custom_url_base(sielf):

    def test_licence_information(self, instantiate_af_objects_credentials_and_api_key):
        """License Information tests."""
        r = self.af.system_and_configuration.license_information()
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_install_license(self, instantiate_af_objects_credentials_and_api_key):
        """Install License tests."""
        # Error output currently malformed
        # Error 400 is returned when license is invalid
        # Test will be fixed accordingly when a patch is realeased by JFrog
        # Licence currently supplied is also invalid
        try:
            params = {"licenseKey": "QWERTY123"}
            r = self.af.system_and_configuration.install_license(params)
            RtpyTestMixin.assert_isinstance_dict(r)
        except self.af.MalformedAfApiError:
            pass

    def test_version_and_addons_information(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Version And Addons Information tests."""
        r = self.af.system_and_configuration.version_and_addons_information()
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_get_reverse_proxy_configuration(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Get Reverse Proxy Configuration tests."""
        r = self.af.system_and_configuration.get_reverse_proxy_configuration()
        RtpyTestMixin.assert_isinstance_dict(r)

    # Unsupported method
    # def test_update_reverse_proxy_configuration(self):

    def test_get_reverse_proxy_snippet(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Get Reverse Proxy snippet tests."""
        # No proxy configuration by default (400)
        try:
            r = self.af.system_and_configuration.get_reverse_proxy_snippet()
            RtpyTestMixin.assert_isinstance_dict(r)
        except self.af.AfApiError as error:
            if error.status_code != 400:
                raise error
