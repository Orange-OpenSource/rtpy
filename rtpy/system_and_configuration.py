# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the SYSTEM AND CONFIGURATION  REST API Methods category."""

from .tools import RtpyBase


class RtpySystemAndConfiguration(RtpyBase):
    """SYSTEM AND CONFIGURATION methods category."""

    def system_info(self, **kwargs):
        """
        Get general system information.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "System Info"
        return self._request("GET", self._prefix, api_method, kwargs)

    def system_health_ping(self, **kwargs):
        """
        Get a simple status response about the state of Artifactory.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "System Health Ping"
        target = self._prefix + "ping"
        return self._request("GET", target, api_method, kwargs)

    # def verify_connection()

    def general_configuration(self, **kwargs):
        """
        Get the general configuration (artifactory.config.xml).

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "General Configuration"
        target = self._prefix + "configuration"
        return self._request("GET", target, api_method, kwargs)

    def save_general_configuration(self, xml_file_path, **kwargs):
        """
        Save the general configuration (artifactory.config.xml).

        Parameters
        ----------
        xml_file_path: str
            Path of the xml file to POST
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Save General Configuration"
        target = self._prefix + "configuration"
        myparams = {"Content-Type": "application/xml"}
        with open(xml_file_path, "rb") as files:
            return self._request(
                "POST", target, api_method, kwargs, params=myparams, data=files
            )

    # Unsupported method
    # def update_custom_url_base(new_url)

    def license_information(self, **kwargs):
        """
        Retrieve information about the currently installed license.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Licence Information"
        target = self._prefix + "license"
        return self._request("GET", target, api_method, kwargs)

    def install_license(self, params, **kwargs):
        """
        Install new license key or change the current one.

        Parameters
        ----------
        params: str
           Settings of the license
        **kwargs
            Keyword arguments

        """
        # The JSON output in case of an error is currently incorrect
        api_method = self._category + "Install License"
        target = self._prefix + "license"
        return self._request("POST", target, api_method, kwargs, params=params)

    # Unsupported methods
    # def ha_license_information()
    # def install_ha_cluster_licenses()
    # def delete_ha_cluster_license()

    def version_and_addons_information(self, **kwargs):
        """
        Retrieve information about versions and addons.

        (the current Artifactory version, revision, and currently installed Add-ons).

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Versions and Add-ons Information"
        target = self._prefix + "version"
        return self._request("GET", target, api_method, kwargs)

    def get_reverse_proxy_configuration(self, **kwargs):
        """
        Retrieve the reverse proxy configuration.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Reverse Proxy Configuration"
        target = self._prefix + "configuration/webServer"
        return self._request("GET", target, api_method, kwargs)

    # Unsupported method
    # def update_reverse_proxy_configuration()

    def get_reverse_proxy_snippet(self, **kwargs):
        """
        Get the reverse proxy configuration snippet in text format.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Reverse Proxy Snippet"
        target = self._prefix + "configuration/reverseProxy/nginx"
        return self._request("GET", target, api_method, kwargs)
