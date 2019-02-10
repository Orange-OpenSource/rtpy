# User Guide

## Table of contents
- **[Getting Started](#getting-started)**

- **[Responses](#responses)**

- **[Tips](#tips)**

- **[Examples](#examples)**
    
<br/>

# Getting Started
- [Instantiate the Rtpy class](#instantiate-the-rtpy-class)
  - [Mandatory keys](#mandatory-keys)
  - [Optional keys](#optional-keys)
<br>

## Instantiate the Rtpy class
A rtpy.Rtpy object is used to make all the API calls.
<br/>
To be instantiated the Rtpy class only takes a **python dictionary as first positional argument**.
This dictionary contains the user's settings such as API key and Artifactory instance URL.
<br/>
### Mandatory keys
- **"af_url"** : URL of the AF instance (starting with http(s)://)
- **"api_key"** or **"username"** and **"password"** : API key or username and password for the user in the Artifactory instance

```python
import rtpy

settings = {}
settings["af_url"] = "http://..."
settings["api_key"] = "123QWA..." 
# settings["username"] = "my_username"
# settings["password"] = "my_password"

af = rtpy.Rtpy(settings)
```
### Optional keys
- **"verbose_level"** : 0/1 
  - The desired verbose level, 0 for nothing, 1 to print performed operations
  - 0 if not not provided
- **"raw_response"** : False/True
  - True will return a [requests.Response object](http://docs.python-requests.org/en/master/api/#requests.Response) and the errors will not be automatically raised
  - False will return a python object
  - False if not provided
- **"session"**: [requests.Session](http://docs.python-requests.org/en/master/api/#requests.Session) object
    - rtpy uses a [requests.Session](http://docs.python-requests.org/en/master/api/#requests.Session) object to make calls to the Artifactory API endpoint. A custom can be provided session object when creating a Rtpy object for advanced HTTP configurations, proxies, SSL...
    - request.Session() (default attributes) if not provided

```python
import requests
import rtpy

settings["verbose_level"] = 0/1
settings["raw_response"] = False/True

# SSL : custom CA bundle example
session = requests.Session()
session.verify = "path/to/ca_bundle.crt"
settings['session'] = session

af = rtpy.Rtpy(settings)
```
<br/><br/>
# Responses

The response when using methods can be a :
- When "raw_response" is **False** (default):
  - python dictionary or list (a converted json output) (most cases)
  - unicode string ([(requests.Response)](http://docs.python-requests.org/en/master/api/#requests.Response).text)  (if the json content can't be decoded/is missing/isn't expected)

- When "raw_response" is **True** :
  - [requests.Response Object](http://docs.python-requests.org/en/master/api/#requests.Response) 

<br/><br/>
# Tips
- [Environment variables as settings](#environment-variables-as-settings)
- [Error handling](#error-handling)
- [Overriding settings](#overriding-settings)
- [Instantiate and check equality of multiple Rtpy objects](#instantiate-and-check-equality-of-multiple-rtpy-objects)
- [pretty-print](#pretty-print)
- [Json file to Python dictionary](#json-file-to-python-dictionary)

<br>

## Environment variables as settings
Use environement variables for the api_key and af_url in the settings dictionary
```python
settings = {}
settings["af_url"] = os.environ["ARTIFACTORY_URL"] # URL of the AF instance
settings["api_key"] = os.environ["ARTIFACTORY_API_KEY"] # User/Admin API key in the given AF instance

af = rtpy.Rtpy(settings)
```
<br/>

## Error handling
There are currently 4 errors :
 - [UserSettingsError](#usersettingserror)
 - [AfApiError](#afapierror)
 - [MalformedAfApiError](#malformedafapierror)
 - [RtpyError](#rtpyerror)

### UserSettingsError
Standalone error, when the instantiation of the Rtpy object fails due to incorrect settings
```python
try:
    af = rtpy.Rtpy(settings)
except rtpy.UserSettingsError:
    # Do stuff
```
<br/>
### AfApiError
When the status code is 4xx-5xx and the API sends a well formed JSON

The error has specific attributes
```python
try:
    r = af.category.method_xyz()

except af.AfApiError as error:

    # All the attributes of the error
    print(dir(error))

    # Rtpy attributes for the error
    print(error.api_method)
    print(error.url)
    print(error.verb)
    print(error.status_code)
    print(error.message)
    print(error.print_message)

    if error.status_code == 404:
        # Do stuff

    if error.status_code == 403:
        # Do stuff
```
<br/>
### MalformedAfApiError
When the status code is 4xx-5xx and the API sends a malformed JSON
```python
try:
    # The JSON is currently malformed when the API sends an error when using this method
    af.system_and_configuration.install_license(params)
except af.MalformedAfApiError:
   pass
```
<br/>
### RtpyError
When a method is called and parameters are missing or incorrect
```python
try:
    # Providing "" for artifact_path will raise the RtpyError
    af.artifacts_and_storage.retrieve_artifact("repo_key", "")
except af.RtpyError:
    pass
```
<br/>
## Overriding settings
All the settings can be overridden for a **single function call** (original settings are restored when the call is over) <br/>
This is useful for debugging (verbose level) or not raising errors (raw_response). It can also be used to provide different credentials

```python
r = af.category.method_xyz(settings={"raw_response" : True, "verbose_level" : 1})

r = af.category.method_xyz(settings={"verbose_level" : 1})

r = af.category.method_xyz(settings={"api_key" : "123ABC..."})

session = requests.Session()
session.verify = "path/to/ca_bundle.crt"
r = af.category.method_xyz(settings={"session" : session})

```
<br/>

## Instantiate and check equality of multiple Rtpy objects
This can be used to have different persistent settings and make different calls with different users

```python
import rtpy

af1 = rtpy.Rtpy({"af_url" : "https://...", "api_key" : "123QWA..."})
af2 = rtpy.Rtpy({"af_url" : "https://...", "api_key" : "456IOU..."})

# Usage of Rtpy's __repr__ and __eq__ special methods 
settings = {}
settings["af_url"] = "http://localhost:8081/artifactory"
settings["username"] = "admin"
settings["password"] = "password"

af1 = rtpy.Rtpy(settings)

print(af1)
# rtpy.Rtpy({'af_url': 'http://localhost:8081/artifactory', 'username': 'admin', 'password': 'password'})

af2 = rtpy.Rtpy(settings)
assert af1 == af2

af3 = eval(repr(af1))
af4 = eval(repr(af2))

assert af1 == af2 == af3 == af4
```
<br/>

## pretty-print
Use the pprint package to print the json responses in a more readable way

```python
r = af.category.method_xyz()
pprint.pprint(r)
```
<br/>
## Json file to Python dictionary
Convert a json file to a python dictionnary using the json_to_dict method
```python
my_dict = rtpy.json_to_dict(json_file_path)
```
<br/><br/>
# Examples
List of examples for **[supported methods](./SUPPORTED_METHODS.md)**.

- [ARITFACTS AND STORAGE](#artifacts-and-storage)
  - [Folder Info](#folder-info)
  - [File Info](#file-info)
  - [Get Storage Summary Info](#get-storage-summary-info)
  - [Item Last Modified](#item-last-modified)
  - [File Statistics](#file-statistics)
  - [Item Properties](#item-properties)
  - [Set Item Properties](#set-item-properties)
  - [Delete Item Properties](#delete-item-properties)
  - [Set Item SHA256 Checksum](#set-item-sha256-checksum)
  - [Retrieve Artifact](#retrieve-artifact)
  - [Retrieve Folder or Repository Archive](#retrieve-folder-or-repository-archive)
  - [Trace Artifact Retrieval](#trace-artifact-retrieval)
  - [Create Directory](#create-directory)
  - [Deploy Artifact](#deploy-artifact)
  - [Deploy Artifact by Checksum](#deploy-artifact-by-checksum)
  - [Delete Item](#delete-item)
  - [Copy Item](#copy-item)
  - [Move Item](#move-item)
  - [Artifact Sync Download](#artifact-sync-download)
  - [File List](#file-list)
  - [Get Background Tasks](#get-background-tasks)
  - [Empty Trash Can](#empty-trash-can)
  - [Delete Item From Trash Can](#delete-item-from-trash-can)
  - [Restore Item From Trash Can](#restore-item-from-trash-can)
  - [Optimize System Storage](#optimize-system-storage)

- [BUILDS](#builds)
  - [All Builds](#all-builds)

- [REPOSITORIES](#repositories)
  - [Get Repositories](#get-repositories)
  - [Repository Configuration](#repository-configuration)
  - [Create Repository](#create-repository)
  - [Update Repository Configuration](#update-repository-configuration)
  - [Delete Repository](#delete-repository)
  - [Calculate YUM Repository Metadata](#calculate-yum-repository-metadata)
  - [Calculate NuGet Repository Metadata](#calculate-nuget-repository-metadata)
  - [Calculate Npm Repository Metadata](#calculate-npm-repository-metadata)
  - [Calculate Maven Index](#calculate-maven-index)
  - [Calculate Maven Metadata](#calculate-maven-metadata)
  - [Calculate Debian Repository Metadata](#calculate-debian-repository-metadata)
  - [Calculate Opkg Repository Metadata](#calculate-opkg-repository-metadata)
  - [Calculate Bower Index](#calculate-bower-index)
  - [Calculate Helm Chart Index](#calculate-helm-chart-index)

- [SEARCHES](#searches)
  - [Artifactory Query Language](#artifactory-query-language)
  - [List Docker Repositories](#list-docker-repositories)
  - [List Docker Tags](#list-docker-tags)

- [SECURITY](#security)
  - [Get Users](#get-users)
  - [Get User Details](#get-user-details)
  - [Get User Encrypted Password](#get-user-encrypted-password)
  - [Create or Replace User](#create-or-replace-user)
  - [Update User](#update-user)
  - [Delete User](#delete-user)
  - [Get Locked Out Users](#get-locked-out-users)
  - [Unlock Locked Out User](#unlock-locked-out-user)
  - [Unlock Locked Out Users](#unlock-locked-out-users)
  - [Unlock All Locked Out Users](#unlock-all-locked-out-users)
  - [Create API Key](#create-api-key)
  - [Regenerate API Key](#regenerate-api-key)
  - [Get API Key](#get-api-key)
  - [Revoke API Key](#revoke-api-key)
  - [Revoke User API Key](#revoke-user-api-key)
  - [Get Groups](#get-groups)
  - [Get Group Details](#get-group-details)
  - [Create or Replace Group](#create-or-replace-group)
  - [Update Group](#update-group)
  - [Delete Group](#delete-group)
  - [Get Permission Targets](#get-permission-targets)
  - [Get Permission Target Details](#get-permission-target-details)
  - [Create or Replace Permission Target](#create-or-replace-permission-target)
  - [Delete Permission Target](#delete-permission-target)
  - [Effective Item Permissions](#effective-item-permissions)

- [SUPPORT](#support)
  - [Create Bundle](#create-bundle)
  - [List Bundles](#list-bundles)
  - [Get Bundle](#get-bundle)
  - [Delete Bundle](#delete-bundle)

- [SYSTEM AND CONFIGURATION](#system-and-configuration)
  - [System Info](#system-info)
  - [System Health Ping](#system-health-ping)
  - [General Configuration](#general-configuration)
  - [General Configuration](#general-configuration)
  - [Save General Configuration](#save-general-configuration)
  - [License Information](#license-information)
  - [Install License](#install-license)
  - [Version and Addons information](#version-and-addons-informations)
  - [Get Reverse Proxy Configuration](#get-reverse-proxy-configuration)
  - [Get Reverse Proxy Snippet](#get-reverse-proxy-snippet)

<br>
## ARTIFACTS AND STORAGE

### Folder Info
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FolderInfo](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FolderInfo)
```python
r = af.artifacts_and_storage.folder_info(repo_key, folder_path)
# repo_key is the name of the repository in Artifactory
# folder_path is the path of the folder inside the repo
# To get information on the root repo, use "", as argument for folder_path
```
<br/>
### File Info
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileInfo](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileInfo)
```python
r = af.artifacts_and_storage.file_info(repo_key, file_path)
# repo_key is the name of the repository in Artifactory
# file path is the path of the file inside the repo
```
<br/>
### Get Storage Summary Info
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetStorageSummaryInfo](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetStorageSummaryInfo)
```python
r = af.artifacts_and_storage.get_storage_summary_info()
```
<br/>
### Item Last Modified
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemLastModified](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemLastModified)
```python
r = af.artifacts_and_storage.item_last_modified(repo_key, item_path)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo
```
<br/>
### File Statistics
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileStatistics](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileStatistics)
```python
r = af.artifacts_and_storage.file_statistics(repo_key, item_path)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo
```
<br/>
### Item Properties
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemProperties](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemProperties)
```python
r = af.artifacts_and_storage.item_properties(repo_key, item_path)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo

# Standard example
r = af.artifacts_and_storage.item_properties("my_repo", "folder/artifact.png")

# Retrieve specific propertie(s)
r = af.artifacts_and_storage.item_properties(repo_key, item_path, properties="version")
r = af.artifacts_and_storage.item_properties(repo_key, item_path, properties="version, owner")
```
<br/>
### Set Item Properties
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemProperties](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemProperties)
```python
r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, properties)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo

# Single property
r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version=1.0")

# Set multiple properties
r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version=1.0;author=smith")
```
<br/>
### Delete Item Properties
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemProperties](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemProperties)
```python
r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, properties)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo

# Delete a single property
r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version")

# Delete multiple properties
r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version,author")
```
<br/>
### Set Item SHA256 Checksum
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemSHA256Checksum](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemSHA256Checksum)
```python
params = {"repo_key": my_repo_key, "path": mypath}
# repo_key is the name of the repository in Artifactory
# artifact_path is the path of the artifact inside the repo
r = af.artifacts_and_storage.set_item_sha256_checksum(params)
```
<br/>
### Retrieve Artifact
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveArtifact](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveArtifact)
```python
r = af.artifacts_and_storage.retrieve_artifact(repo_key, artifact_path)
# repo_key is the name of the repository in Artifactory
# artifact_path is the path of the artifact inside the repo

# Save the file locally
with open("myartifact.png", "wb") as artifact:
    artifact.write(r.content)
```
<br/>
### Retrieve Folder or Repository Archive
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveFolderorRepositoryArchive](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveFolderorRepositoryArchive)
```python
r = af.artifacts_and_storage.retrieve_folder_or_repository_archive(repo_key, path, archive_type)
# repo_key is the name of the repository in Artifactory
# path is the path of the folder inside the repo
# archive_type can be "zip", "tar", "tar.gz", "tgz"

# Checksums can be included
r = af.artifacts_and_storage.retrieve_folder_or_repository_archive(repo_key, path, archive_type, include_checksums=True)

# Save the archive locally
with open("myarchive.archive_type", "wb") as archive:
    archive.write(r.content)
```
<br/>
### Trace Artifact Retrieval
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-TraceArtifactRetrieval](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-TraceArtifactRetrieval)
```python
r = af.artifacts_and_storage.trace_artifact_retrieval(repo_key, item_path)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo

# with this method the response is a Python requests response object 
# use r.text

print(r.text)
```
<br/>
### Create Directory
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateDirectory](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateDirectory)
```python
r = af.artifacts_and_storage.create_directory(repo_key, directory_path)
# repo_key is the name of the repository in Artifactory
# directory_path is the path of the directory inside the repo

# Known issue : when trying to create a directory that already exists, 
# response will not say already exist and nothing will happen.
```
<br/>
### Deploy Artifact
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifact](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifact)
```python
r = af.artifacts_and_storage.deploy_artifact(repo_key, local_artifact_path, target_artifact_path)
# repo_key is the name of the repository in Artifactory
# target_artifact_path is the path of the artifact inside the repo
# local_artifact_path is the path of the artifact on the local machine

# Standard example
r = af.artifacts_and_storage.deploy_artifact("myrepo", "myartifact_on_my_machine.png", "directory/my_remote_artifact.png")

# It is possible to attach properties as part of deploying an artifact using 
# Artifactory's Matrix Parameters : 
# https://www.jfrog.com/confluence/display/RTF4X/Using+Properties+in+Deployment+and+Resolution

# Single property
r = af.artifacts_and_storage.deploy_artifact("myrepo", "myartifact_on_my_machine", "myartifact;prop1=value")

# Multiple properties
r = af.artifacts_and_storage.deploy_artifact("myrepo", "myartifact_on_my_machine", "myartifact;prop1=value;prop2=value2")
```
<br/>
### Deploy Artifact by Checksum
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifactbyChecksum](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifactbyChecksum)
```python
r = af.artifacts_and_storage.deploy_artifact_by_checksum(repo_key, target_artifact_path, sha_type, sha_value):
# repo_key is the name of the repository in Artifactory
# target_artifact_path is the path of the artifact inside the repo
# sha_type is "sha1" or "sha256"
# sha_value is the value of the sha (string)

# Standard example
sha_type = "sha1"
sha_value = "e1a13e64b0414015d43dd80eed7876d7cee5e50e"

r = af.artifacts_and_storage.deploy_artifact_by_checksum("my_repo", "my_remote_artifact", sha_type, sha_value)


# It is possible to attach properties as part of deploying an artifact using 
# Artifactory's Matrix Parameters : 
# https://www.jfrog.com/confluence/display/RTF4X/Using+Properties+in+Deployment+and+Resolution

# Single property
r = af.artifacts_and_storage.deploy_artifact_by_checksum("myrepo", "myartifact;prop1=value", sha_type, sha_value)

# Multiple properties
r = af.artifacts_and_storage.deploy_artifact_by_checksum("myrepo", "myartifact;prop1=value;prop2=value2", sha_type, sha_value)
```
<br/>
### Delete Item
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItem](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItem)
```python
r = af.artifacts_and_storage.delete_item(repo_key, path_to_item)
# repo_key is the name of the repository in Artifactory
# path_to_item is the path to the item (repo or artifact) in the repo
# use "" as argument for path_to_item to delete all the content of a repository
```
<br/>
### Copy Item
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CopyItem](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CopyItem)
```python
r = af.artifacts_and_storage.copy_item(src_repo_key, src_item_path, target_repo_key, target_item_path)
# src_repo_key is the name of the repository in Artifactory
# src_item_path is the path to the item (repo or artifact) in the repo
# target_repo_key is the name of the target repository in Artifactory
# target_item_path is the path of the item in the target repository

# Additionnal options from the documentation can be supplied as a string
r = af.artifacts_and_storage.copy_item(src_repo_key, src_item_path, target_repo_key, target_item_path, options=string_of_options)
# Such as "[&dry=1][&suppressLayouts=0/1(default)][&failFast=0/1]"
```
<br/>
### Move Item
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-MoveItem](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-MoveItem)
```python
r = af.artifacts_and_storage.move_item(src_repo_key, src_item_path, target_repo_key, target_item_path)
# src_repo_key is the name of the repository in Artifactory
# src_item_path is the path to the item (repo or artifact) in the repo
# target_repo_key is the name of the target repository in Artifactory
# target_item_path is the path of the item in the target repository

# Additionnal options from the documentation can be supplied as a string
r = af.artifacts_and_storage.move_item(src_repo_key, src_item_path, target_repo_key, target_item_path, options=string_of_options)
# Such as [&dry=1][&suppressLayouts=0/1(default)][&failFast=0/1]
```
<br/>
### Artifact Sync Download
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactSyncDownload](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactSyncDownload)
```python
r = af.artifacts_and_storage.artifact_sync_download(repo_key, artifact_path)
# repo_key is the name of the repository in Artifactory
# artifact_path is the path of the artifact inside the repo

# Additionnal options from the documentation can be supplied as a string
r = af.artifacts_and_storage.artifact_sync_download(repo_key, artifact_path, options=string_of_options)
# Such as [?content=none/progress][&mark=numOfBytesToPrintANewProgressMark]
# If no content parameter is specified the file content is downloaded to the client.
```
<br/>
### File List
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileList](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileList)
```python
r = af.artifacts_and_storage.file_list(repo_key, folder_path)
# repo_key is the name of the repository in Artifactory
# folder_path is the path of the folder inside the repo
# To get information on the root repo, use "", as argument for folder_path

# Additionnal options from the documentation can be supplied as a string
r = af.artifacts_and_storage.file_list(repo_key, folder_path, options=string_of_options)
# Such as [&depth=n][&listFolders=0/1][&mdTimestamps=0/1][&includeRootPath=0/1]
```
<br/>
### Get Background Tasks
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBackgroundTasks](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBackgroundTasks)
```python
r = af.artifacts_and_storage.get_background_tasks()
```
<br/>
### Empty Trash Can
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EmptyTrashCan](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EmptyTrashCan)
```python
r = af.artifacts_and_storage.empty_trash_can()
```
<br/>
### Delete Item From Trash Can
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemFromTrashCan](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemFromTrashCan)
```python
r = af.artifacts_and_storage.delete_item_from_trash_can(path_in_trashcan)
# path_in_trashcan is the path of the item inside the trashcan, typically : repo_name/folder/file
```
<br/>
### Restore Item From Trash Can
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RestoreItemfromTrashCan](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RestoreItemfromTrashCan)
```python
r = af.artifacts_and_storage.restore_item_from_trash_can(path_in_trashcan, target_path)
# path_in_trashcan is the path of the item inside the trashcan, typically : repo_name/folder/file
# target_path is the path where the item will be restored, repo_name/folder/file
```
<br/>
### Optimize System Storage
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-OptimizeSystemStorage](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-OptimizeSystemStorage)
```python
r = af.artifacts_and_storage.optimize_system_storage()
```
<br/><br/>
## BUILDS

### All Builds

```python
r = af.builds.all_builds()
```
<br/><br/>
## REPOSITORIES

### Get Repositories
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetRepositories](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetRepositories)
```python
r = af.repositories.get_repositories()
```
<br/>
### Repository Configuration
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RepositoryConfiguration](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RepositoryConfiguration)
```python
r = af.repositories.repository_configuration(repo_key)
# repo_key is the name of the repository in Artifactory
```
<br/>
### Create Repository
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateRepository](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateRepository)
```python
params = {}
params["key"] = "my_repo_name"
params["rclass"] = "local"
params["packageType"] = "debian"
# for remote repos : params["url"] = "http://..."
# for virtual repos : params["repositories"] = ["repo1", "repo2"]
r = af.repositories.create_repository(params)
# params is a dictionary (some fields are mandatory) of the repository settings
# https://www.jfrog.com/confluence/display/RTF/Repository+Configuration+JSON#RepositoryConfigurationJSON-application/vnd.org.jfrog.artifactory.repositories.LocalRepositoryConfiguration+json
```
<br/>
### Update Repository Configuration
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateRepositoryConfiguration](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateRepositoryConfiguration)
```python
params = {}
params["key"] = "my_repo_name"
params["description"] = "new_description"
r = af.repositories.update_repository_configuration(params)
# params is a dictionary (some fields are mandatory) of the repository settings that will be updated
```
<br/>
### Delete Repository
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteRepository](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteRepository)
```python
r = af.repositories.delete_repository(repo_key)
# repo_key is the name of the repository in Artifactory
```
<br/>
### Calculate YUM Repository Metadata
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateYUMRepositoryMetadata](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateYUMRepositoryMetadata)
```python
r = af.repositories.calculate_yum_repository_metadata(repo_key)
# repo_key is the name of the repository in Artifactory

# Additionnal options from the documentation can be supplied as a string
r = af.calculate_yum_repository_metadata(repo_key, options=string_of_options)
# Such as [?path={path to repodata dir][&async=0/1]

# a GPG passphrase can be supplied
gpg_passphrase = "abc"
r = af.calculate_yum_repository_metadata(repo_key, x_gpg_passphrase=gpg_passphrase)
```
<br/>
### Calculate NuGet Repository Metadata
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNuGetRepositoryMetadata](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNuGetRepositoryMetadata)
```python
r = af.repositories.calculate_nuget_repository_metadata(repo_key)
# repo_key is the name of the repository in Artifactory
```
<br/>
### Calculate Npm Repository Metadata
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNpmRepositoryMetadata](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNpmRepositoryMetadata)
```python
r = af.repositories.calculate_npm_repository_metadata(repo_key)
# repo_key is the name of the repository in Artifactory
```
<br/>
### Calculate Maven Index
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenIndex](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenIndex)
```python
r = af.repositories.calculate_maven_index(options_string)
# options_string is a string of the possible options
# Such as [?repos=x[,y]][&force=0/1]
```
<br/>
### Calculate Maven Metadata
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenMetadata](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenMetadata)
```python
r = af.repositories.calculate_maven_metadata(repo_key, folder_path)
# repo_key is the name of the repository in Artifactory
# folder_path is the path of the folder inside the repo

# Additionnal options from the documentation can be supplied as a string
r = af.repositories.calculate_maven_metadata(repo_key, folder_path, options=string_of_options)
# Such as {nonRecursive=true | false}
```
<br/>
### Calculate Debian Repository Metadata
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateDebianRepositoryMetadata](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateDebianRepositoryMetadata)
```python
r = af.repositories.calculate_debian_repository_metadata(repo_key)
# repo_key is the name of the repository in Artifactory

# Additionnal options from the documentation can be supplied as a string
r = af.calculate_debian_repository_metadata(repo_key, options=string_of_options)
# Such as [?async=0/1][?writeProps=0/1]

# a GPG passphrase can be supplied
gpg_passphrase = "abc"
r = af.calculate_debian_repository_metadata(repo_key, x_gpg_passphrase=gpg_passphrase)
```
<br/>
### Calculate Opkg Repository Metadata
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateOpkgRepositoryMetadata](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateOpkgRepositoryMetadata)
```python
r = af.repositories.calculate_opkg_repository_metadata(repo_key)
# repo_key is the name of the repository in Artifactory

# Additionnal options from the documentation can be supplied as a string
r = af.calculate_opkg_repository_metadata(repo_key, options=string_of_options)
# Such as [?async=0/1][?writeProps=0/1]

# a GPG passphrase can be supplied
gpg_passphrase = "abc"
r = af.calculate_opkg_repository_metadata(repo_key, x_gpg_passphrase=gpg_passphrase)
```
<br/>
### Calculate Bower Index
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateBowerIndex](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateBowerIndex)
```python
r = af.repositories.calculate_bower_index(repo_key)
# repo_key is the name of the repository in Artifactory
```
<br/>
### Calculate Helm Chart Index
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateHelmChartIndex](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateHelmChartIndex)
```python
r = af.repositories.calculate_helm_chart_index(repo_key)
# repo_key is the name of the repository in Artifactory
```
<br/><br/>
## SEARCHES

### Artifactory Query Language
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactoryQueryLanguage(AQL)](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactoryQueryLanguage(AQL))
```python
query = "aql_querry_string"
r = af.searches.artifactory_query_language(query)
# Example : query = "items.find({"repo":{"$eq":"my-repo"}})"
```
<br/>
### List Docker Repositories
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerRepositories](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerRepositories)
```python
r = af.searches.list_docker_repositories(repo_key)
# repo_key is the name of the repository in Artifactory

# Additionnal options from the documentation can be supplied as a string
r = af.searches.list_docker_repositories(repo_key, options=string_of_options)

```
<br/>
### List Docker Tags
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerTags](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerTags)
```python
r = af.searches.list_docker_tags(repo_key, image_path)
# repo_key is the name of the repository/registry in Artifactory
# image_path is the path of the docker image in the repository/registry

# Additionnal options from the documentation can be supplied as a string
r = af.searches.list_docker_repositories(repo_key, image_path, options=string_of_options)
# Such as ?n=<n from the request>&last=<last tag value from previous response>
```
<br/><br/>
## SECURITY

### Get Users
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUsers](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUsers)
```python
r = af.security.get_users()
```
<br/>
### Get User Details
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserDetails](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserDetails)
```python
r = af.security.get_user_details(username)
# username is the name of the user in Artifactory
```
<br/>
### Get User Encrypted Password
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserEncryptedPassword](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserEncryptedPassword)
```python
r = af.security.get_user_encrypted_password()
```
<br/>
### Create or Replace User
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceUser](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceUser)
```python
params = {}
params["name"] = "my_username"
params["admin"] = "false"
params["email"] = "myuser@orange.com"
params["password"] = "password"
r = af.security.create_or_replace_user(params)
# username is the name of the user in Artifactory 
# params ia a dictionary of desired fields to use to create the user and their value(s)
# https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON
```
<br/>
### Update User
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateUser](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateUser)
```python
params = {}
params["admin"] = "true"
r = af.security.update_user(params)
# username is the name of the user in Artifactory
# params ia a dictionary of desired fields to update and their value(s)
# https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON
```
<br/>
### Delete User
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteUser](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteUser)
```python
r = af.security.delete_user(username)
# username is the name of the user in Artifactory.
```
<br/>
### Get Locked Out Users
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetLockedOutUsers](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetLockedOutUsers)
```python
r = af.security.get_locked_out_users()
```
<br/>
### Unlock Locked Out User
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUser](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUser)
```python
r = af.security.unlock_locked_out_user(username)
# username is the name of the user in Artifactory.
```
<br/>
### Unlock Locked Out Users
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUsers](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUsers)
```python
r = af.security.unlock_locked_out_users(user_list)
# user_list is a python list of the users to unlock
```
<br/>
### Unlock All Locked Out Users
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockAllLockedOutUsers](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockAllLockedOutUsers)
```python
r = af.security.unlock_all_locked_out_users()
```
<br/>
### Create API Key
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateAPIKey](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateAPIKey)
```python
r = af.security.create_api_key()
```
<br/>
### Regenerate API Key
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RegenerateAPIKey](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RegenerateAPIKey)
```python
r = af.security.regenerate_api_key()
```
<br/>
### Get API Key
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetAPIKey](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetAPIKey)
```python
r = af.security.get_api_key()
```
<br/>
### Revoke API Key
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeAPIKey](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeAPIKey)
```python
r = af.security.revoke_api_key()
```
<br/>
### Revoke User API Key
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeUserAPIKey](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeUserAPIKey)
```python
r = af.security.revoke_user_api_key(username)
# username is the name of the user in Artifactory
```
<br/>
### Get Groups
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroups](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroups)
```python
r = af.security.get_groups()
```
<br/>
### Get Group Details
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroupDetails](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroupDetails)
```python
r = af.security.get_group_details(group_name)
# group_name is the name of the group in Artifactory.
```
<br/>
### Create or Replace Group
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceGroup](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceGroup)
```python
params = {}
params["group_name"] = "my_group"
r = af.security.create_or_replace_group(params)
# params is a python dictionnary which should be like :
# https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON
```
<br/>
### Update Group
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateGroup](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateGroup)
```python
params = {}
params["group_name"] = "my_group"
params["description"] = "my_description"
r = af.security.update_group(params)
# params is a python dictionnary which should be like :
# https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON
```
<br/>
### Delete Group
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteGroup](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteGroup)
```python
r = af.security.delete_group(group_name)
# group_name is the name of the group in Artifactory.
```
<br/>
### Get Permission Targets
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargets](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargets)
```python
r = af.security.get_permission_targets()
```
<br/>
### Get Permission Target Details
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargetDetails](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargetDetails)
```python
r = af.security.get_permission_target_details(permission_target_name)
# permission_target_name is the name of the permission in Artifactory.
```
<br/>
### Create or Replace Permission Target
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplacePermissionTarget](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplacePermissionTarget)
```python
params = {}
params["permission_target_name"] = "my_permission"
params["repositories"] = ["myrepo1", "myrepo2"]
r = af.security.create_or_replace_permission_target(params)
# https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON
```
<br/>
### Delete Permission Target
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeletePermissionTarget](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeletePermissionTarget)
```python
r = af.security.delete_permission_target(permission_target_name)
# permission_target_name is the name of the permission in Artifactory.
```
<br/>
### Effective Item Permissions
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EffectiveItemPermissions](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EffectiveItemPermissions)
```python
r = af.security.effective_item_permissions(repo_key, item_path)
# repo_key is the name of the repository in Artifactory
# item_path is the path of the item inside the repo
# To get information on the root repo, use "", as argument for item_path

```
<br/>
<br/><br/>
## SUPPORT

### Create Bundle
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateBundle](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateBundle)
```python
# params is a python dictionnary which should be like :
# https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateBundle
params = rtpy.json_to_dict("tests/templates/bundle_creation.json")
r = af.support.create_bundle(params)
```
<br/>
### List Bundles
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListBundles](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListBundles)
```python
r = af.support.list_bundles()
```
<br/>
### Get Bundle
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBundle](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBundle)
```python
# bundle_name is the name of the bundle
r = af.support.get_bundle(bundle_name)
with open(my_bundle_name, "wb") as bundle_file:
    bundle_file.write(r.content)
```
<br/>
### Delete Bundle
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteBundle](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteBundle)
```python
# bundle_name is the name of the bundle
r = af.support.delete_bundle(bundle_name)
```
<br/><br/>
## SYSTEM AND CONFIGURATION

### System Info
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemInfo](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemInfo)
```python
r = af.system_and_configuration.system_info()
```
<br/>
### System Health Ping
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemHealthPing](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemHealthPing)
```python
r = af.system_and_configuration.system_health_ping()
```
<br/>
### General Configuration
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GeneralConfiguration](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GeneralConfiguration)
```python
r = af.system_and_configuration.general_configuration()
```
<br/>
### Save General Configuration
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SaveGeneralConfiguration](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SaveGeneralConfiguration)
```python
r = af.system_and_configuration.save_general_configuration(xml_file_path)
# xml_file_path is the path on the local machine of the configuration file to be pushed
```
<br/>
### License Information
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-LicenseInformation](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-LicenseInformation)
```python
r = af.system_and_configuration.license_information()
```
<br/>
### Install License
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-InstallLicense](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-InstallLicense)
```python
params = {"licenseKey": "license_string"}
r = af.system_and_configuration.install_license(params)
```
<br/>
### Version and Addons Information
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-VersionandAdd-onsinformation](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-VersionandAdd-onsinformation)
```python
 r = af.system_and_configuration.version_and_addons_information()
```
<br/>
### Get Reverse Proxy Configuration
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration)
```python
r = af.system_and_configuration.get_reverse_proxy_configuration()
```
<br/>
### Get Reverse Proxy Configuration
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration)
```python
r = af.system_and_configuration.get_reverse_proxy_configuration()
```
<br/>
### Get Reverse Proxy Snippet
[https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxySnippet](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxySnippet)
```python
r = af.system_and_configuration.get_reverse_proxy_snippet()
```
<br/>