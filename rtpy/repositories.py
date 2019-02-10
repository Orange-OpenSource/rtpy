# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the REPOSITORIES REST API Methods category."""

from .tools import RtpyBase


class RtpyRepositories(RtpyBase):
    """REPOSITORIES methods category."""

    def get_repositories(self, options=None, **kwargs):
        """
        Return a list of minimal repository details.

        For all repositories of the specified type.

        Parameters
        ----------
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Repositories"
        target = self._append_to_string("repositories", options)
        return self._request("GET", target, api_method, kwargs)

    def repository_configuration(self, repo_key, **kwargs):
        """
        Retrieve the current configuration of a repository.

        Supported by local, remote and virtual repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Repository Configuration"
        target = self._prefix + repo_key
        return self._request("GET", target, api_method, kwargs)

    def create_repository(self, params, **kwargs):
        """
        Create a new repository in Artifactory with the provided configuration.

        Supported by local, remote and virtual repositories.
        A position may be specified using the pos parameter.
        If the map size is shorter than pos the repository is the last one
        (the default behavior).

        Parameters
        ----------
        params: dict
            Parameters of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create Repository"
        repo_key = params["key"]
        target = self._prefix + repo_key
        return self._request("PUT", target, api_method, kwargs, params=params)

    def update_repository_configuration(self, params, **kwargs):
        """
        Update an exiting repository configuration in Artifactory.

        With the provided configuration elements.
        Supported by local, remote and virtual repositories.

        Parameters
        ----------
        params: dict
            Parameters of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Update Repository Configuration"
        repo_key = params["key"]
        target = self._prefix + repo_key
        params["Content-Type"] = "application/json"
        return self._request("POST", target, api_method, kwargs, params=params)

    def delete_repository(self, repo_key, **kwargs):
        """
        Remove a repository.

        Configuration together with the whole repository content.
        Supported by local, remote and virtual repositories

        Parameters
        ----------
        repo_key: str
            Key of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Repository"
        target = self._prefix + repo_key
        return self._request("DELETE", target, api_method, kwargs)

    def calculate_yum_repository_metadata(
        self, repo_key, x_gpg_passphrase=None, options=None, **kwargs
    ):
        """
        Calculate/recalculate the YUM metdata for a repository.

        Based on the RPM package currently hosted in the repository.
        Supported by local and virtual repositories only.
        Calculation can be synchronous (the default) or asynchronous.
        For Virtual repositories, calculates the merged metadata
        from all aggregated repositories on the specified path.
        The path parameter must be passed for virtual calculation.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        x_gpg_passphrase: str
            Passphrase
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate YUM Repository Metadata"
        target = "yum/" + repo_key
        target = self._append_to_string(target, options)
        params = {}
        if x_gpg_passphrase:
            params["X-GPG-PASSPHRASE"] = x_gpg_passphrase
        return self._request("POST", target, api_method, kwargs, params=params)

    def calculate_nuget_repository_metadata(self, repo_key, **kwargs):
        """
        Recalculate all the NuGet packages for a repository.

        (local/cache/virtual), and re-annotate the NuGet properties
        for each NuGet package according to it's internal nuspec file.
        Please see the NuGet integration documentation for more details.
        Supported by local, local-cache, remote and virtual repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate NuGet Repository Metadata"
        target = "nuget/" + repo_key + "/reindex"
        return self._request("POST", target, api_method, kwargs)

    def calculate_npm_repository_metadata(self, repo_key, **kwargs):
        """
        Recalculate the npm search index for this repository (local/virtual).

        Please see the Npm integration documentation for more details.
        Supported by local and virtual repositories.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Npm Repository Metadata"
        target = "npm/" + repo_key + "/reindex"
        return self._request("POST", target, api_method, kwargs)

    def calculate_maven_index(self, options, **kwargs):
        """
        Calculates/caches a Maven index for the specified repositories.

        For a virtual repository specify all underlying repositories
        that you want the aggregated index to include.
        Calculation can be forced, which for remote repositories
        will cause downloading of a remote index even if a locally
        ached index has not yet expired;
        and index recalculation based on the cache
        on any failure to download the remote index,
        including communication errors
        (the default behavior is to only use the cache when a remote index
        cannot be found and returns a 404). Forcing has no effect
        on local repositories index calculation.

        Parameters
        ----------
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Maven Index"
        target = "maven?" + options
        return self._request("POST", target, api_method, kwargs)

    def calculate_maven_metadata(self, repo_key, folder_path, options=None, **kwargs):
        """
        Calculate Maven metadata on the specified path.

        (local repositories only).

        Parameters
        ----------
        repo_key: str
            Key of the repository
        folder_path: str
            Path of the folder in the repository
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Maven Metadata"
        target = "maven/calculateMetadata/" + repo_key + "/" + folder_path
        target = self._append_to_string(target, options)

        return self._request("POST", target, api_method, kwargs)

    # Unsupported ressource intensive methods

    def calculate_debian_repository_metadata(
        self, repo_key, x_gpg_passphrase=None, options=None, **kwargs
    ):
        """
        Calculate/recalculate the Packages and Release metadata.

        for this repository, based on the Debian packages in it.
        Calculation can be synchronous (the default) or asynchronous.
        Please refer to Debian Repositories for more details.
        Supported by local repositories only.
        From version 4.4, by default, the recalculation process
        also writes several entries from the Debian package's
        metadata as properties on all of the artifacts (based on the control
        file's content).
        This operation may not always be required
        (for example, if the Debian files are intact and were not modified,
        only the index needs to be recalculated.
        The operation is resource intensive and can be disabled by
        passing the ?writeProps=0 query param.
        From version 5.7, the target repository can be a virtual repository.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        x_gpg_passphrase: str
            Passphrase
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Debian Repository Metadata"
        target = "deb/reindex/" + repo_key
        target = self._append_to_string(target, options)
        params = {}
        if x_gpg_passphrase:
            params["X-GPG-PASSPHRASE"] = x_gpg_passphrase
        return self._request("POST", target, api_method, kwargs, params=params)

    def calculate_opkg_repository_metadata(
        self, repo_key, x_gpg_passphrase=None, options=None, **kwargs
    ):
        """
        Calculate/recalculate the Packages and Release metadata fora repository.

        Based on the ipk packages in it (in each feed location).
        Calculation can be synchronous (the default) or asynchronous.
        Please refer to Opkg Repositories for more details.
        Supported by local repositories only.
        By default, the recalculation process also writes several entries
        from the ipk package's metadata as properties on all of the artifacts
        (based on the control file's content).
        This operation may not always be required
        (for example, if the ipk files are intact and were not modified,
        only the index needs to be recalculated.
        The operation is resource intensive and can be disabled by passing
        the ?writeProps=0 query param.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        x_gpg_passphrase: str
            Passphrase
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Opkg Repository Metadata"
        target = "opkg/reindex/" + repo_key
        target = self._append_to_string(target, options)
        params = {}
        if x_gpg_passphrase:
            params["X-GPG-PASSPHRASE"] = x_gpg_passphrase
        return self._request("POST", target, api_method, kwargs, params=params)

    def calculate_bower_index(self, repo_key, **kwargs):
        """
        Recalculate the index for a Bower repository.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Bower Index"
        target = "bower/" + repo_key + "/" + "reindex"
        return self._request("POST", target, api_method, kwargs)

    def calculate_helm_chart_index(self, repo_key, **kwargs):
        """
        Calculate Helm chart index on the specified path.

        (local repositories only).

        Parameters
        ----------
        repo_key: str
            Key of the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Helm Chart Index"
        target = "helm/" + repo_key + "/" + "reindex"
        return self._request("POST", target, api_method, kwargs)

    def calculate_cran_repository_metadata(self, repo_key, options=None, **kwargs):
        """
        Calculates/recalculates the Packages and Release metadata for a repository.

        Based on the CRAN packages in it.
        The calculation can be synchronous (the default) or asynchronous.
        Please refer to CRAN Repositories for more details.
        Supported by local repositories only.
        From version 6.1, by default, the recalculation process
        also writes several entries from the CRAN package's metadata
        as properties on all of the artifacts (based on the control file's content).

        Parameters
        ----------
        repo_key: str
            Key of the repository
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate CRAN Repository Metadata"
        target = "cran/reindex/" + repo_key
        target = self._append_to_string(target, options)
        return self._request("POST", target, api_method, kwargs)

    def calculate_conda_repository_metadata(self, repo_key, options=None, **kwargs):
        """
        Calculate/recalculate the Conda packages and release metadata for a repository.

        The calculation can be synchronous (the default) or asynchronous.
        Please refer to Conda Repositories for more details.
        Supported for local repositories only

        Parameters
        ----------
        repo_key: str
            Key of the repository
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Calculate Conda Repository Metadata"
        target = "conda/reindex/" + repo_key
        target = self._append_to_string(target, options)
        return self._request("POST", target, api_method, kwargs)
