# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions and classes used by the main categories of methods."""

from __future__ import unicode_literals
import json
import sys
from copy import deepcopy

import requests
from requests.exceptions import HTTPError


class RtpyBase(object):
    """
    Rtpy Base class.

    Attributes
    ----------
    _prefix: str
        API endpoint used for a given API method category ("search/"...)
    _category: str
        Major API method category (Searches, Repositories...)
    _user_settings: dict
        Complete user settings, default values are changed at class instantiation

    """

    def __init__(self, provided_settings, prefix, category):
        """
        Object instantiation.

        User settings get set and verified, _category and _prefix attributes are set.

        Parameters
        ----------
        provided_settings: str
            Original settings dict supplied by the user from the rtpy.Rtpy class
        prefix: str
            API endpoint used for a given API method category ("search/"...)
        category: str
            Major API method category (Searches, Repositories...)

        """
        self._category = category
        self._prefix = prefix
        self._user_settings = {
            "af_url": None,
            "api_key": None,
            "username": None,
            "password": None,
            "raw_response": False,
            "verbose_level": 0,
            "auth": (),
            "X-JFrog-Art-Api": None,
            "api_endpoint": None,
            "session": requests.Session(),
        }
        self._configure_user_settings(provided_settings)
        self._validate_user_settings()

    def _check_provided_keys_in_settings(self, provided_settings):
        """
        Check if the provided settings only modify the correct fields.

        Parameters
        ----------
        provided_settings: str
            Original settings dict supplied by the user from the rtpy.Rtpy class

        Raises
        ------
        UserSettingsError
            If the settings are invalid

        Returns
        -------
        None
            Nothing

        """
        allowed_settings_keys = [
            "af_url",
            "api_key",
            "username",
            "password",
            "raw_response",
            "verbose_level",
            "session",
        ]

        message = ""
        for setting in allowed_settings_keys:
            message += '"' + str(setting) + '" '

        message += (
            "are the only settings "
            "that can provided!\n"
            "Offending key(s) supplied : "
        )

        offending_keys = (
            key for key in provided_settings if key not in allowed_settings_keys
        )
        offending_keys = tuple(key for key in offending_keys)
        for key in offending_keys:
            message += '"{}" '

        message = message.format(*offending_keys)
        if offending_keys:
            raise UserSettingsError(message)

    def _configure_user_settings(self, provided_settings):
        """
        Configure or update user settings.

        Returns
        -------
        None
            Nothing

        """
        self._check_provided_keys_in_settings(provided_settings)
        self._original_user_settings = deepcopy(self._user_settings)
        for setting in provided_settings:
            self._user_settings[setting] = provided_settings[setting]

    def _restore_user_settings(self):
        """Restore original user settings."""
        self._user_settings = self._original_user_settings

    def _validate_user_settings(self):
        """
        Verify if the _user_settings attribute dict is valid.

        Raises
        ------
        UserSettingsError
            If the _user_settings dict is invalid

        Returns
        -------
        None
            Nothing

        """
        if (
            not self._user_settings["af_url"]
            or not self._user_settings["api_key"]
            and (
                not self._user_settings["username"]
                or not self._user_settings["password"]
            )
        ):

            message = (
                "An af_url, and api_key or username and password "
                + "must be provided in a dictionary to set the user settings!"
            )
            raise UserSettingsError(message)

        if self._user_settings["api_key"] and (
            self._user_settings["username"] or self._user_settings["password"]
        ):
            message = (
                "An api_key and user name and password"
                + " can't be provided at the same time!"
            )
            raise UserSettingsError(message)

        self._user_settings["auth"] = None
        if self._user_settings["username"] and self._user_settings["password"]:
            self._user_settings["auth"] = (
                self._user_settings["username"],
                self._user_settings["password"],
            )

        self._user_settings["X-JFrog-Art-Api"] = self._user_settings["api_key"]
        self._user_settings["api_endpoint"] = self._user_settings["af_url"] + "/api/"

        allowed_raw_response = [False, True]
        allowed_verbose_level = [0, 1]

        if self._user_settings["raw_response"] not in allowed_raw_response:
            raise UserSettingsError(
                "raw_response must be " + str(allowed_raw_response) + "!"
            )

        if self._user_settings["verbose_level"] not in allowed_verbose_level:
            raise UserSettingsError(
                "verbose_level must be " + str(allowed_verbose_level) + "!"
            )

    def _request(
        self,
        verb,
        target,
        api_method,
        kwargs,
        byte_output=False,
        no_api=False,
        data=None,
        params=None,
    ):
        """
        Call the remote API, process the response and return it.

        Parameters
        ----------
        verb: str
            HTTP verb ("GET", "POST"...)
        target: str
            API sub endpoint specific for the method
        api_method: str
            Name of the specific method (category and name)
        kwargs: dict
            Dictionary of keyword arguments (supplied by the method)
        byte_output: bool
            True will return a raw requests.Response() object
            True indicates that the result of the method will be used to download
            a file/artifact
            False by default
        no_api: bool
            True to remove 'api/' from the target endpoint
            False by default
        data
            Python requests data keyword argument
        params
            Python requests json keyword argument

        Returns
        -------
        response
                The result of the processed request.Response()
                given by _convert_response method

        """
        # Checking if the settings kwarg was supplied
        settings = self._settings_if_settings_in_kwargs(kwargs)
        if settings:
            self._configure_user_settings(settings)
            self._validate_user_settings()

        headers = {}

        if self._user_settings["X-JFrog-Art-Api"]:
            headers = {"X-JFrog-Art-Api": self._user_settings["X-JFrog-Art-Api"]}

        auth = self._user_settings["auth"]
        raw_response = self._user_settings["raw_response"]

        # Changing the endpoint when necessary
        if not no_api:
            request_url = self._user_settings["api_endpoint"] + target
        if no_api:
            request_url = self._user_settings["af_url"] + target

        possible_headers = [
            "Content-Type",
            "X-Checksum-Deploy",
            "X-Checksum-Sha1",
            "X-Checksum-Sha256",
            "X-Result-detail",
            "X-GPG-PASSPHRASE",
        ]
        # Extracting the headers from the params dict
        if params:

            headers_to_add = [field for field in params if field in possible_headers]

            for header in headers_to_add:
                headers[header] = str(params[header])
                del params[header]
        else:
            params = None

        if self._user_settings["verbose_level"] >= 1:
            message = (
                "\n\nPerforming Artifactory REST API operation : "
                + api_method
                + "\nVerb : "
                + verb
                + "\nURL : "
                + request_url
            )
            sys.stdout.write(message)

        response = self._user_settings["session"].request(
            verb, request_url, headers=headers, json=params, data=data, auth=auth
        )

        if self._user_settings["verbose_level"] >= 1:
            message = "\nStatus Code : " + str(response.status_code) + "\n"
            sys.stdout.write(message)

        if settings:
            self._restore_user_settings()

        return self._convert_response(
            api_method, request_url, verb, response, raw_response, byte_output
        )

    def _convert_response(
        self, api_method, target, verb, response, raw_response, byte_output
    ):
        """
        Convert (if necessary) a requests.Response() object raise an error.

        If response.text is of json format, a Python dict will be returned
        or an error if that dict is an error output dict
        Else a raw response.text will be returned

        A raw Python Requests response object is returned if raw_response
        or byte_output is true

        Parameters
        ----------
        api_method: str
            Name of the specific method (category and name)
        target: str
            API sub endpoint specific for the method
        verb: str
            HTTP verb ("GET", "POST"...)
        response: requests.Response
            The requests.Response object for the API call
        raw_response: bool
            True to return the original requests.Response
        byte_output: bool
            True to return the original requests.Response if no errors are found

        Raises
        ------
        error
            An error raised by the _process_and_raise_error method

        Returns
        -------
        response: requests.Response or str or dict
            The returned response to the client

        """
        if raw_response:
            return response

        # Trying to see if the response content can be loaded as a json
        bad_status_codes = list(range(400, 600))
        if response.status_code in bad_status_codes:
            self._process_and_raise_error(response, api_method, target, verb)

        if not raw_response:
            try:
                if byte_output:
                    return response
                else:
                    response2 = response.json()
                    return response2

            except ValueError:
                return response.text

    def _process_and_raise_error(self, response, api_method, target, verb):
        """
        Look for errors in a requests.Response object from the Artifactory REST API.

        Parameters
        ----------
        response: requests.Response()
            Original response for the API call
        api_method: str
            Name of the specific method (category and name)
        target: str
            API sub endpoint specific for the method
        verb: str
            HTTP verb ("GET", "POST"...)

        Raises
        ------
        MalformedAfApiError
            If there is an error but the JSON is malformed
        AfApiError
            If the is an error
            and the JSON is a standard Artifactory REST API error JSON

        """
        malformed_json = False
        error_details = None
        try:
            json_content = response.json()
            if "errors" in json_content:
                message = json_content["errors"][0]["message"]
                if "status" in json_content["errors"][0]:
                    status_code = json_content["errors"][0]["status"]
                else:
                    status_code = response.status_code

                error_details = {
                    "api_method": api_method,
                    "url": target,
                    "verb": verb,
                    "status_code": status_code,
                    "message": message,
                }
            if not error_details:
                malformed_json = True
        except ValueError:
            malformed_json = True

        if malformed_json:
            message = (
                "The json output for the error was malformed "
                "(Not a standard Artifactory REST API error json), "
                'set the "raw_response" setting to True in your '
                "settings dictionary to get a raw requests.Response() object "
                "for debugging!, requests.Response.text : {}".format(response.text)
            )
            raise self.MalformedAfApiError(message)
        else:
            raise self.AfApiError(error_details)

    def _append_to_string(self, target, options):
        """
        Add a string of options to a target string (URL in this case).

        Parameters
        ----------
        target: str
            API sub endpoint specific for the method
        options: str
            String of options

        Returns
        -------
        target: str
            The target with the string of options appended to it

        """
        if options:
            target += options
            return target
        return target

    def _add_forward_slash_if_not_empty(self, target, path):
        """
        Add a forward slash to a string if the other string != "".

        Parameters
        ----------
        target: str
            API sub endpoint specific for the method
        path: str
            Path in the sub endpoint (usually and item)

        """
        if path != "":
            target += "/" + path
            return target
        return target

    def _settings_if_settings_in_kwargs(self, kwargs):
        """
        Extract the settings key from the kwargs dict and return it if present.

        Parameters
        ----------
        kwargs: dict
            Keyword arguments

        Returns
        -------
        settings: dict or None
            The settings dict if in kwargs, None otherwise

        """
        if "settings" in kwargs:
            settings = kwargs["settings"]
        else:
            settings = None
        return settings

    class MalformedAfApiError(HTTPError):
        """Raised when encountering a malformed Artifactory REST API error JSON."""

        pass

    class AfApiError(HTTPError):
        """
        Raised when encountering a standard Artifactory REST API error JSON.

        Attributes
        ----------
        api_method: str
            Name of the specific method (category and name)
        url: str
            Full URL used for API call
        verb: str
            HTTP verb used for the API call ("GET", "POST"...)
        status_code: int
            HTTP status code for the API call
        message: str
            Error message given by the Artifactory REST API
        print_message: str
            Well formatted multiline message with all the attributes

        """

        def __init__(self, error_details):
            """Error object instantiation."""
            self.api_method = error_details["api_method"]
            self.url = error_details["url"]
            self.verb = error_details["verb"]
            self.status_code = error_details["status_code"]
            self.message = error_details["message"]
            self.print_message = (
                "\nArtifactory REST API operation : "
                + self.api_method
                + "\nURL : "
                + self.url
                + "\nVerb : "
                + self.verb
                + "\nStatus Code : "
                + str(self.status_code)
                + "\nMessage : "
                + self.message
            )
            HTTPError.__init__(self, self.print_message)

    class RtpyError(ValueError):
        """
        Raised if arguments are wrong or incomplete for a method.

        This error is used as a preemptive measure in some methods to check arguments.

        """

        pass


class UserSettingsError(ValueError):
    """Raised if some of the provided settings are incorrect or missing."""

    pass


def json_to_dict(json_file_path):
    """
    Convert a .json file to a Python dictionary.

    Parameters
    ----------
    json_file_path: str
        Path of the JSON file

    Returns
    -------
    dictionary: dict
        The original JSON file as a Python dictionary

    """
    with open(json_file_path, "r") as json_data:
        dictionary = json.load(json_data, encoding="utf8")
        return dictionary
