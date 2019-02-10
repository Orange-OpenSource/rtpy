# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the SEARCHES REST API Methods category."""


from .tools import RtpyBase


class RtpySearches(RtpyBase):
    """SEARCHES methods category."""

    def artifactory_query_language(self, query, **kwargs):
        """
        Search items using the Artifactory Query Language (AQL).

        Parameters
        ---------
        query: str
            The AQL string
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Artifactory Query Language"
        target = self._prefix + "aql"
        params = {"Content-Type": "text/plain"}
        return self._request(
            "POST", target, api_method, kwargs, data=query, params=params
        )

    """Old previously supported methods (code not updated for current rtpy)
    def artifact_search_quick_search(
            artifact_name, options=None,
            x_result_detail=None, **kwargs):

        # Artifact search by part of file name.
        # Searches return file info URIs.
        # Can limit search to specific repositories (local or caches).

        api_method = self._category + "Artifact Search Quick Search"
        target = self._prefix + 'artifact?name=' + artifact_name
        params = {}
        if x_result_detail:
            if x_result_detail not in ['info', 'properties',
                'info, properties']:
                message = "x_result_detail must be 'info', 'properties', " + \
                    "'info, properties'!"
                raise self.RtpyError(message)
            params['X-Result-detail'] = x_result_detail

        if options:
            target = target + options
        return request('GET', target, api_method, kwargs, params=params)

    # def archive_entries_search_class_search():
    # def gavc_search():


    def property_search(properties, options=None,
                        x_result_detail=None, **kwargs):
        api_method = self._category + "Property Search"
        target = self._prefix + 'prop?' + properties
        params = {}
        if x_result_detail:
            if x_result_detail not in ['info', 'properties',
                'info, properties']:
                message = "x_result_detail must be 'info', 'properties', " + \
                    "'info, properties'!"
                raise self.RtpyError(message)
            params['X-Result-detail'] = x_result_detail
        if options:
            target = target + options
        return request('GET', target, api_method, kwargs, params=params)


    def checksum_search(checksum_type, checksum_value, options=None,
                        x_result_detail=None, **kwargs):
        api_method = self._category + "Checksum Search"
        if checksum_type not in ['md5', 'sha1', 'sha256']:
            message = 'sha_type must be "md5", "sha1" or "sha256", ' + \
                'type given was "'+checksum_type+'"'
            raise self.RtpyError(message)

        target = self._prefix + 'checksum?' + checksum_type + \
                '=' + checksum_value
        params = {}
        if x_result_detail:
            if x_result_detail not in ['info', 'properties',
                'info, properties']:
                message = "x_result_detail must be 'info', 'properties', " + \
                    "'info, properties'!"
                raise self.RtpyError(message)
            params['X-Result-detail'] = x_result_detail
        if options:
            target = target + options
        return request('GET', target, api_method, kwargs, params=params)


    def bad_checksum_search(checksum_type, options=None,
                            **kwargs):
        api_method = self._category + "Bad Checksum Search"
        target = self._prefix + 'badChecksum?type=' + checksum_type
        if checksum_type not in ['md5', 'sha1']:
            message = 'sha_type must be "md5"or "sha1", ' + \
                'type given was "'+checksum_type+'"'
            raise self.RtpyError(message)

        if options:
            target = target + options
        return request('GET', target, api_method, kwargs)


    def artifacts_not_downloaded_since(not_used_since, options=None,
                                       **kwargs):
        api_method = self._category + "Artifacts Not Downloaded Since"
        target = self._prefix + 'usage?notUsedSince=' + not_used_since
        if options:
            target = target + options

        return request('GET', target, api_method, kwargs)
    """

    # Unsupported methods
    # def artifacts_with_date_in_date_range()
    # def artifacts_created_in_date_range()
    # def pattern_search()
    # def builds_for_dependcy()
    # def license_search()
    # def artifact_version_search()
    # def artifact_latest_version_search_based_on_layout()
    # def artifact_latest_version_search_based_on_properties()
    # def build_artifacts_search()

    def list_docker_repositories(self, repo_key, options=None, **kwargs):
        """
        List all Docker repositories (the registry's _catalog).

        (Hosted in an Artifactory Docker repository).

        Parameters
        ----------
        repo_key: str
            Key of the repository
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "List Docker Repositories"
        target = "docker/" + repo_key + "/v2/_catalog"
        target = self._append_to_string(target, options)
        return self._request("GET", target, api_method, kwargs)

    def list_docker_tags(self, repo_key, image_path, options=None, **kwargs):
        """
        List all tags of the specified Artifactory Docker repository.

        Parameters
        ----------
        repo_key: str
            Key of the repository
        image_path: str
            Path of the image in the repository
        options: str
            String of options
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "List Docker Tags"
        target = "docker/" + repo_key + "/v2/" + image_path + "/tags/list"
        target = self._append_to_string(target, options)
        return self._request("GET", target, api_method, kwargs)
