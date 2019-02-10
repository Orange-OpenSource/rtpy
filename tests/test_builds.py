# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the tests for the BUILDS REST API Methods category."""

from __future__ import unicode_literals

import pytest

from .mixins import RtpyTestMixin


class TestsBuilds(RtpyTestMixin):
    """BUILDS methods category tests."""

    @pytest.fixture
    def setup_and_teardown_test_env(self):
        """Create the test environement for each specific test."""
        pass

    def test_all_builds(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_and_teardown_test_env,
    ):
        """
        All Builds tests.

        Currently returning 404 because no builds were previously created

        """
        try:
            self.af.builds.all_builds()
        except self.af.AfApiError as error:
            if error.status_code != 404:
                raise error

    # Unsupported methods
    # def test_build_runs()
    # def test_build_upload()
    # def test_build_info()
    # def test_builds_diff()
    # def test_build_promotion()
    # def test_promote_docker_image()
    # def test_delete_builds()
    # def test_push_build_to_bintray()
    # def test_distribute_build()
    # def test_control_build_retention()
