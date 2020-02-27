Examples
========

List of examples for `supported API methods <supported_api_methods.html>`_.

ARTIFACTS AND STORAGE
---------------------

Folder Info
^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FolderInfo <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FolderInfo>`_

.. code-block:: python

 r = af.artifacts_and_storage.folder_info(repo_key, folder_path)
 # repo_key is the name of the repository in Artifactory
 # folder_path is the path of the folder inside the repo
 # To get information on the root repo, use "", as argument for folder_path


File Info
^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileInfo <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileInfo>`_

.. code-block:: python

 r = af.artifacts_and_storage.file_info(repo_key, file_path)
 # repo_key is the name of the repository in Artifactory
 # file path is the path of the file inside the repo


Get Storage Summary Info
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetStorageSummaryInfo <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetStorageSummaryInfo>`_

.. code-block:: python

 r = af.artifacts_and_storage.get_storage_summary_info()


Item Last Modified
^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemLastModified <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemLastModified>`_

.. code-block:: python

 r = af.artifacts_and_storage.item_last_modified(repo_key, item_path)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo


File Statistics
^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileStatistics <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileStatistics>`_

.. code-block:: python

 r = af.artifacts_and_storage.file_statistics(repo_key, item_path)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo


Item Properties
^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemProperties <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ItemProperties>`_

.. code-block:: python

 r = af.artifacts_and_storage.item_properties(repo_key, item_path)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo

 # Standard example
 r = af.artifacts_and_storage.item_properties("my_repo", "folder/artifact.png")

 # Retrieve specific propertie(s)
 r = af.artifacts_and_storage.item_properties(repo_key, item_path, properties="version")
 r = af.artifacts_and_storage.item_properties(repo_key, item_path, properties="version, owner")


Set Item Properties
^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemProperties <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemProperties>`_

.. code-block:: python

 r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, properties)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo

 # Single property
 r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version=1.0")

 # Set multiple properties
 r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version=1.0;author=smith")

 # Additionnal options from the documentation can be supplied as a string
 r = af.artifacts_and_storage.set_item_properties(repo_key, item_path, "version=1.0;author=smith", options=string_of_options)
 # options_string is a string of the possible options
 # Such as [&recursive=1]


Delete Item Properties
^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemProperties <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemProperties>`_

.. code-block:: python

 r = af.artifacts_and_storage.delete_item_properties(repo_key, item_path, properties)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo

 # Delete a single property
 r = af.artifacts_and_storage.delete_item_properties(repo_key, item_path, "version")

 # Delete multiple properties
 r = af.artifacts_and_storage.delete_item_properties(repo_key, item_path, "version,author")


Set Item SHA256 Checksum
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemSHA256Checksum <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SetItemSHA256Checksum>`_

.. code-block:: python

 params = {"repo_key": my_repo_key, "path": mypath}
 # repo_key is the name of the repository in Artifactory
 # artifact_path is the path of the artifact inside the repo
 r = af.artifacts_and_storage.set_item_sha256_checksum(params)


Retrieve Artifact
^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveArtifact <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveArtifact>`_

.. code-block:: python

 r = af.artifacts_and_storage.retrieve_artifact(repo_key, artifact_path)
 # repo_key is the name of the repository in Artifactory
 # artifact_path is the path of the artifact inside the repo

 # Save the file locally
 with open("myartifact.png", "wb") as artifact:
     artifact.write(r.content)


Retrieve Folder or Repository Archive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveFolderorRepositoryArchive <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RetrieveFolderorRepositoryArchive>`_

.. code-block:: python

 r = af.artifacts_and_storage.retrieve_folder_or_repository_archive(repo_key, path, archive_type)
 # repo_key is the name of the repository in Artifactory
 # path is the path of the folder inside the repo
 # archive_type can be "zip", "tar", "tar.gz", "tgz"

 # Checksums can be included
 r = af.artifacts_and_storage.retrieve_folder_or_repository_archive(repo_key, path, archive_type, include_checksums=True)

 # Save the archive locally
 with open("myarchive.archive_type", "wb") as archive:
     archive.write(r.content)


Trace Artifact Retrieval
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-TraceArtifactRetrieval <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-TraceArtifactRetrieval>`_

