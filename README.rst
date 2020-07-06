.. role:: raw-html-m2r(raw)
   :format: html


rtpy
====


.. image:: https://img.shields.io/pypi/v/rtpy.svg
   :target: https://pypi.org/project/rtpy/
   :alt: image


.. image:: https://img.shields.io/pypi/pyversions/rtpy.svg
   :target: https://pypi.org/project/rtpy/
   :alt: image


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black


.. image:: https://readthedocs.org/projects/rtpy/badge/?version=latest
   :target: https://rtpy.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://img.shields.io/pypi/l/rtpy.svg
   :target: https://pypi.org/project/rtpy/
   :alt: image


Python wrapper for the **\ `JFrog Artifactory REST API <https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API>`_\ **
:raw-html-m2r:`<br/>`
:raw-html-m2r:`<br/>`

Documentation
-------------

**\ `https://rtpy.rtfd.io <https://rtpy.rtfd.io>`_\ **

:raw-html-m2r:`<br/>`

Installation
------------

.. code-block:: shell

   $ pip install rtpy

:raw-html-m2r:`<br/>`

Usage
-----

.. code-block:: python

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

:raw-html-m2r:`<br/>`

Running the tests
-----------------

Requirements :
^^^^^^^^^^^^^^


* Dependencies : see [tool.poetry.dependencies] and [tool.poetry.dev-dependencies] in `pyproject.toml <./pyproject.toml>`_
* Artifactory instance (with a valid license) running

**NEVER run the tests on a production instance!**

Launch
^^^^^^


* Set the following environment variables:

  * AF_TEST_URL
  * AF_TEST_USERNAME
  * AF_TEST_PASSWORD

The user must have admin privileges (it's API key will be revoked during the tests)


* Clone the repository and launch the tests using the command :

.. code-block:: shell

   $ python -m pytest -v
