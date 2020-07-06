# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Rtpy class definition with it's attributes which is exposed to the end user."""

from copy import deepcopy

from .tools import RtpyBase
from .artifacts_and_storage import RtpyArtifactsAndStorage
from .builds import RtpyBuilds
from .repositories import RtpyRepositories
from .searches import RtpySearches
from .security import RtpySecurity
from .system_and_configuration import RtpySystemAndConfiguration


class Rtpy(RtpyBase):
    """
    Main parent class.

    Attributes are the classes are the methods categories.

    Parameters
    ---------
    settings: dict
        The user settings, mandaroty keys are "af_url" and "api_key"
        or "username" and "password".

    Attributes
    ----------
    artifacts_and_storage: rtpy.artifacts_and_storage.RtpyArtifactsAndStorage
        Category for multiple API methods
    buils: rtpy.builds.RtpyBuilds
        Category for multiple API methods
    repositories: rtpy.repositories.RtpyRepositories
        Category for multiple API methods
    searches: rtpy.searches.RtpySearches
        Category for multiple API methods
    security: rtpy.security.RtpySecurity
        Category for multiple API methods
    support: rtpy.support.RtpySupport
        Category for multiple API methods
    system_and_configuration: rtpy.system_and_configuration.RtpySystemAndConfiguration
        Category for multiple API methods
    settings: dict
        Previously supplied settings at class instantiation

    """

    def __init__(self, settings):
        """Object Instantiation."""
        settings = deepcopy(settings)
        self.artifacts_and_storage = RtpyArtifactsAndStorage(
            settings, "storage/", "[ARTIFACTS & STORAGE] : "
        )
        self.builds = RtpyBuilds(settings, "build/", "[BUILDS] : ")
        self.repositories = RtpyRepositories(
            settings, "repositories/", "[REPOSITORIES] : "
        )
        self.searches = RtpySearches(settings, "search/", "[SEARCHES] : ")
        self.security = RtpySecurity(settings, "security/", "[SECURITY] : ")
        self.system_and_configuration = RtpySystemAndConfiguration(
            settings, "system/", "[SYSTEM & CONFIGURATION] : "
        )
        self.settings = settings

    def __call__(self):
        """Shortcut to all the system health ping method to verify connectivity."""
        return self.system_and_configuration.system_health_ping()
