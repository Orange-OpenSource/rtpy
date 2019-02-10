# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the BUILDS REST API Methods category."""


from .tools import RtpyBase


class RtpyBuilds(RtpyBase):
    """BUILDS methods category."""

    def all_builds(self, **kwargs):
        """Provide information on all builds.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "All Builds"
        return self._request("GET", "build", api_method, kwargs)

    # Unsupported methods
    # def build_runs()
    # def build_upload()
    # def build_info()
    # def builds_diff()
    # def build_promotion()
    # def promote_docker_image()
    # def delete_builds()
    # def push_build_to_bintray()
    # def distribute_build()
    # def control_build_retention()
