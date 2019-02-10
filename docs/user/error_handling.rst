Error handling
==============

UserSettingsError
-----------------

Standalone error, when the instantiation of the Rtpy object fails due to incorrect settings

.. code-block:: python

 try:
     af = rtpy.Rtpy(settings)
 except rtpy.UserSettingsError:
     # Do stuff


AfApiError
----------

When the status code is 4xx-5xx and the API sends a well formed JSON

The error has specific attributes

.. code-block:: python

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


MalformedAfApiError
-------------------

When the status code is 4xx-5xx and the API sends a malformed JSON

.. code-block:: python

 try:
     # The JSON is currently malformed when the API sends an error when using this method
     af.system_and_configuration.install_license(params)
 except af.MalformedAfApiError:
    # Do stuff


RtpyError
---------

When a method is called and parameters are missing or incorrect

.. code-block:: python

 try:
     # Providing "" for artifact_path will raise the RtpyError
     af.artifacts_and_storage.retrieve_artifact("repo_key", "")
 except af.RtpyError:
     # Do stuff