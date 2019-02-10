# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the test for the SEARCHES REST API Methods category."""

from __future__ import unicode_literals

import pytest

from .mixins import RtpyTestMixin


class TestsSearches(RtpyTestMixin):
    """SEARCHES methods category tests."""

    @pytest.fixture
    def setup_then_destroy_test_env(self):
        """Create the test environement for each specific test."""
        # setup
        self.repo_name = RtpyTestMixin.generate_random_string()
        self.artifact_path = "python_logo.png"
        self.params = {}
        self.params["key"] = self.repo_name
        self.params["rclass"] = "local"
        self.params["packageType"] = "debian"
        self.af.repositories.create_repository(self.params)

        self.folder_name = RtpyTestMixin.generate_random_string()
        self.af.artifacts_and_storage.create_directory(self.repo_name, self.folder_name)

        self.af.artifacts_and_storage.deploy_artifact(
            self.repo_name, "tests/assets/python_logo.png", self.artifact_path
        )
        self.af.artifacts_and_storage.set_item_properties(
            self.repo_name, "python_logo.png", "test=true"
        )
        yield

        # teardown
        self.af.repositories.delete_repository(self.repo_name)

    def test_artifactory_query_language(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Artifactory Query Language tests."""
        query = 'items.find({"repo":{"$eq":"' + self.repo_name + '"}})'
        r = self.af.searches.artifactory_query_language(query)
        RtpyTestMixin.assert_isinstance_dict(r)
        if not r["results"]:
            raise self.RtpyTestError("results shouldn't be an empty list!")

    # Unsupported methods
    # def test_artifact_search_quick_search(self)
    # def test_archive_entries_search_class_search()
    # def test_gavc_search()
    # def test_property_search(self):
    # def test_checksum_search(self):
    # def test_bad_checksum_search(self):
    # def test_artifacts_with_date_in_date_range()
    # def test_artifacts_created_in_date_range()
    # def test_pattern_search()
    # def test_builds_for_dependcy()
    # def test_license_search()
    # def test_artifact_version_search()
    # def test_artifact_latest_version_search_based_on_layout()
    # def test_artifact_latest_version_search_based_on_properties()
    # def test_build_artifacts_search()

    def test_list_docker_repositories(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_docker_repo,
    ):
        """List Docker Repositories tests."""
        # Currently not possible to push images to non http Artifactory
        # Using docker-py
        r = self.af.searches.list_docker_repositories(self.docker_repo_key)
        RtpyTestMixin.assert_isinstance_dict(r)

        r = self.af.searches.list_docker_repositories(
            self.docker_repo_key, options="?n=3"
        )
        # RtpyTestMixin.assert_isinstance_dict(r)

    def test_list_docker_tags(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_docker_repo,
    ):
        """List Docker Tags."""
        # Currently 404 if no image exists
        # Output currently not verified as no image is pushed for the tests
        # See reason in the above test
        try:
            r = self.af.searches.list_docker_tags(self.docker_repo_key, "my_image")
            r = self.af.searches.list_docker_tags(
                self.docker_repo_key, "my_image", options="?n=3"
            )
            RtpyTestMixin.assert_isinstance_dict(r)
        except self.af.AfApiError as error:
            if error.status_code != 404:
                raise error
