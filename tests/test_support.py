# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the tests for the SUPPORT REST API Methods category."""

from __future__ import unicode_literals
import os

import rtpy
from .mixins import RtpyTestMixin


class TestsSupport(RtpyTestMixin):
    """SUPPORT methods category tests."""

    def test_create_bundle(self, instantiate_af_objects_credentials_and_api_key):
        """Create Bundle tests."""
        params = rtpy.json_to_dict("tests/assets/bundle_creation.json")
        r = self.af.support.create_bundle(params)
        created_bundle = r["bundles"][0]
        r2 = self.af.support.list_bundles()
        validation = False
        for bundle_name in r2["bundles"]:
            a = bundle_name.index(".zip?")
            bundle_name = bundle_name[: a + 4]
            if bundle_name == created_bundle:
                validation = True
        if not validation:
            raise self.RtpyTestError("Bundle that was created not in bundle list!")
        self.af.support.delete_bundle(created_bundle)
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_list_bundles(self, instantiate_af_objects_credentials_and_api_key):
        """List Bundles tests."""
        r = self.af.support.list_bundles()
        if "bundles" not in r:
            raise self.RtpyTestError("Expected bundles key in output dictionnary!")
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_get_bundle(self, instantiate_af_objects_credentials_and_api_key):
        """Get Bundle tests."""
        params = rtpy.json_to_dict("tests/assets/bundle_creation.json")
        r = self.af.support.create_bundle(params)
        created_bundle = r["bundles"][0]
        bundle_name_good = created_bundle[33:]
        bundle = self.af.support.get_bundle(created_bundle)
        with open(bundle_name_good, "wb") as bundle_file:
            bundle_file.write(bundle.content)
        r = self.af.support.delete_bundle(created_bundle)
        os.remove(bundle_name_good)

    def test_delete_bundle(self, instantiate_af_objects_credentials_and_api_key):
        """Delete Bundle tests."""
        params = rtpy.json_to_dict("tests/assets/bundle_creation.json")
        r = self.af.support.create_bundle(params)
        created_bundle = r["bundles"][0]
        r = self.af.support.delete_bundle(created_bundle)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
