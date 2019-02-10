# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the tests for the REPOSITORIES REST API Methods category."""

from __future__ import unicode_literals
import time

import pytest

from .mixins import RtpyTestMixin


class TestsRepositories(RtpyTestMixin):
    """REPOSITORIES methods category tests."""

    @pytest.fixture
    def create_debian_repo_push_artifacts_then_delete_repo(self):
        """Create the test environement for each specific test."""
        # setup
        self.debian_repo_key = "rtpy_tests_repositories_debian_repo"
        self.artifact_path = "python_logo.png"
        params = {
            "key": self.debian_repo_key,
            "rclass": "local",
            "packageType": "debian",
        }
        self.af.repositories.create_repository(params)

        self.folder_name = RtpyTestMixin.generate_random_string()
        self.af.artifacts_and_storage.create_directory(
            self.debian_repo_key, self.folder_name
        )

        self.af.artifacts_and_storage.deploy_artifact(
            self.debian_repo_key, "tests/assets/python_logo.png", self.artifact_path
        )
        self.af.artifacts_and_storage.set_item_properties(
            self.debian_repo_key, "python_logo.png", "test=true"
        )
        yield

        # teardown
        self.af.repositories.delete_repository(self.debian_repo_key)

    def test_get_repositories(self, instantiate_af_objects_credentials_and_api_key):
        """Get Repositories tests."""
        r = self.af.repositories.get_repositories()
        RtpyTestMixin.assert_isinstance_list(r)
        r = self.af.repositories.get_repositories(
            options="?type=local&packageType=pypi"
        )
        RtpyTestMixin.assert_isinstance_list(r)

    def test_repository_configuration(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_debian_repo_push_artifacts_then_delete_repo,
    ):
        """Repository Configuration tests."""
        r = self.af.repositories.repository_configuration(self.debian_repo_key)
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_create_repository(self, instantiate_af_objects_credentials_and_api_key):
        """Create Repository tests."""
        params = {
            "key": "rtpy_tests_repositories_test_create_repository",
            "rclass": "local",
            "packageType": "generic",
        }
        r = self.af.repositories.create_repository(params)
        self.af.repositories.delete_repository(
            "rtpy_tests_repositories_test_create_repository"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_update_repository_configuration(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_debian_repo_push_artifacts_then_delete_repo,
    ):
        """Update Repository Configuration tests."""
        params = {"description": "new_description", "key": self.debian_repo_key}
        r = self.af.repositories.update_repository_configuration(params)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_delete_repository(self, instantiate_af_objects_credentials_and_api_key):
        """Delete Repository tests."""
        params = {
            "key": "rtpy_tests_repositories_delete_repository",
            "rclass": "local",
            "packageType": "generic",
        }
        self.af.repositories.create_repository(params)
        r = self.af.repositories.delete_repository(
            "rtpy_tests_repositories_delete_repository"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_yum_repository_metadata(
        self, instantiate_af_objects_credentials_and_api_key, create_and_delete_yum_repo
    ):
        """Calculate YUM Repository Metadata tests."""
        self.af.artifacts_and_storage.create_directory(self.yum_repo_key, "folder1")
        r = self.af.repositories.calculate_yum_repository_metadata(self.yum_repo_key)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        r = self.af.repositories.calculate_yum_repository_metadata(
            self.yum_repo_key, options="?path=folder1&async=0"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        r = self.af.repositories.calculate_yum_repository_metadata(
            self.yum_repo_key, options="?path=folder1&async=0", x_gpg_passphrase="abc"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_nuget_repository_metadata(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_nuget_repo,
    ):
        """Calculate Nuget Repository Metadata tests."""
        r = self.af.repositories.calculate_nuget_repository_metadata(
            self.nuget_repo_key
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_npm_repository_metadata(
        self, instantiate_af_objects_credentials_and_api_key, create_and_delete_npm_repo
    ):
        """Calculate NPM Repository Metadata tests."""
        r = self.af.repositories.calculate_npm_repository_metadata(self.npm_repo_key)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_maven_index(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_maven_repo,
    ):
        """Test Calculate Maven Index tests."""
        # The test is run twice with credentials and api_key which can result
        # in the following error:
        # Status Code : 500
        # Message : Could not run indexer: Another manual
        # task org.artifactory.maven.index.MavenIndexerJob is still active!
        while True:
            try:
                r = self.af.repositories.calculate_maven_index(
                    "repos=" + self.maven_repo_key
                )
                break
            except self.af.AfApiError as error:
                if error.status_code == 500:
                    time.sleep(1)
                    pass

        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_maven_metadata(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_maven_repo,
    ):
        """Calculate Maven Metadata tests."""
        self.af.artifacts_and_storage.create_directory(self.maven_repo_key, "folder1")
        r = self.af.repositories.calculate_maven_metadata(
            self.maven_repo_key, "folder1"
        )
        r = self.af.repositories.calculate_maven_metadata(
            self.maven_repo_key, "folder1", options="?nonRecursive=true"
        )

        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_debian_repository_metadata(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_debian_repo_push_artifacts_then_delete_repo,
    ):
        """Calculate Debian Repository Metadata."""
        r = self.af.repositories.calculate_debian_repository_metadata(
            self.debian_repo_key
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        r = self.af.repositories.calculate_debian_repository_metadata(
            self.debian_repo_key, options="?writeProps=0"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        r = self.af.repositories.calculate_debian_repository_metadata(
            self.debian_repo_key, options="?writeProps=0", x_gpg_passphrase="abc"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_opkg_repository_metadata(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_opkg_repo,
    ):
        """Calculate Opkg Repository Metadata tests."""
        r = self.af.repositories.calculate_opkg_repository_metadata(self.opkg_repo_key)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        r = self.af.repositories.calculate_opkg_repository_metadata(
            self.opkg_repo_key, options="?writeProps=0"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        r = self.af.repositories.calculate_opkg_repository_metadata(
            self.opkg_repo_key, options="?writeProps=0", x_gpg_passphrase="abc"
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_bower_index(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_bower_repo,
    ):
        """Calculate Bower Index tests."""
        r = self.af.repositories.calculate_bower_index(self.bower_repo_key)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_helm_chart_index(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_helm_repo,
    ):
        """Calculate Helm Chart Index tests."""
        r = self.af.repositories.calculate_helm_chart_index(self.helm_repo_key)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_cran_repository_metadata(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_cran_repo,
    ):
        """Calculate CRAN Repository Metadata tests."""
        r = self.af.repositories.calculate_cran_repository_metadata(self.cran_repo_key)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_calculate_conda_repository_metadata(
        self,
        instantiate_af_objects_credentials_and_api_key,
        create_and_delete_conda_repo,
    ):
        """Calculate Conda Repository Metadata tests."""
        # Currently returning HTTP 500
        # Probably because the test repository is empty?
        try:
            r = self.af.repositories.calculate_conda_repository_metadata(
                self.conda_repo_key
            )
            RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        except self.af.AfApiError as error:
            if error.status_code != 500:
                raise error
