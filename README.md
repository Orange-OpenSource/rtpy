# rtpy

[![image](https://img.shields.io/pypi/v/rtpy.svg)](https://pypi.org/project/rtpy/)
[![image](https://img.shields.io/pypi/pyversions/rtpy.svg)](https://pypi.org/project/rtpy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Documentation Status](https://readthedocs.org/projects/rtpy/badge/?version=latest)](https://rtpy.readthedocs.io/en/latest/?badge=latest)
[![image](https://img.shields.io/pypi/l/rtpy.svg)](https://pypi.org/project/rtpy/)

Python wrapper for the **[JFrog Artifactory REST API](https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API)**
<br/>
<br/>

## Documentation

**[https://rtpy.rtfd.io](https://rtpy.rtfd.io)**

<br/>

## Installation

```shell
$ pip install rtpy
```
<br/>

## Usage

```python
import rtpy

# instantiate a rtpy.Rtpy object
settings = {}
settings["af_url"] = "http://..."
settings["api_key"] = "123QWA..."
# settings["username"] = "my_username"
# settings["password"] = "my_password"

af = rtpy.Rtpy(settings)

# use a method
r = af.system_and_configuration.system_health_ping()
print(r)
# OK
```
<br/>

## Running the tests

### Requirements :

- Dependencies : see [tool.poetry.dependencies] and [tool.poetry.dev-dependencies] in [pyproject.toml](./pyproject.toml)
- Artifactory instance (with a valid license) running

**NEVER run the tests on a production instance!**


### Launch

- Set the following environment variables:
    - AF_TEST_URL
    - AF_TEST_USERNAME
    - AF_TEST_PASSWORD

The user must have admin privileges (it's API key will be revoked during the tests)
- Clone the repository and launch the tests using the command :

```shell
$ python -m pytest -v
```