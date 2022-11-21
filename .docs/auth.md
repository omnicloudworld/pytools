---
title: AUTH
hide:
    - navigation
---

#


The class provides features to working with authentication systems that work in GCP for
access to HTTP endpoints.

The GCP contains two HTTP authentication systems:

__- on the instance security level (Identity Access Manager)__

_This system controls traffic directly on endpoints (Cloud Run, Cloud Functions, etc).
In the case when your instance required authentication HTTP requests will be passed
to instance only if it contains an "authentication" header with Bearer token. The
authentication header should approve that request's sender has a role Invoker._

__- on the load balancing system (Identity Aware Proxy)__

_IAP provides feature for pass or block traffic to one or more endpoints base on OAuth2.
IAP can use two subsystems as an identity provider:_

  - Identity Access Manager

  _in this case authenticated user can become only Google account, but IAM can provides
  permission to group (through Google Groups for business)_

  - Identity Platform

  _in this case authentication will done through identity provider such as Facebook,
  Twitter, Google, etc, but you cant use Google Groups for business_

The HeaderGCP work with Identity Access Manager on both system only now.


```py linenums='1' title='making the instance from environment'
from skyant.tools.auth import HeaderGCP

env_auth = HeaderGCP()
```

The ```env_auth``` will be created authentication headers for your service account of your
Google Cloud instance which defined during deployment.

For test code in development environment you should pass to the environment variable
GOOGLE_APPLICATION_CREDENTIALS a path to the service account key in JSON format.


Also you can pass service account to instance initialisation procedure.

```py linenums='1' title='making the instance from service account'
from skyant.tools.auth import HeaderGCP

sa_auth = HeaderGCP('path_to_service_account_key.json')
```

## Making headers

The instance of ```skyant.tools.auth.HeaderGCP``` contains two methods for assist you to created
a HTTP headers.

### make_bearer

This method makes a bearer header for your service account & provided scope.

=== "IAM with direct access"

    ```py linenums='1' title='make bearer'
    from skyant.tools.auth import HeaderGCP

    hgcp = HeaderGCP('key.json')

    token = hgcp.make_bearer('https://my.cloud-google-host.com')

    request_headers = {
        'authentication': token
    }
    ```

=== "IAM behind Identity Aware Proxy & Load Balancer"

    ```python linenums='1' title='make bearer'
    from skyant.tools.auth import HeaderGCP

    hgcp = HeaderGCP('key.json')

    token = hgcp.make_bearer('user_id') # (1)!

    request_headers = {
        'authentication': token
    }
    ```

    1. The user_id is __NOT email__. Please looking for user_id in service account key.


In this case the variable "token" will contains token in format "Bearer {token}".  The "authentication"
header is sufficient for access to Google Cloud instances such as Cloud Run if your service 
account has a role "* Invoker".

### fill_header

For more easy making a HTTP header you can use method ```fill_header```. This method not only makes
a token but insert it into a current headers.

=== "code"
    ```py linenums='1' title='fill header'
    from skyant.tools.auth import HeaderGCP

    request_headers = {
        'Content-Type': 'applications/json'
    }

    hgcp = HeaderGCP('key.json')

    request_headers = hgcp.fill_header('https://my.cloud-google-host.com')

    request_headers
    ```

=== "result"

    ```py linenums='1' title='new header'
    {
        'Content-Type': 'applications/json',
        'Authentication': 'Bearer aowiejfow34ituow4utowuotuwgt52g'
    }
    ```

!!!info
    The method ```fill_header``` overwrites the Authentication header if it exist. For saving
    original header set argument ```replace``` to ```True```.

    ```py linenums='1' title='not replace'
    request_headers = hgcp.fill_header('https://my.cloud-google-host.com', replace=False)
    ```

!!!warning
    If you use domain alias, your alias work ONLY as host name. The scope argument always must be
    set as instance URL from Google Cloud Console.


## Read headers

If your instance was got a request then requested user was been authenticated by Google Cloud Platform.
Despite this in some cases you needs to know who send request.

In this case you can read the headers by read_auth class method that returns full & decrypted
related header [^1] or get_user which returns only email as a string.
{ .annotate }

[^1]: Dependent on traffic got to you from the header will be different. The read_auth analyses all variants.

