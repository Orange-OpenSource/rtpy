Responses
=========

The response when using methods can be a :

*
  When "raw_response" is **False** (default):

  * python dictionary or list (a converted json output) (most cases)
  * unicode string (\ `(requests.Response) <http://docs.python-requests.org/en/master/api/#requests.Response>`_.text)  (if the json content can't be decoded/is missing/isn't expected)

*
  When "raw_response" is **True** :

  * `requests.Response Object <http://docs.python-requests.org/en/master/api/#requests.Response>`_