.. code-block:: python

 r = af.artifacts_and_storage.trace_artifact_retrieval(repo_key, item_path)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo

 # with this method the response is a Python requests response object
 # use r.text

 print(r.text)


Create Directory
^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateDirectory <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateDirectory>`_

.. code-block:: python

 r = af.artifacts_and_storage.create_directory(repo_key, directory_path)
 # repo_key is the name of the repository in Artifactory
 # directory_path is the path of the directory inside the repo

 # Known issue : when trying to create a directory that already exists,
 # response will not say already exist and nothing will happen.


Deploy Artifact
^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifact <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifact>`_

.. code-block:: python

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


Deploy Artifact by Checksum
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifactbyChecksum <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeployArtifactbyChecksum>`_

.. code-block:: python

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


Delete Item
^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItem <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItem>`_

.. code-block:: python

 r = af.artifacts_and_storage.delete_item(repo_key, path_to_item)
 # repo_key is the name of the repository in Artifactory
 # path_to_item is the path to the item (repo or artifact) in the repo
 # use "" as argument for path_to_item to delete all the content of a repository


Copy Item
^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CopyItem <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CopyItem>`_

.. code-block:: python

 r = af.artifacts_and_storage.copy_item(src_repo_key, src_item_path, target_repo_key, target_item_path)
 # src_repo_key is the name of the repository in Artifactory
 # src_item_path is the path to the item (repo or artifact) in the repo
 # target_repo_key is the name of the target repository in Artifactory
 # target_item_path is the path of the item in the target repository

 # Additionnal options from the documentation can be supplied as a string
 r = af.artifacts_and_storage.copy_item(src_repo_key, src_item_path, target_repo_key, target_item_path, options=string_of_options)
 # Such as "[&dry=1][&suppressLayouts=0/1(default)][&failFast=0/1]"


Move Item
^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-MoveItem <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-MoveItem>`_

.. code-block:: python

 r = af.artifacts_and_storage.move_item(src_repo_key, src_item_path, target_repo_key, target_item_path)
 # src_repo_key is the name of the repository in Artifactory
 # src_item_path is the path to the item (repo or artifact) in the repo
 # target_repo_key is the name of the target repository in Artifactory
 # target_item_path is the path of the item in the target repository

 # Additionnal options from the documentation can be supplied as a string
 r = af.artifacts_and_storage.move_item(src_repo_key, src_item_path, target_repo_key, target_item_path, options=string_of_options)
 # Such as [&dry=1][&suppressLayouts=0/1(default)][&failFast=0/1]


Artifact Sync Download
^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactSyncDownload <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactSyncDownload>`_

.. code-block:: python

 r = af.artifacts_and_storage.artifact_sync_download(repo_key, artifact_path)
 # repo_key is the name of the repository in Artifactory
 # artifact_path is the path of the artifact inside the repo

 # Additionnal options from the documentation can be supplied as a string
 r = af.artifacts_and_storage.artifact_sync_download(repo_key, artifact_path, options=string_of_options)
 # Such as [?content=none/progress][&mark=numOfBytesToPrintANewProgressMark]
 # If no content parameter is specified the file content is downloaded to the client.


File List
^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileList <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-FileList>`_

.. code-block:: python

 r = af.artifacts_and_storage.file_list(repo_key, folder_path)
 # repo_key is the name of the repository in Artifactory
 # folder_path is the path of the folder inside the repo
 # To get information on the root repo, use "", as argument for folder_path

 # Additionnal options from the documentation can be supplied as a string
 r = af.artifacts_and_storage.file_list(repo_key, folder_path, options=string_of_options)
 # Such as [&depth=n][&listFolders=0/1][&mdTimestamps=0/1][&includeRootPath=0/1]


