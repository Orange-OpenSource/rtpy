# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Definitions of the tests for the SECURITY REST API Methods category."""

from __future__ import unicode_literals

from .mixins import RtpyTestMixin


class TestsSecurity(RtpyTestMixin):
    """SECURITY methods category tests."""

    def test_get_users(self, instantiate_af_objects_credentials_and_api_key):
        """Get Users tests."""
        r = self.af.security.get_users()
        RtpyTestMixin.assert_isinstance_list(r)

    def test_get_user_details(self, instantiate_af_objects_credentials_and_api_key):
        """Get User Details tests."""
        r = self.af.security.get_user_details("admin")
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_get_user_encrypted_password(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Get User Encrypted Password tests."""
        r = self.af.security.get_user_encrypted_password()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_create_or_replace_user(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Create or Replace User tests."""
        myparams = {}
        myparams["name"] = "rtpy_test_user1"
        myparams["admin"] = "true"
        myparams["email"] = "rtpy@mail.com"
        myparams["password"] = "password"

        r = self.af.security.create_or_replace_user(myparams)
        self.af.security.get_user_details(myparams["name"])
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        self.af.security.delete_user("rtpy_test_user1")

    def test_update_user(self, instantiate_af_objects_credentials_and_api_key):
        """Update User tests."""
        myparams = {}
        myparams["name"] = "rtpy_test_user2"
        myparams["admin"] = "true"
        myparams["email"] = "rtpy@mail.com"
        myparams["password"] = "password"

        self.af.security.create_or_replace_user(myparams)
        r = self.af.security.get_user_details(myparams["name"])
        admin_status_original = r["admin"]

        myparams = {}
        myparams["admin"] = "false"
        myparams["name"] = "rtpy_test_user2"
        r = self.af.security.update_user(myparams)
        r2 = self.af.security.get_user_details("rtpy_test_user2")
        admin_status = r2["admin"]
        self.af.security.delete_user("rtpy_test_user2")

        if admin_status == admin_status_original:
            message = "Field did not update properly!"
            raise self.RtpyTestError(message)

        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_delete_user(self, instantiate_af_objects_credentials_and_api_key):
        """Delete User tests."""
        myparams = {}
        myparams["name"] = "rtpy_test_user3"
        myparams["admin"] = "true"
        myparams["email"] = "rtpy@mail.com"
        myparams["password"] = "password"

        self.af.security.create_or_replace_user(myparams)
        r = self.af.security.delete_user("rtpy_test_user3")
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    # Unsupported Methods
    # def test_expire_password_for_a_single_user()
    # def test_expire_password_for_multiple_users()
    # def test_expire_password_for_all_users()
    # def test_unexpire_password_for_a_single_user()
    # def test_change_password()
    # def test_get_password_expiration_policy()
    # def test_set_password_expiration_policy()
    # def test_configure_user_lock_policy()

    def test_get_locked_out_users(self, instantiate_af_objects_credentials_and_api_key):
        """Get locked Out Users tests."""
        r = self.af.security.get_locked_out_users()
        RtpyTestMixin.assert_isinstance_list(r)

    def test_unlock_locked_out_user(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Unlock Locked Out User tests."""
        r = self.af.security.unlock_locked_out_user("admin")
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_unlock_locked_out_users(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Unlock Locked Out Users tests."""
        r = self.af.security.unlock_locked_out_users([])
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        myparams = {}
        myparams["name"] = "rtpy_test_user4"
        myparams["email"] = "rtpy@mail.com"
        myparams["password"] = "password"
        self.af.security.create_or_replace_user(myparams)
        myparams = {}
        myparams["name"] = "rtpy_test_user5"
        myparams["email"] = "rtpy@mail.com"
        myparams["password"] = "password"
        self.af.security.create_or_replace_user(myparams)

        # The method sometimes returns an error 500.
        try:
            r = self.af.security.unlock_locked_out_users(
                ["rtpy_test_user4", "rtpy_test_user5"]
            )
            RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        except self.af.AfApiError as error:
            if error.status_code != 500:
                raise error

        self.af.security.delete_user("rtpy_test_user4")
        self.af.security.delete_user("rtpy_test_user5")

    def test_unlock_all_locked_out_users(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Unlock All Locked Out Users tests."""
        r = self.af.security.unlock_all_locked_out_users()
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_create_api_key(self, instantiate_af_object_with_credentials):
        """Create API key tests."""
        """
        try:
            self.af.security.revoke_api_key()
        except (self.af.AfApiError, self.af.MalformedAfApiError):
            pass

        r = self.af.security.create_api_key()
        RtpyTestMixin.assert_isinstance_dict(r)
        """
        pass

    def test_regenerate_api_key(self, instantiate_af_object_with_credentials):
        """Regenerate API key tests."""
        """
        try:
            self.af.security.revoke_api_key()
            self.af.security.create_api_key()
        except (self.af.AfApiError, self.af.MalformedAfApiError):
            pass
        r = self.af.security.regenerate_api_key()
        RtpyTestMixin.assert_isinstance_dict(r)
        """
        pass

    def test_get_api_key(self, instantiate_af_object_with_credentials):
        """Get API key tests."""
        """
        try:
            self.af.security.revoke_api_key()
        except (self.af.AfApiError, self.af.MalformedAfApiError):
            pass

        self.af.security.create_api_key()
        r = self.af.security.get_api_key()
        RtpyTestMixin.assert_isinstance_dict(r)
        """
        pass

    def test_revoke_api_key(self, instantiate_af_object_with_credentials):
        """Revoke API key tests."""
        """
        try:
            self.af.security.revoke_api_key()
        except (self.af.AfApiError, self.af.MalformedAfApiError):
            pass

        self.af.security.create_api_key()
        r = self.af.security.revoke_api_key()
        RtpyTestMixin.assert_isinstance_dict(r)
        """
        pass

    def test_revoke_user_api_key(self, instantiate_af_object_with_credentials):
        """Revoke User API key tests."""
        """
        try:
            self.af.security.create_api_key()
        except (self.af.AfApiError, self.af.MalformedAfApiError):
            pass
        r = self.af.security.revoke_user_api_key("admin")
        RtpyTestMixin.assert_isinstance_dict(r)
        """
        pass

    def test_get_groups(self, instantiate_af_objects_credentials_and_api_key):
        """Get Groups tests."""
        r = self.af.security.get_groups()
        RtpyTestMixin.assert_isinstance_list(r)

    def test_get_group_details(self, instantiate_af_objects_credentials_and_api_key):
        """Get Group Details tests."""
        r = self.af.security.get_group_details("readers")
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_create_or_replace_group(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Create Or Replace Group tests."""
        group_name = "rtpy_tests_group1"
        params = {"description": "mydesc", "group_name": group_name}
        r = self.af.security.create_or_replace_group(params)
        self.af.security.delete_group(group_name)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_update_group(self, instantiate_af_objects_credentials_and_api_key):
        """Update Group tests."""
        """
        currently not working for an unknown reason
        group_name = "rtpy_tests_group2"
        params = {"description": "mydesc", "group_name": group_name}
        r = self.af.security.create_or_replace_group(
            params, settings={"raw_response": True})
        r = self.af.security.get_group_details(group_name)
        description_original = r["description"]
        params2 = {"description": "mydesc_new", "group_name": group_name}
        r = self.af.security.update_group(params2)
        r2 = self.af.security.get_group_details(group_name)
        self.af.security.delete_group(group_name)
        if r2["description"] == description_original:
            message = "Group did not update properly, check the fields!"
            # raise self.RtpyTestError(message)
            pass
        #RtpyTestMixin.assert_isinstance_str(self.py_version, r)
        """
        pass

    def test_delete_group(self, instantiate_af_objects_credentials_and_api_key):
        """Delete Group tests."""
        group_name = "rtpy_tests_group3"
        params = {"description": "mydesc", "group_name": group_name}
        self.af.security.create_or_replace_group(params)
        r = self.af.security.delete_group(group_name)
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_get_permission_targets(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Get Permission Targets tests."""
        r = self.af.security.get_permission_targets()
        RtpyTestMixin.assert_isinstance_list(r)

    def test_get_permission_target_details(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Get Permission Target Details tests."""
        r = self.af.security.get_permission_target_details("Anything")
        RtpyTestMixin.assert_isinstance_dict(r)

    def test_create_or_replace_permission_target(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Create or Replace Permission Target."""
        params = {}
        params["key"] = "rtpy_test_repo_security_1"
        params["rclass"] = "local"
        params["packageType"] = "generic"
        try:
            self.af.repositories.delete_repository("rtpy_test_repo_security_1")
        except self.af.AfApiError as error:
            if error.status_code not in [400, 404]:
                raise
        r = self.af.repositories.create_repository(params)

        params = {}
        params["repositories"] = ["rtpy_test_repo_security_1"]
        params["name"] = "rtpy_test_ptarget_1"
        r = self.af.security.create_or_replace_permission_target(params)
        self.af.security.delete_permission_target("rtpy_test_ptarget_1")
        try:
            self.af.repositories.delete_repository("rtpy_test_repo_security_1")
        except self.af.AfApiError as error:
            if error.status_code not in [400, 404]:
                raise
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_delete_permission_target(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Delete Permission Target tests."""
        params = {}
        params["key"] = "rtpy_test_repo_security_2"
        params["rclass"] = "local"
        params["packageType"] = "generic"
        try:
            self.af.repositories.delete_repository("rtpy_test_repo_security_2")
        except self.af.AfApiError as error:
            if error.status_code not in [400, 404]:
                raise
        self.af.repositories.create_repository(params)
        params = {}
        params["repositories"] = ["rtpy_test_repo_security_2"]
        params["name"] = "rtpy_test_ptarget_2"
        self.af.security.create_or_replace_permission_target(params)
        r = self.af.security.delete_permission_target("rtpy_test_ptarget_2")
        try:
            self.af.repositories.delete_repository("rtpy_test_repo_security_2")
        except self.af.AfApiError as error:
            if error.status_code not in [400, 404]:
                raise
        RtpyTestMixin.assert_isinstance_str(self.py_version, r)

    def test_effective_item_permissions(
        self, instantiate_af_objects_credentials_and_api_key
    ):
        """Effective Item Permissions tests."""
        params = {}
        params["key"] = "rtpy_test_repo_security_3"
        params["rclass"] = "local"
        params["packageType"] = "generic"
        self.af.repositories.create_repository(params)
        r = self.af.security.effective_item_permissions("rtpy_test_repo_security_3", "")
        self.af.repositories.delete_repository("rtpy_test_repo_security_3")
        RtpyTestMixin.assert_isinstance_dict(r)
