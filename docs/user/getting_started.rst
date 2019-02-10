Getting started
===============

Instantiate a rtpy.Rtpy object
------------------------------

A rtpy.Rtpy object is used to make all the API calls.
To be instantiated the rtpy.Rtpy class only takes a **Python dictionary as first positional argument**.
This dictionary contains the user's settings such as API key and Artifactory instance URL.

Mandatory keys
^^^^^^^^^^^^^^


* **"af_url"** : URL of the AF instance (starting with http(s)://)
* **"api_key"** or **"username"** and **"password"** : API key or username and password for the user in the Artifactory instance

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


Optional keys
^^^^^^^^^^^^^


* **"verbose_level"** : 0/1

  * The desired verbose level, 0 for nothing, 1 to print performed operations
  * 0 if not not provided

* **"raw_response"** : False/True

  * True will return a `requests.Response object <http://docs.python-requests.org/en/master/api/#requests.Response>`_ and the errors will not be automatically raised
  * False will return a python object
  * False if not provided

* **"session"**\ : `requests.Session <http://docs.python-requests.org/en/master/api/#requests.Session>`_ object

  * rtpy uses a `requests.Session <http://docs.python-requests.org/en/master/api/#requests.Session>`_ object to make calls to the Artifactory API endpoint. A custom can be provided session object when creating a rtpy.Rtpy object for advanced HTTP configurations, proxies, SSL...
  * request.Session() if not provided

.. code-block:: python

 import requests
 import rtpy

 settings["verbose_level"] = 0/1
 settings["raw_response"] = False/True

 # SSL : custom CA bundle example
 session = requests.Session()
 session.verify = "path/to/ca_bundle.crt"
 settings['session'] = session

 af = rtpy.Rtpy(settings)

 r = af.system_and_configuration.system_health_ping()
 print(r)
 # OK