Get Background Tasks
^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBackgroundTasks <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBackgroundTasks>`_

.. code-block:: python

 r = af.artifacts_and_storage.get_background_tasks()


Empty Trash Can
^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EmptyTrashCan <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EmptyTrashCan>`_

.. code-block:: python

 r = af.artifacts_and_storage.empty_trash_can()


Delete Item From Trash Can
^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemFromTrashCan <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteItemFromTrashCan>`_

.. code-block:: python

 r = af.artifacts_and_storage.delete_item_from_trash_can(path_in_trashcan)
 # path_in_trashcan is the path of the item inside the trashcan, typically : repo_name/folder/file


Restore Item From Trash Can
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RestoreItemfromTrashCan <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RestoreItemfromTrashCan>`_

.. code-block:: python

 r = af.artifacts_and_storage.restore_item_from_trash_can(path_in_trashcan, target_path)
 # path_in_trashcan is the path of the item inside the trashcan, typically : repo_name/folder/file
 # target_path is the path where the item will be restored, repo_name/folder/file


Optimize System Storage
^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-OptimizeSystemStorage <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-OptimizeSystemStorage>`_

.. code-block:: python

 r = af.artifacts_and_storage.optimize_system_storage()


BUILDS
------

All Builds
^^^^^^^^^^

.. code-block:: python

 r = af.builds.all_builds()


REPOSITORIES
------------

Get Repositories
^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetRepositories <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetRepositories>`_

.. code-block:: python

 r = af.repositories.get_repositories()

 # Additionnal options from the documentation can be supplied as a string
 r = af.repositories.get_repositories(options=string_of_options)
 # Such as [?type=repositoryType (local|remote|virtual|distribution)]
 # [&packageType=maven|gradle|ivy|sbt|helm|cocoapods|opkg|rpm|nuget|cran|gems|npm|bower|debian|composer|pypi|docker|vagrant|gitlfs|go|yum|conan|chef|puppet|generic]

Repository Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RepositoryConfiguration <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RepositoryConfiguration>`_

.. code-block:: python

 r = af.repositories.repository_configuration(repo_key)
 # repo_key is the name of the repository in Artifactory


Create Repository
^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateRepository <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateRepository>`_

.. code-block:: python

 params = {}
 params["key"] = "my_repo_name"
 params["rclass"] = "local"
 params["packageType"] = "debian"
 # for remote repos : params["url"] = "http://..."
 # for virtual repos : params["repositories"] = ["repo1", "repo2"]
 r = af.repositories.create_repository(params)
 # params is a dictionary (some fields are mandatory) of the repository settings
 # https://www.jfrog.com/confluence/display/RTF/Repository+Configuration+JSON#RepositoryConfigurationJSON-application/vnd.org.jfrog.artifactory.repositories.LocalRepositoryConfiguration+json


Update Repository Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateRepositoryConfiguration <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateRepositoryConfiguration>`_

.. code-block:: python

 params = {}
 params["key"] = "my_repo_name"
 params["description"] = "new_description"
 r = af.repositories.update_repository_configuration(params)
 # params is a dictionary (some fields are mandatory) of the repository settings that will be updated


Delete Repository
^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteRepository <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteRepository>`_

.. code-block:: python

 r = af.repositories.delete_repository(repo_key)
 # repo_key is the name of the repository in Artifactory


Calculate YUM Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateYUMRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateYUMRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_yum_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory

 # Additionnal options from the documentation can be supplied as a string
 r = af.calculate_yum_repository_metadata(repo_key, options=string_of_options)
 # Such as [?path={path to repodata dir][&async=0/1]

 # a GPG passphrase can be supplied
 gpg_passphrase = "abc"
 r = af.calculate_yum_repository_metadata(repo_key, x_gpg_passphrase=gpg_passphrase)


