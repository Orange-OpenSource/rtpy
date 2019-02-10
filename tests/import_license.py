# coding: utf-8

# Copyright (C) 2018 Orange
#
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the 'LICENSE.md' file
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

"""Use an environment variable to create a JSON file for the Artifactory license."""

import os
import json

key = os.environ["AF_TEST_LICENSE"]

with open("tests/license.json", "w") as jsonfile:
    licensedata = {"licenseKey": key}
    jsonfile.write(json.dumps(licensedata))
