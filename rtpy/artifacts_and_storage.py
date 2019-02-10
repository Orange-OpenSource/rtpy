# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the ARTIFACTS AND STORAGE REST API Methods category."""

from .tools import RtpyBase


class RtpyArtifactsAndStorage(RtpyBase):
    """ARTIFACTS AND STORAGE methods category."""

    def folder_info(self, repo_key, folder_path, **kwargs):
        """
        Folder Info.

        For virtual use, the virtual repository returns the unified children.
        Supported by local, local-cached and virtual repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        folder_path: str
            The path of the folder in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Folder Info"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, folder_path)
        return self._request("GET", target, api_method, kwargs)

    def file_info(self, repo_key, file_path, **kwargs):
        """
        File Info.

        For virtual use the virtual repository returns the resolved file.
        Supported by local, local-cached and virtual repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        file_path: str
            The path of the file in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "File Info"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, file_path)
        return self._request("GET", target, api_method, kwargs)

    def get_storage_summary_info(self, **kwargs):
        """
        Return storage summary information.

        regarding binaries file store and repositories.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Storage Summary Info"
        target = "storageinfo"
        return self._request("GET", target, api_method, kwargs)

    def item_last_modified(self, repo_key, item_path, **kwargs):
        """
        Retrieve the last modified item at the given path.

        If the given path is a folder,
        the latest last modified item is searched for recursively.
        Supported by local and local-cached repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Item Last Modified"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, item_path)
        target = target + "?lastModified"
        return self._request("GET", target, api_method, kwargs)

    def file_statistics(self, repo_key, item_path, **kwargs):
        """
        Item statistics.

        Record the number of times an item was downloaded,
        last download date and last downloader.
        Supported by local and local-cached repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "File Statistics"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, item_path)
        target = target + "?stats"
        return self._request("GET", target, api_method, kwargs)

    def item_properties(self, repo_key, item_path, properties=None, **kwargs):
        """
        Item Properties. Optionally return only the properties requested.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        properties: str
            String of properties
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Item Properties"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, item_path)
        target = target + "?properties"
        if properties:
            target = target + "=" + properties
        return self._request("GET", target, api_method, kwargs)

    def set_item_properties(
        self, repo_key, item_path, properties, options=None, **kwargs
    ):
        """
        Attach properties to an item (file or folder).

        When a folder is used property attachment is recursive by default.
        Supported by local and local-cached repositories

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        properties: str
            String of properties
        options: str, optional
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Set Item Properties"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, item_path)
        target = target + "?properties=" + properties
        target = self._append_to_string(target, options)
        return self._request("PUT", target, api_method, kwargs)

    def delete_item_properties(
        self, repo_key, item_path, properties, options=None, **kwargs
    ):
        """
        Delete the specified properties from an item (file or folder).

        When a folder is used property removal is recursive by default.
        Supported by local and local-cached repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        properties: str
            String of properties
        options: str, optional
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Item Properties"
        target = self._prefix + repo_key
        target = self._add_forward_slash_if_not_empty(target, item_path)
        target = target + "?properties=" + properties
        target = self._append_to_string(target, options)
        return self._request("DELETE", target, api_method, kwargs)

    def set_item_sha256_checksum(self, params, **kwargs):
        """
        Calculate an artifact's SHA256 checksum and attaches it as a property.

        (with key "sha256"). If the artifact is a folder,
        then recursively calculates the SHA256 of each item in
        the folder and attaches the property to each item.

        Parameters
        ----------
        params: dict
            Dictionary comprised of {"repo_key": str, "path": str}
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Set Item SHA256 Checksum"
        target = "checksum/sha256"
        params["Content-Type"] = "application/json"
        return self._request("POST", target, api_method, kwargs, params=params)

    def retrieve_artifact(self, repo_key, artifact_path, **kwargs):
        """
        Retrieve an artifact from the specified destination.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        artifact_path: str
            Path of the artifact in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Retrieve Artifact"
        if artifact_path == "":
            message = "artifact path can't be empty !"
            raise self.RtpyError(message)
        target = "/" + repo_key + "/" + artifact_path
        return self._request(
            "GET", target, api_method, kwargs, byte_output=True, no_api=True
        )

    # Unsupported methods
    # def retrieve_latest_artifact():
    # def retrieve_build_artifacts_archive():

    def retrieve_folder_or_repository_archive(
        self, repo_key, path, archive_type, include_checksums=False, **kwargs
    ):
        """
        Retrieve an archive file (supports zip/tar/tar.gz/tgz).

        containing all the artifacts that reside under the specified path
        (folder or repository root). Requires Enable Folder Download to be set.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        path: str
            Path of the folder in the repository
        archive_type: str
            Type of archive
        include_checksums: bool, optional
            True to include checksums, False by default
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Retrieve Folder or Repository Archive"
        if archive_type not in ["zip", "tar", "tar.gz", "tgz"]:
            message = "archive_type must be zip, tar, tar.gz or tgz !"
            raise self.RtpyError(message)
        target = "archive/download/" + repo_key
        target = self._add_forward_slash_if_not_empty(target, path)
        target = target + "?archiveType=" + archive_type

        if include_checksums:
            target = target + "&includeChecksumFiles=true"
        if not include_checksums:
            target = target + "&includeChecksumFiles=false"
        return self._request("GET", target, api_method, kwargs, byte_output=True)

    def trace_artifact_retrieval(self, repo_key, item_path, **kwargs):
        """
        Simulate an artifact retrieval request from the specified.

        location and returns verbose output about the resolution process.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Trace Artifact Retrieval"
        target = "/" + repo_key + "/" + item_path + "?trace"
        return self._request("GET", target, api_method, kwargs, no_api=True)

    # def archive_entry_download():

    def create_directory(self, repo_key, directory_path, **kwargs):
        """
        Create new directory at the specified destination.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        directory_path: str
            Path of the directory in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create Directory"
        target = "/" + repo_key + "/" + directory_path + "/"
        return self._request("PUT", target, api_method, kwargs, no_api=True)

    def deploy_artifact(
        self, repo_key, local_artifact_path, target_artifact_path, **kwargs
    ):
        """
        Deploy an artifact to the specified destination.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        local_artifact_path: str
            Local path of the artifact to upload
        target_artifact_path: str
            Target path of the artifact in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Deploy Artifact"
        target = "/" + repo_key + "/" + target_artifact_path
        with open(local_artifact_path, "rb") as files:
            return self._request(
                "PUT", target, api_method, kwargs, data=files, no_api=True
            )

    def deploy_artifact_by_checksum(
        self, repo_key, target_artifact_path, sha_type, sha_value, **kwargs
    ):
        """
        Deploy an artifact to the specified destination.

        By checking if the artifact content already exists in Artifactory.
        If Artifactory already contains a user readable artifact with
        the same checksum the artifact content is copied over to
        the new location and return a response
        without requiring content transfer.
        Otherwise, a 404 error is returned to indicate
        that content upload is expected in order to deploy the artifact.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        target_artifact_path: str
            Target path of the artifact in the repository
        sha_type: str
            Type of secure hash
        sha_value: str
            Value of the secure hash
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Deploy Artifact By Checksum"
        if sha_type not in ["sha1", "sha256"]:
            message = (
                'sha_type must be "sha1" or "sha256", '
                + 'type given was "'
                + sha_type
                + '"'
            )
            raise self.RtpyError(message)

        params = {}
        params["X-Checksum-Deploy"] = True
        if sha_type == "sha1":
            params["X-Checksum-Sha1"] = sha_value
        if sha_type == "sha256":
            params["X-Checksum-Sha256"] = sha_value
        target = "/" + repo_key + "/" + target_artifact_path
        return self._request(
            "PUT", target, api_method, kwargs, no_api=True, params=params
        )

    # Unsupported methods
    # def deploy_artifacts_from_archive()
    # def push_a_set_of_artifacts_to_bintray()
    # def push_docker_tag_to_bintray()
    # def distribute_artifact()
    # def file_compliance_info()

    def delete_item(self, repo_key, path_to_item, **kwargs):
        """
        Delete a file or a folder from the specified destination.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        path_to_item: str
            Path of the item in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Item"
        target = "/" + repo_key + "/" + path_to_item
        return self._request("DELETE", target, api_method, kwargs, no_api=True)

    def copy_item(
        self,
        src_repo_key,
        src_item_path,
        target_repo_key,
        target_item_path,
        options=None,
        **kwargs
    ):
        """
        Copy an artifact or a folder to the specified destination.

        Supported by local repositories only.

        Parameters
        ----------
        src_repo_key: str
            Key of the source repository
        src_item_path: str
            Path of the item in the source repository
        target_repo_key: str
            Key of the target repository
        target_item_path: str
            Path of the item in the target repository
        options: str, optional
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Copy Item"
        target = "copy/" + src_repo_key
        target = self._add_forward_slash_if_not_empty(target, src_item_path)
        target = target + "?to=/" + target_repo_key
        if target_repo_key != "":
            target = target + "/" + target_item_path
        target = self._append_to_string(target, options)
        return self._request("POST", target, api_method, kwargs)

    def move_item(
        self,
        src_repo_key,
        src_item_path,
        target_repo_key,
        target_item_path,
        options=None,
        **kwargs
    ):
        """
        Move an artifact or a folder to the specified destination.

        Supported by local repositories only.

        Parameters
        ----------
        src_repo_key: str
            Key of the source repository
        src_item_path: str
            Path of the item in the source repository
        target_repo_key: str
            Key of the target repository
        target_item_path: str
            Path of the item in the target repository
        options: str, optional
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Move Item"
        target = "move/" + src_repo_key
        target = self._add_forward_slash_if_not_empty(target, src_item_path)
        target = target + "?to=/" + target_repo_key
        if target_repo_key != "":
            target = target + "/" + target_item_path
        target = self._append_to_string(target, options)
        return self._request("POST", target, api_method, kwargs)

    # Unsupported methods
    # def get_repository_replication_configuration():
    # def set_repository_replication_configuration():
    # def update_repository_replication_configuration():
    # def delete_repository_replication_configuration():
    # def scheduled_replication_status():
    # def pull_or_push_replication():
    # def update_local_multi_push_replication():
    # def delete_local_multi_push_replication():
    # def enable_or_disable_multiple_replications():
    # def global_system_replication_configuration():
    # def block_system_replication():
    # def unblock_system_replication():

    def artifact_sync_download(self, repo_key, artifact_path, options=None, **kwargs):
        """
        Download an artifact.

        With or without returning
        he actual content to the client.

        When tracking the progress marks are printed
        (by default every 1024 bytes).
        This is extremely useful
        if you want to trigger downloads on a remote Artifactory server,
        for example to force eager cache population of large artifacts,
        but want to avoid the bandwidth consumption involved in transferring
        the artifacts to the triggering client.
        If no content parameter is specified
        the file content is downloaded to the client.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        artifact_path: str
            Path of the artifact in the repository
        options: str, optional
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Artifact Sync Download"
        if artifact_path == "":
            message = "artifact path can't be empty !"
            raise self.RtpyError(message)
        target = "download/" + repo_key + "/" + artifact_path
        target = self._append_to_string(target, options)
        return self._request("GET", target, api_method, kwargs)

    def file_list(self, repo_key, folder_path, options=None, **kwargs):
        """
        Get a flat (the default) or deep listing of the files and folders.

        (not included by default) within a folder
        For deep listing you can specify an optional
        depth to limit the results.
        Optionally include a map of metadata timestamp values
        as part of the result

        Parameters
        ----------
        repo_key: str
            Key of the repository
        folder_path: str
            Path of the folder in the repository
        options: str, optional
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "File List"
        target = "storage/" + repo_key
        target = self._add_forward_slash_if_not_empty(target, folder_path)
        target = target + "?list"
        target = self._append_to_string(target, options)
        return self._request("GET", target, api_method, kwargs)

    def get_background_tasks(self, **kwargs):
        """
        Retrieve list of background tasks currently scheduled.

        Or running in Artifactory
        In HA, the nodeId is added to each task.
        Task can be in one of few states: scheduled,
        running, stopped, canceled.
        Running task also shows the task start time.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Background Tasks"
        target = "tasks"
        return self._request("GET", target, api_method, kwargs)

    def empty_trash_can(self, **kwargs):
        """
        Empty the trash can permanently deleting all its current contents.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Empty Trash Can"
        target = "trash/empty"
        return self._request("POST", target, api_method, kwargs)

    def delete_item_from_trash_can(self, path_in_trashcan, **kwargs):
        """
        Permanently delete an item from the trash can.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Item From Trash Can"
        target = "trash/clean/" + path_in_trashcan
        return self._request("DELETE", target, api_method, kwargs)

    def restore_item_from_trash_can(self, path_in_trashcan, target_path, **kwargs):
        """
        Restore an item from the trash can.

        Parameters
        ----------
        path_in_trashcan: str
            Path of the item in the trashcan (repo_name/folder/file)
        target_path: str
            Where to restore the item (repo_name/folder/file)

        """
        api_method = self._category + "Restore Item From Trash Can"
        target = "trash/restore/" + path_in_trashcan + "?to=" + target_path
        return self._request("POST", target, api_method, kwargs)

    def optimize_system_storage(self, **kwargs):
        """
        Raise a flag to invoke balancing between redundant storage units.

        Of a sharded filestore following the next garbage collection.

        """
        api_method = self._category + "Optimize System Storage"
        target = "system/storage/optimize"
        return self._request("POST", target, api_method, kwargs)

    # Unsupported methods
    # def get_puppet_modules()
    # def get_puppet_module()
    # def get_puppet_releases()
    # def get_puppet_release()