Calculate NuGet Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNuGetRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNuGetRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_nuget_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory


Calculate Npm Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNpmRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateNpmRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_npm_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory


Calculate Maven Index
^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenIndex <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenIndex>`_

.. code-block:: python

 r = af.repositories.calculate_maven_index(options)
 # options is a string of the possible options
 # Such as [?repos=x[,y]][&force=0/1]


Calculate Maven Metadata
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateMavenMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_maven_metadata(repo_key, folder_path)
 # repo_key is the name of the repository in Artifactory
 # folder_path is the path of the folder inside the repo

 # Additionnal options from the documentation can be supplied as a string
 r = af.repositories.calculate_maven_metadata(repo_key, folder_path, options=string_of_options)
 # Such as {nonRecursive=true | false}


Calculate Debian Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateDebianRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateDebianRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_debian_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory

 # Additionnal options from the documentation can be supplied as a string
 r = af.calculate_debian_repository_metadata(repo_key, options=string_of_options)
 # Such as [?async=0/1][?writeProps=0/1]

 # a GPG passphrase can be supplied
 gpg_passphrase = "abc"
 r = af.calculate_debian_repository_metadata(repo_key, x_gpg_passphrase=gpg_passphrase)


Calculate Opkg Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateOpkgRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateOpkgRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_opkg_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory

 # Additionnal options from the documentation can be supplied as a string
 r = af.calculate_opkg_repository_metadata(repo_key, options=string_of_options)
 # Such as [?async=0/1][?writeProps=0/1]

 # a GPG passphrase can be supplied
 gpg_passphrase = "abc"
 r = af.calculate_opkg_repository_metadata(repo_key, x_gpg_passphrase=gpg_passphrase)


Calculate Bower Index
^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateBowerIndex <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateBowerIndex>`_

.. code-block:: python

 r = af.repositories.calculate_bower_index(repo_key)
 # repo_key is the name of the repository in Artifactory


Calculate Helm Chart Index
^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateHelmChartIndex <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateHelmChartIndex>`_

.. code-block:: python

 r = af.repositories.calculate_helm_chart_index(repo_key)
 # repo_key is the name of the repository in Artifactory


Calculate CRAN Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateCRANRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateCRANRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_cran_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory

 # Additionnal options from the documentation can be supplied as a string
 r = af.repositories.calculate_cran_repository_metadata(repo_key, options=string_of_options)
 # Such as [?async=0/1]


Calculate Conda Repository Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateCondaRepositoryMetadata <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CalculateCondaRepositoryMetadata>`_

.. code-block:: python

 r = af.repositories.calculate_conda_repository_metadata(repo_key)
 # repo_key is the name of the repository in Artifactory

 # Additionnal options from the documentation can be supplied as a string
 r = af.repositories.calculate_conda_repository_metadata(repo_key, options=string_of_options)
 # Such as [?async=0/1]

SEARCHES
--------

