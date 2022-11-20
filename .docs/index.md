---
title: Tools
hide:
    - toc
    - footer
    - navigation
---


#

__This package contains a helpers for fast & easy building a micro-applications.__

For installing the package please run

```bash linenums='1'
pip3 install skyant-tools
```

## Authentication

Google Cloud Platform provides two features for authenticating HTTP requests:
__direct to an instance__ (Cloud Run, Cloud Function, etc) with
[Identity Access Manager](https://cloud.google.com/iam) or __through
[Identit Aware Proxy](https://cloud.google.com/iap)__.

The package ```skyant.tools.auth``` provides features for convenience as for making a request 
well as read it & getting an authenticated user name.


## Duty

The [duty](https://pypi.org/project/duty/) is a simple and beautiful task runner for developers.

The ```skyant.tools.duty``` provides some typically tasks for everyday.


## Cryptography

More action related to cryptography is hard for the majority of developers, so wo provides some
everyday features:

- symmetric encrypt/decrypt data with a password

- calculating a hash of dict base on __only data value__

```py linenums='1' title='example'
hash_a = skyant.tools.crypto.data_hash({'a': 3, 'b': [2, 1]})
hash_b = skyant.tools.crypto.data_hash({'b': [1, 2], 'a': 3})

hash_a == hash_b
True
```

!!!info
    It is [the ROADMAAP task](https://gitlab.com/skyant/python/tools/-/issues/2).

