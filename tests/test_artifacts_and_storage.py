# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the tests for the ARTIFACTS AND STORAGE REST API Methods category."""

from __future__ import unicode_literals
import os

import pytest

from .mixins import RtpyTestMixin


class TestsArtifactsAndStorage(RtpyTestMixin):
    """ARTIFACTS AND STORAGE methods category tests."""

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

    def test_folder_info(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Folder Info method tests."""
        r = self.af.artifacts_and_storage.folder_info(self.repo_name, self.folder_name)
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_file_info(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """File Info method tests."""
        r = self.af.artifacts_and_storage.file_info(self.repo_name, self.artifact_path)
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_get_storage_summary_info(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Get Storage Summary Info tests."""
        r = self.af.artifacts_and_storage.get_storage_summary_info()
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_item_last_modified(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Item Last Modified tests."""
        r = self.af.artifacts_and_storage.item_last_modified(
            self.repo_name, self.artifact_path
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_file_statistics(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """File Statistics tests."""
        r = self.af.artifacts_and_storage.file_statistics(
            self.repo_name, self.artifact_path
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_item_properties(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Item Properties tests."""
        r = self.af.artifacts_and_storage.set_item_properties(
            self.repo_name, self.artifact_path, "rtpy=true"
        )
        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path
        )
        RtpyTestMixin.assert_isinstance_dict(r)
        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path, properties="rtpy"
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_set_item_properties(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Set Item Properties tests."""
        self.af.artifacts_and_storage.set_item_properties(
            self.repo_name, self.artifact_path, "rtpy=true"
        )
        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path
        )
        if r["properties"]["rtpy"][0] != "true":
            message = "Property missing or has incorrect value"
            raise self.RtpyTestError(message)
        self.af.artifacts_and_storage.delete_item_properties(
            self.repo_name, self.artifact_path, "rtpy"
        )
        RtpyTestMixin.assert_isinstance_dict(r)
        self.af.artifacts_and_storage.set_item_properties(
            self.repo_name, self.artifact_path, "rtpy=true", options="&recursive=0"
        )
        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path
        )
        if r["properties"]["rtpy"][0] != "true":
            message = "Property missing or has incorrect value"
            raise self.RtpyTestError(message)
        self.af.artifacts_and_storage.delete_item_properties(
            self.repo_name, self.artifact_path, "rtpy"
        )

    def test_delete_item_properties(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Delete Item Properties tests."""
        self.af.artifacts_and_storage.set_item_properties(
            self.repo_name, self.artifact_path, "rtpy=true;p2=false"
        )

        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path
        )
        if r["properties"]["rtpy"][0] != "true":
            message = "Property missing or has incorrect value"
            raise self.RtpyTestError(message)
        self.af.artifacts_and_storage.delete_item_properties(
            self.repo_name, self.artifact_path, "rtpy"
        )
        self.af.artifacts_and_storage.delete_item_properties(
            self.repo_name, self.artifact_path, "rtpy", options="&recursive=0"
        )
        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path
        )
        if "rtpy" in r["properties"]:
            message = "Property wasn't deleted!"
            raise self.RtpyTestError(message)
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_set_item_sha256_checksum(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Set Item 256 checksum tests."""
        params = {"repoKey": self.repo_name, "path": self.artifact_path}
        self.af.artifacts_and_storage.set_item_sha256_checksum(params)
        r = self.af.artifacts_and_storage.item_properties(
            self.repo_name, self.artifact_path
        )
        if "sha256" not in r["properties"]:
            message = "sha256 property wasn't added!"
            raise self.RtpyTestError(message)
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_retrieve_artifact(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Retrieve Artifact tests."""
        r = self.af.artifacts_and_storage.retrieve_artifact(
            self.repo_name, self.artifact_path
        )
        with open("myartifact.png", "wb") as artifact:
            artifact.write(r.content)

        os.remove("myartifact.png")

        # Unsupported methods
        # def test_retrieve_latest_artifact():
        # def test_retrieve_build_artifacts_archive():"""

    def test_retrieve_folder_or_repository_archive(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """
        Retrieve Folder or Repository Archive tests.

        Folder download is not allowed by default
        catching the HTTP 403 so the test can pass

        """
        archive_types = ["zip", "tar", "tar.gz", "tgz"]

        self.af.artifacts_and_storage.create_directory(self.repo_name, "mydir")

        for archive_type in archive_types:
            try:
                r = self.af.artifacts_and_storage.retrieve_folder_or_repository_archive(
                    self.repo_name, "", archive_type
                )
                with open("myarchive." + archive_type, "wb") as archive:
                    archive.write(r.content)
                os.remove("myarchive." + archive_type)
            except self.af.AfApiError as error:
                if error.status_code != 403:
                    raise error

            try:
                r = self.af.artifacts_and_storage.retrieve_folder_or_repository_archive(
                    self.repo_name, "mydir", archive_type, include_checksums=True
                )
                with open("myarchive." + archive_type, "wb") as archive:
                    archive.write(r.content)
                os.remove("myarchive." + archive_type)
            except self.af.AfApiError as error:
                if error.status_code != 403:
                    raise error

    def test_trace_artifact_retrieval(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Trace Artifact Retrieval tests."""
        r = self.af.artifacts_and_storage.trace_artifact_retrieval(
            self.repo_name, self.artifact_path
        )
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    # Unsupported method
    # def test_archive_entry_download():

    def test_create_directory(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Create Directory tests."""
        r = self.af.artifacts_and_storage.create_directory(self.repo_name, "mydir")
        RtpyTestMixin.assert_isinstance_dict(r)
        r = self.af.artifacts_and_storage.folder_info(self.repo_name, "mydir")

    def test_deploy_artifact(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Deploy Artifact tests."""
        r = self.af.artifacts_and_storage.deploy_artifact(
            self.repo_name, "tests/assets/python_logo.png", "python_logo.png"
        )
        RtpyTestMixin.assert_isinstance_dict(r)
        self.af.artifacts_and_storage.file_info(self.repo_name, "python_logo.png")

    def test_deploy_artifact_by_checksum(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Deploy Artifact by checksum tests."""
        r = self.af.artifacts_and_storage.deploy_artifact_by_checksum(
            self.repo_name,
            "python_logo_copy1.png",
            "sha1",
            "9e0a0e7dbc3d5f05c71812e0a38aebefe525506c",
        )

        RtpyTestMixin.assert_isinstance_dict(r)
        self.af.artifacts_and_storage.file_info(self.repo_name, "python_logo_copy1.png")

        r = self.af.artifacts_and_storage.deploy_artifact_by_checksum(
            self.repo_name,
            "python_logo_copy2.png",
            "sha256",
            "fd04e86f3b8992bd599bab7ec407223aebd14541b7b055f5725d6d55398708c5",
        )
        RtpyTestMixin.assert_isinstance_dict(r)
        self.af.artifacts_and_storage.file_info(self.repo_name, "python_logo_copy2.png")

    # Unsupported methods
    # def test_deploy_artifacts_from_archive():
    # def test_push_a_set_of_artifacts_to_bintray():
    # def test_push_docker_tag_to_bintray():
    # def test_distribute_artifact():
    # def test_file_compliance_info():

    def test_delete_item(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Delete Item tests."""
        r = self.af.artifacts_and_storage.delete_item(
            self.repo_name, self.artifact_path
        )
        try:
            r = self.af.artifacts_and_storage.file_info(
                self.repo_name, self.artifact_path
            )
        except self.af.AfApiError as error:
            if error.status_code != 404:
                raise self.RtpyTestError("Artifact wasn't deleted!")

        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_copy_item(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Copy Item tests."""
        r = self.af.artifacts_and_storage.copy_item(
            self.repo_name, self.artifact_path, self.repo_name, "python_logo_copy.png"
        )

        RtpyTestMixin.assert_isinstance_dict(r)
        self.af.artifacts_and_storage.file_info(self.repo_name, "python_logo_copy.png")
        r = self.af.artifacts_and_storage.copy_item(
            self.repo_name,
            self.artifact_path,
            self.repo_name,
            "python_logo_copy.png",
            options="&dry=1",
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_move_item(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Move Item tests."""
        r = self.af.artifacts_and_storage.move_item(
            self.repo_name, self.artifact_path, self.repo_name, "python_logo_copy.png"
        )
        RtpyTestMixin.assert_isinstance_dict(r)
        self.af.artifacts_and_storage.file_info(self.repo_name, "python_logo_copy.png")
        r = self.af.artifacts_and_storage.move_item(
            self.repo_name,
            "python_logo_copy.png",
            self.repo_name,
            "python_logo_copy2.png",
            options="&dry=1",
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_artifact_sync_download(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Artifact Sync Download tests."""
        r = self.af.artifacts_and_storage.artifact_sync_download(
            self.repo_name, self.artifact_path, options="?content=progress"
        )

        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    # Unsupported methods
    # def test_get_repository_replication_configuration():
    # def test_set_repository_replication_configuration():
    # def test_update_repository_replication_configuration():
    # def test_delete_repository_replication_configuration():
    # def test_scheduled_replication_status():
    # def test_pull_or_push_replication():
    # def test_update_local_multi_push_replication():
    # def test_delete_local_multi_push_replication():
    # def test_enable_or_disable_multiple_replications():
    # def test_global_system_replication_configuration():
    # def test_block_system_replication():
    # def test_unblock_system_replication():

    def test_file_list(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """File List tests."""
        r = self.af.artifacts_and_storage.file_list(self.repo_name, "")
        RtpyTestMixin.assert_isinstance_dict(r)
        r = self.af.artifacts_and_storage.file_list(self.repo_name, self.folder_name)
        RtpyTestMixin.assert_isinstance_dict(r)
        r = self.af.artifacts_and_storage.file_list(
            self.repo_name, self.folder_name, options="&mdTimestamps=0"
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_get_background_tasks(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Get Background Tasks tests."""
        r = self.af.artifacts_and_storage.get_background_tasks()
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_empty_trash_can(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Empty Trash Can tests."""
        r = self.af.artifacts_and_storage.empty_trash_can()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_delete_item_from_trash_can(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Delete Item From Trash Can tests."""
        r = self.af.artifacts_and_storage.delete_item(
            self.repo_name, self.artifact_path
        )
        path_in_trashcan = self.repo_name + "/" + self.artifact_path
        r = self.af.artifacts_and_storage.delete_item_from_trash_can(path_in_trashcan)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_restore_item_from_trash_can(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Restore Item From Trash Can tests."""
        r = self.af.artifacts_and_storage.delete_item(
            self.repo_name, self.artifact_path
        )
        path_in_trashcan = self.repo_name + "/" + self.artifact_path
        target_path = self.repo_name + "/" + "python_logo_restored.png"
        r = self.af.artifacts_and_storage.restore_item_from_trash_can(
            path_in_trashcan, target_path
        )
        r = self.af.artifacts_and_storage.file_info(
            self.repo_name, "python_logo_restored.png"
        )
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_optimize_system_storage(
        self,
        instantiate_af_objects_credentials_and_api_key,
        setup_then_destroy_test_env,
    ):
        """Optimize System Storage tests."""
        r = self.af.artifacts_and_storage.optimize_system_storage()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
