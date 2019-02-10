# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Functions for the SECURITY REST API Methods category."""

from .tools import RtpyBase


class RtpySecurity(RtpyBase):
    """SECURITY methods category."""

    def get_users(self, **kwargs):
        """
        Get the users list.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Users"
        return self._request("GET", "security/users", api_method, kwargs)

    def get_user_details(self, username, **kwargs):
        """
        Get the details of an Artifactory user.

        Parameters
        ---------
        username: str
            Name of the user
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get User Details"
        target = self._prefix + "users/" + username
        return self._request("GET", target, api_method, kwargs)

    def get_user_encrypted_password(self, **kwargs):
        """
        Get the encrypted password of the authenticated requestor.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get User Encrypted Password"
        target = self._prefix + "encryptedPassword"
        return self._request("GET", target, api_method, kwargs)

    def create_or_replace_user(self, params, **kwargs):
        """
        Create a new user in Artifactory or replaces an existing user.

        Parameters
        ---------
        params: dict
            Settings of the user
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create or Replace User"
        username = params["name"]
        target = self._prefix + "users/" + username
        params["Content-Type"] = "application/json"
        return self._request("PUT", target, api_method, kwargs, params=params)

    def update_user(self, params, **kwargs):
        """
        Update an exiting user in Artifactory with the provided user details.

        Parameters
        ---------
        params: dict
            Settings of the user
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Update User"
        username = params["name"]
        target = self._prefix + "users/" + username
        params["Content-Type"] = "application/json"
        return self._request("POST", target, api_method, kwargs, params=params)

    def delete_user(self, username, **kwargs):
        """
        Remove an Artifactory user.

        Parameters
        ---------
        username: str
            Name of the user
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete User"
        target = self._prefix + "users/" + username
        return self._request("DELETE", target, api_method, kwargs)

    # Unsupported Methods
    # def expire_password_for_a_single_user()
    # def expire_password_for_multiple_users()
    # def expire_password_for_all_users()
    # def unexpire_password_for_a_single_user()
    # def change_password()
    # def get_password_expiration_policy()
    # def set_password_expiration_policy()
    # def configure_user_lock_policy()
    # def retrieve_user_lock_policy()

    def get_locked_out_users(self, **kwargs):
        """
        Get a list of the locked out users.

        If locking out users is enabled, lists all users
        that were locked out due to recurrent incorrect login attempts.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Locked Out Users"
        target = self._prefix + "lockedUsers"
        return self._request("GET", target, api_method, kwargs)

    def unlock_locked_out_user(self, username, **kwargs):
        """
        Unlock a single user that was locked out.

        Parameters
        ---------
        username: str
            Name of the user
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Unlock Locked Out User"
        target = self._prefix + "unlockUsers/" + username
        return self._request("POST", target, api_method, kwargs)

    def unlock_locked_out_users(self, user_list, **kwargs):
        """
        Unlock a list of users that were locked out.

        Parameters
        ---------
        user_list: list
            List of str representing usernames
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Unlock Locked Out Users"
        target = self._prefix + "unlockUsers"

        counter = 0
        data = "[ "
        for user in user_list:
            if counter == len(user_list) - 1:
                data = data + '"' + user + '"'
            else:
                data = data + '"' + user + '", '
            counter = counter + 1

        data = data + " ]"
        params = {}
        params["Content-Type"] = "application/json"
        return self._request(
            "POST", target, api_method, kwargs, data=data, params=params
        )

    def unlock_all_locked_out_users(self, **kwargs):
        """
        Unlock all users that were locked out.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Unlock All Locked Out Users"
        target = self._prefix + "unlockAllUsers"
        return self._request("POST", target, api_method, kwargs)

    def create_api_key(self, **kwargs):
        """
        Create an API key for the current user.

        Returns an error if API key already exists,
        use regenerate API key instead.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create API key"
        target = self._prefix + "apiKey"
        return self._request("POST", target, api_method, kwargs)

    def regenerate_api_key(self, **kwargs):
        """
        Regenerate an API key for the current user.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Regenerate API key"
        target = self._prefix + "apiKey"
        return self._request("PUT", target, api_method, kwargs)

    def get_api_key(self, **kwargs):
        """
        Get the current user's own API key.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get API key"
        target = self._prefix + "apiKey"
        return self._request("GET", target, api_method, kwargs)

    def revoke_api_key(self, **kwargs):
        """
        Revoke the current user's API key.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Revoke API key"
        target = self._prefix + "apiKey"
        return self._request("DELETE", target, api_method, kwargs)

    def revoke_user_api_key(self, username, **kwargs):
        """
        Revoke the API key of another user.

        Parameters
        ---------
        username: str
            Name of the user
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Revoke User API key"
        target = self._prefix + "apiKey/" + username
        return self._request("DELETE", target, api_method, kwargs)

    def get_groups(self, **kwargs):
        """
        Get the groups list.

        Parameters
        ---------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Groups"
        target = self._prefix + "groups"
        return self._request("GET", target, api_method, kwargs)

    def get_group_details(self, group_name, **kwargs):
        """
        Get the details of an Artifactory Group.

        Parameters
        ---------
        group_name: str
            Name of the group
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Group Details"
        target = self._prefix + "groups" + "/" + group_name
        return self._request("GET", target, api_method, kwargs)

    def create_or_replace_group(self, params, **kwargs):
        """
        Create a new group in Artifactory or replace an existing group.

        Parameters
        ---------
        params: dict
            Settings of the group
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create or Replace Group"
        group_name = params["group_name"]
        target = self._prefix + "groups" + "/" + group_name
        return self._request("PUT", target, api_method, kwargs, params=params)

    def update_group(self, params, **kwargs):
        """
        Update an exiting group in Artifactory.

        Parameters
        ---------
        params: dict
            Settings of the group
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Update Group"
        group_name = params["group_name"]
        target = self._prefix + "groups" + "/" + group_name
        return self._request("POST", target, api_method, kwargs, params=params)

    def delete_group(self, group_name, **kwargs):
        """
        Remove an Artifactory group.

        Parameters
        ---------
        group_name: str
            Name of the group
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Group"
        target = self._prefix + "groups" + "/" + group_name
        return self._request("DELETE", target, api_method, kwargs)

    def get_permission_targets(self, **kwargs):
        """
        Get the permission targets list.

        Parameters
        ----------
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Permission Targets"
        target = self._prefix + "permissions"
        return self._request("GET", target, api_method, kwargs)

    def get_permission_target_details(self, permission_target_name, **kwargs):
        """
        Get the details of an Artifactory Permission Target.

        Parameters
        ----------
        permission_target_name: str
            Name of the permission target
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Get Permission Target Details"
        target = self._prefix + "permissions/" + permission_target_name
        return self._request("GET", target, api_method, kwargs)

    def create_or_replace_permission_target(self, params, **kwargs):
        """
        Create a new permission target in Artifactory.

        (or replace an existing permission target).

        Parameters
        ----------
        params: dict
            Settings of the permission target
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Create or Replace Permission Target"
        permission_target_name = params["name"]
        target = self._prefix + "permissions/" + permission_target_name
        return self._request("PUT", target, api_method, kwargs, params=params)

    def delete_permission_target(self, permission_target_name, **kwargs):
        """
        Delete an Artifactory permission target.

        Parameters
        ----------
        permission_target_name: str
            Name of the permission target
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Delete Permission Target"
        target = self._prefix + "permissions/" + permission_target_name
        return self._request("DELETE", target, api_method, kwargs)

    def effective_item_permissions(self, repo_key, item_path, **kwargs):
        """
        Return a list of effective permissions.

        (for the specified item(file or folder).

        Parameters
        ----------
        repo_key: str
            Key of the repository
        item_path: str
            The path of the item in the repository
        **kwargs
            Keyword arguments

        """
        api_method = self._category + "Effective item permissions"
        target = "storage/" + repo_key + "/" + item_path + "?permissions"
        return self._request("GET", target, api_method, kwargs)

    # Unsupported Methods
    # def security_configuration()
    # def activate_artifactory_key_encryption()
    # def deactivate_artifactory_key_encryption()
    # def get_gpg_public_key()
    # def set_gpg_public_key()
    # def set_gpg_private_key()
    # def set_gpg_pass_phrase()
    # def create_token()
    # def refresh_token()
    # def revoke_token()
    # def get_service_id()
    # def get_certificates()
    # def get_certificate()
    # def add_certificate()
    # def delete_certificate()
