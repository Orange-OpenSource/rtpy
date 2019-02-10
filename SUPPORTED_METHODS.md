# Curently supported REST API methods

- [BUILDS](#builds)
- [ARTIFACTS AND STORAGE](#artifacts-and-storage)
- [SEARCHES](#searches)
- [SECURITY](#security)
- [REPOSITORIES](#repositories)
- [SYSTEM AND CONFIGURATION](#system-and-configuration)
- [PLUGINS](#plugins)
- [IMPORT AND EXPORT](#import-and-export)
- [SUPPORT](#support)

**Original complete JFrog Artifactory REST API method list : https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API**

# BUILDS
 
* [x] All Builds
* [ ] Build Runs
* [ ] Build Upload
* [ ] Build Info
* [ ] Builds Diff
* [ ] Build Promotion
* [ ] Promote Docker Image
* [ ] Delete Builds
* [ ] Build Rename
* [ ] Push Build to Bintray 
* [ ] Distribute Build
* [ ] Control Build Retention

# ARTIFACTS AND STORAGE

* [x] Folder Info
* [x] File Info
* [x] Get Storage Summary Info
* [x] Item Last Modified
* [x] File Statistics
* [x] Item Properties
* [x] Set Item Properties
* [x] Delete Item Properties
* [x] Set Item SHA256 Checksum
* [x] Retrieve Artifact
* [ ] Retrieve Latest Artifact
* [ ] Retrieve Build Artifacts Archive
* [x] Retrieve Folder or Repository Archive
* [x] Trace Artifact Retrieval
* [ ] Archive Entry Download
* [x] Create Directory
* [x] Deploy Artifact
* [x] Deploy Artifact by Checksum
* [ ] Deploy Artifacts from Archive
* [ ] Push a Set of Artifacts to Bintray
* [ ] Push Docker Tag to Bintray
* [ ] Distribute Artifact
* [ ] File Compliance Info
* [x] Delete Item
* [x] Copy Item
* [x] Move Item
* [ ] Get Repository Replication Configuration
* [ ] Set Repository Replication Configuration
* [ ] Update Repository Replication Configuration
* [ ] Delete Repository Replication Configuration
* [ ] Scheduled Replication Status
* [ ] Pull/Push Replication
* [ ] Pull/Push Replication (Deprecated)
* [ ] Create or Replace Local Multi-push Replication 
* [ ] Update Local Multi-push Replication 
* [ ] Delete Local Multi-push Replication 
* [ ] Enable or Disable Multiple Replications
* [ ] Get Global System Replication Configuration
* [ ] Block System Replication
* [ ] Unblock System Replication
* [x] Artifact Sync Download
* [ ] Folder Sync (Deprecated)
* [x] File List
* [x] Get Background Tasks
* [x] Empty Trash Can
* [x] Delete Item From Trash Can
* [x] Restore Item from Trash Can
* [x] Optimize System Storage
* [ ] Get Puppet Modules
* [ ] Get Puppet Module
* [ ] Get Puppet Releases
* [ ] Get Puppet Release

# SEARCHES

* [x] Artifactory Query Language (AQL)
* [ ] Artifact Search (Quick Search)
* [ ] Archive Entries Search (Class Search)
* [ ] GAVC Search
* [ ] Property Search
* [ ] Checksum Search
* [ ] Bad Checksum Search
* [ ] Artifacts Not Downloaded Since
* [ ] Artifacts With Date in Date Range
* [ ] Artifacts Created in Date Range
* [ ] Pattern Search
* [ ] Builds for Dependency
* [ ] License Search
* [ ] Artifact Version Search
* [ ] Artifact Latest Version Search Based on Layout
* [ ] Artifact Latest Version Search Based on Properties
* [ ] Build Artifacts Search
* [x] List Docker Repositories
* [x] List Docker Tags

# SECURITY

* [x] Get Users
* [x] Get User Details
* [ ] Get User Encrypted Password
* [x] Create or Replace User
* [x] Update User
* [x] Delete User
* [ ] Expire Password for a Single User
* [ ] Expire Password for Multiple Users
* [ ] Expire Password for All Users
* [ ] Unexpire Password for a Single User
* [ ] Change Password
* [ ] Get Password Expiration Policy
* [ ] Set Password Expiration Policy
* [ ] Configure User Lock Policy
* [ ] Retrieve User Lock Policy
* [x] Get Locked Out Users
* [x] Unlock Locked Out User
* [x] Unlock Locked Out Users
* [x] Unlock All Locked Out Users 
* [x] Create API Key
* [x] Regenerate API Key
* [x] Get API Key
* [x] Revoke API Key
* [x] Revoke User API Key
* [ ] Revoke All API Keys
* [x] Get Groups
* [x] Get Group Details
* [x] Create or Replace Group
* [x] Update Group
* [x] Delete Group
* [x] Get Permission Targets
* [x] Get Permission Target Details
* [x] Create or Replace Permission Target
* [x] Delete Permission Target
* [x] Effective Item Permissions
* [ ] Security Configuration (Deprecated)
* [ ] Save Security Configuration (Deprecated)
* [ ] Activate Artifactory Key Encryption
* [ ] Deactivate Artifactory Key Encryption
* [ ] Set GPG Public Key
* [ ] Get GPG Public Key
* [ ] Set GPG Private Key
* [ ] Set GPG Pass Phrase
* [ ] Create Token
* [ ] Refresh Token
* [ ] Revoke Token
* [ ] Get Service ID
* [ ] Get Certificates
* [ ] Add Certificate
* [ ] Delete Certificate

# REPOSITORIES

* [x] Get Repositories
* [x] Repository Configuration
* [x] Create Repository
* [x] Update Repository Configuration
* [x] Delete Repository
* [x] Calculate YUM Repository Metadata
* [x] Calculate NuGet Repository Metadata
* [x] Calculate Npm Repository Metadata
* [x] Calculate Maven Index
* [x] Calculate Maven Metadata
* [x] Calculate Debian Repository Metadata
* [x] Calculate Opkg Repository Metadata
* [x] Calculate Bower Index
* [x] Calculate Helm Chart Index
 
# SYSTEM AND CONFIGURATION

* [x] System Info
* [x] System Health Ping
* [ ] Verify Connection
* [x] General Configuration
* [ ] Save General Configuration
* [ ] Update Custom URL Base
* [x] License Information
* [x] Install License
* [x] Version and Add-ons information
* [x] Get Reverse Proxy Configuration
* [ ] Update Reverse Proxy Configuration
* [x] Get Reverse Proxy Snippet

# PLUGINS
 
* [ ] Execute Plugin Code
* [ ] Retrieve Plugin Info
* [ ] Retrieve Plugin Info Of A Certain Type
* [ ] Retrieve Build Staging Strategy
* [ ] Execute Build Promotion 
* [ ] Reload Plugins
 
# IMPORT AND EXPORT

* [ ] Import Repository Content
* [ ] Import System Settings Example
* [ ] Full System Import
* [ ] Export System Settings Example
* [ ] Export System

# SUPPORT 

* [x] Create Bundle
* [x] List Bundles
* [x] Get Bundle
* [x] Delete Bundle