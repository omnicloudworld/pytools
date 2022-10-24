'''
Objects for working with authentication tools in Google Cloud Platform
'''

import json as _json
from base64 import b64decode as _b64d
from warnings import warn as _warn
from flask import request as _request
from jose import jwt as _jwt
import requests as _requests


def get_gcp(
    headers: dict
    # http headers as dict
) -> dict:
    '''
    Returns the decoded authentication data from HTTP headers which was used
    for get access to Google Cloud Platform entity such as Cloud Run or Cloud Function.
    '''

    if 'authorization' in headers and headers['authorization'] != '':
        token = headers['authorization']
    else:
        return None

    try:
        b64_profile = token[7:].split('.')[1]
        profile = _b64d(b64_profile + '=' * (-len(b64_profile) % 4))
    except Exception as ex:
        _warn(f'Wrong header containt.\n{ex}')
        return None

    return _json.loads(profile)


def get_iap(
    audience: str
    # string which was used througt JWT making
) -> dict:
    '''
    Requests coming through IAP have special headers.

    Return the authenticated user's data if available from Cloud Identity Aware Proxy (IAP).
    If IAP is not active, returns None.
    Raises an exception if IAP header exists, but JWT token is invalid, which
    would indicates bypass of IAP or inability to fetch KEYS.
    '''

    assertion = _request.headers.get('X-Goog-IAP-JWT-Assertion')
    if assertion is None:   # Request did not come through IAP
        _warn('X-Goog-IAP-JWT-Assertion Assertion error.')
        return None

    info = _jwt.decode(
        assertion,
        _requests.get('https://www.gstatic.com/iap/verify/public_key').json(),
        algorithms=['ES256'],
        audience=audience
    )

    return info
