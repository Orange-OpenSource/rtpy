# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the SUPPORT REST API Methods category."""


from .tools import RtpyBase


class RtpySupport(RtpyBase):
    """SUPPORT methods category."""

    def create_bundle(self, params, **kwargs):
        """
        Create a new support bundle.

        Parameters
        ----------
        params: dict
            Settings of the bundle
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create Bundle"
        target = self._prefix + "bundles/"
        return self._request("POST", target, api_method, kwargs, params=params)

    def list_bundles(self, **kwargs):
        """
        List previously created bundle currently stored in the system.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "List Bundles"
        target = self._prefix + "bundles/"
        return self._request("GET", target, api_method, kwargs)

    def get_bundle(self, bundle_name, **kwargs):
        """
        Download a previously created bundle currently stored in the system.

        Parameters
        ----------
        bundle_name: str
            Name of the bundle
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Bundle"
        if bundle_name[:33] == "/artifactory/api/support/bundles/":
            bundle_name = bundle_name[33:]
        target = self._prefix + "bundles/" + bundle_name
        params = {"Content-Type": "application/json"}
        return self._request(
            "GET", target, api_method, kwargs, byte_output=True, params=params
        )

    def delete_bundle(self, bundle_name, **kwargs):
        """
        Delete a previously created bundle from the system.

        Parameters
        ----------
        bundle_name: str
            Name of the bundle
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Bundle"
        target = self._prefix + "bundles" + bundle_name
        return self._request("DELETE", target, api_method, kwargs)
