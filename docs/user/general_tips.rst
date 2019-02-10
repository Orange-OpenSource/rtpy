General tips
============

Verify connectivity with Rtpy self call
---------------------------------------
Call an instantiated Rtby object to verify connectivity (binding to the system health ping method)

.. code-block:: python

 import rtpy

 # instantiate a Rtpy object
 settings = {}
 settings["af_url"] = "http://..."
 settings["api_key"] = "123QWA..."
 # settings["username"] = "my_username"
 # settings["password"] = "my_password"

 af = rtpy.Rtpy(settings)
 r = af()
 # or r = af.system_and_configuration.system_health_ping()
 # print(r)
 # OK

Environment variables as settings
---------------------------------

Use environement variables for the api_key and af_url in the settings dictionary

.. code-block:: python

 settings = {}
 settings["af_url"] = os.environ["ARTIFACTORY_URL"] # URL of the AF instance
 settings["api_key"] = os.environ["ARTIFACTORY_API_KEY"] # User/Admin API key in the given AF instance

 af = rtpy.Rtpy(settings)

Overriding settings
-------------------

All the settings can be overridden for a **single function call** (original settings are restored when the call is over)
This is useful for debugging (verbose level) or not raising errors (raw_response). It can also be used to provide different credentials

.. code-block:: python

 r = af.category.method_xyz(settings={"raw_response" : True, "verbose_level" : 1})

 r = af.category.method_xyz(settings={"verbose_level" : 1})

 r = af.category.method_xyz(settings={"api_key" : "123ABC..."})

 session = requests.Session()
 session.verify = "path/to/ca_bundle.crt"
 r = af.category.method_xyz(settings={"session" : session})


pretty-print
------------

Use the pprint package to print the json responses in a more readable way

.. code-block:: python

 from pprint import pprint
 ...
 r = af.category.method_xyz()
 pprint(r)


Json file to Python dictionary
------------------------------

Convert a json file to a python dictionnary using the json_to_dict method

.. code-block:: python

 my_dict = rtpy.json_to_dict(json_file_path)