Artifactory Query Language
^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactoryQueryLanguage(AQL) <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ArtifactoryQueryLanguage(AQL>`_\ )

.. code-block:: python

 query = "aql_querry_string"
 r = af.searches.artifactory_query_language(query)
 # Example : query = "items.find({"repo":{"$eq":"my-repo"}})"


List Docker Repositories
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerRepositories <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerRepositories>`_

.. code-block:: python

 r = af.searches.list_docker_repositories(repo_key)
 # repo_key is the name of the repository in Artifactory

 # Additionnal options from the documentation can be supplied as a string
 r = af.searches.list_docker_repositories(repo_key, options=string_of_options)
 # Such as ?n=<n from the request>&last=<last tag value from previous response>


List Docker Tags
^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerTags <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListDockerTags>`_

.. code-block:: python

 r = af.searches.list_docker_tags(repo_key, image_path)
 # repo_key is the name of the repository/registry in Artifactory
 # image_path is the path of the docker image in the repository/registry

 # Additionnal options from the documentation can be supplied as a string
 r = af.searches.list_docker_repositories(repo_key, image_path, options=string_of_options)
 # Such as ?n=<n from the request>&last=<last tag value from previous response>


SECURITY
--------

Get Users
^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUsers <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUsers>`_

.. code-block:: python

 r = af.security.get_users()


Get User Details
^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserDetails <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserDetails>`_

.. code-block:: python

 r = af.security.get_user_details(username)
 # username is the name of the user in Artifactory


Get User Encrypted Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserEncryptedPassword <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetUserEncryptedPassword>`_

.. code-block:: python

 r = af.security.get_user_encrypted_password()


Create or Replace User
^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceUser <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceUser>`_

.. code-block:: python

 params = {}
 params["name"] = "my_username"
 params["admin"] = "false"
 params["email"] = "myuser@orange.com"
 params["password"] = "password"
 r = af.security.create_or_replace_user(params)
 # username is the name of the user in Artifactory
 # params ia a dictionary of desired fields to use to create the user and their value(s)
 # https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON


Update User
^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateUser <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateUser>`_

.. code-block:: python

 params = {}
 params["admin"] = "true"
 r = af.security.update_user(params)
 # username is the name of the user in Artifactory
 # params ia a dictionary of desired fields to update and their value(s)
 # https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON


Delete User
^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteUser <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteUser>`_

.. code-block:: python

 r = af.security.delete_user(username)
 # username is the name of the user in Artifactory.


Get Locked Out Users
^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetLockedOutUsers <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetLockedOutUsers>`_

.. code-block:: python

 r = af.security.get_locked_out_users()


Unlock Locked Out User
^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUser <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUser>`_

.. code-block:: python

 r = af.security.unlock_locked_out_user(username)
 # username is the name of the user in Artifactory.


Unlock Locked Out Users
^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUsers <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockLockedOutUsers>`_

.. code-block:: python

 r = af.security.unlock_locked_out_users(user_list)
 # user_list is a python list of the users to unlock


Unlock All Locked Out Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockAllLockedOutUsers <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UnlockAllLockedOutUsers>`_

.. code-block:: python

 r = af.security.unlock_all_locked_out_users()


Create API Key
^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateAPIKey <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateAPIKey>`_

.. code-block:: python

 r = af.security.create_api_key()


Regenerate API Key
^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RegenerateAPIKey <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RegenerateAPIKey>`_

.. code-block:: python

 r = af.security.regenerate_api_key()


Get API Key
^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetAPIKey <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetAPIKey>`_

.. code-block:: python

 r = af.security.get_api_key()


Revoke API Key
^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeAPIKey <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeAPIKey>`_

.. code-block:: python

 r = af.security.revoke_api_key()


Revoke User API Key
^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeUserAPIKey <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-RevokeUserAPIKey>`_

.. code-block:: python

 r = af.security.revoke_user_api_key(username)
 # username is the name of the user in Artifactory


Get Groups
^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroups <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroups>`_

.. code-block:: python

 r = af.security.get_groups()


Get Group Details
^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroupDetails <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetGroupDetails>`_

.. code-block:: python

 r = af.security.get_group_details(group_name)
 # group_name is the name of the group in Artifactory.


Create or Replace Group
^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceGroup <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplaceGroup>`_

.. code-block:: python

 params = {}
 params["group_name"] = "my_group"
 r = af.security.create_or_replace_group(params)
 # params is a python dictionnary which should be like :
 # https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON


Update Group
^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateGroup <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-UpdateGroup>`_

.. code-block:: python

 params = {}
 params["group_name"] = "my_group"
 params["description"] = "my_description"
 r = af.security.update_group(params)
 # params is a python dictionnary which should be like :
 # https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON


Delete Group
^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteGroup <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteGroup>`_

.. code-block:: python

 r = af.security.delete_group(group_name)
 # group_name is the name of the group in Artifactory.


Get Permission Targets
^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargets <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargets>`_

.. code-block:: python

 r = af.security.get_permission_targets()


Get Permission Target Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargetDetails <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetPermissionTargetDetails>`_

.. code-block:: python

 r = af.security.get_permission_target_details(permission_target_name)
 # permission_target_name is the name of the permission in Artifactory.


Create or Replace Permission Target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplacePermissionTarget <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateorReplacePermissionTarget>`_

.. code-block:: python

 params = {}
 params["name"] = "my_permission"
 params["repositories"] = ["myrepo1", "myrepo2"]
 r = af.security.create_or_replace_permission_target(params)
 # https://www.jfrog.com/confluence/display/RTF4X/Security+Configuration+JSON


Delete Permission Target
^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeletePermissionTarget <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeletePermissionTarget>`_

.. code-block:: python

 r = af.security.delete_permission_target(permission_target_name)
 # permission_target_name is the name of the permission in Artifactory.


Effective Item Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EffectiveItemPermissions <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-EffectiveItemPermissions>`_

.. code-block:: python

 r = af.security.effective_item_permissions(repo_key, item_path)
 # repo_key is the name of the repository in Artifactory
 # item_path is the path of the item inside the repo
 # To get information on the root repo, use "", as argument for item_path


SUPPORT
-------

Create Bundle
^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateBundle <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateBundle>`_

.. code-block:: python

 # params is a python dictionnary which should be like :
 # https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-CreateBundle
 params = rtpy.json_to_dict("tests/templates/bundle_creation.json")
 r = af.support.create_bundle(params)


List Bundles
^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListBundles <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-ListBundles>`_

.. code-block:: python

 r = af.support.list_bundles()


Get Bundle
^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBundle <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetBundle>`_

.. code-block:: python

 # bundle_name is the name of the bundle
 r = af.support.get_bundle(bundle_name)
 with open(my_bundle_name, "wb") as bundle_file:
     bundle_file.write(r.content)


Delete Bundle
^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteBundle <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-DeleteBundle>`_

.. code-block:: python

 # bundle_name is the name of the bundle
 r = af.support.delete_bundle(bundle_name)


SYSTEM AND CONFIGURATION
------------------------

System Info
^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemInfo <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemInfo>`_

.. code-block:: python

 r = af.system_and_configuration.system_info()


System Health Ping
^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemHealthPing <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SystemHealthPing>`_

.. code-block:: python

 r = af.system_and_configuration.system_health_ping()


General Configuration
^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GeneralConfiguration <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GeneralConfiguration>`_

.. code-block:: python

 r = af.system_and_configuration.general_configuration()


Save General Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SaveGeneralConfiguration <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SaveGeneralConfiguration>`_

.. code-block:: python

 r = af.system_and_configuration.save_general_configuration(xml_file_path)
 # xml_file_path is the path on the local machine of the configuration file to be pushed


License Information
^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-LicenseInformation <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-LicenseInformation>`_

.. code-block:: python

 r = af.system_and_configuration.license_information()


Install License
^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-InstallLicense <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-InstallLicense>`_

.. code-block:: python

 params = {"licenseKey": "license_string"}
 r = af.system_and_configuration.install_license(params)


Version and Addons Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-VersionandAdd-onsinformation <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-VersionandAdd-onsinformation>`_

.. code-block:: python

 r = af.system_and_configuration.version_and_addons_information()


Get Reverse Proxy Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration>`_

.. code-block:: python

 r = af.system_and_configuration.get_reverse_proxy_configuration()


Get Reverse Proxy Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxyConfiguration>`_

.. code-block:: python

 r = af.system_and_configuration.get_reverse_proxy_configuration()


Get Reverse Proxy Snippet
^^^^^^^^^^^^^^^^^^^^^^^^^

`https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxySnippet <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-GetReverseProxySnippet>`_

.. code-block:: python

 r = af.system_and_configuration.get_reverse_proxy_snippet()

