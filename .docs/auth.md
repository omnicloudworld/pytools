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


## Read headers

