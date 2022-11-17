'''
Object for working with Google Cloud authentication tools.
'''

import json

from google.auth import exceptions
import google.auth.transport.requests as transport_req
from google.oauth2 import id_token, service_account


class GCP():
    '''
    '''

    def __init__(self, key: str = None, **kw):

        self.key = None
        if key:
            try:
                with open(key, "r", encoding='utf-8') as key_file:
                    key_info = json.load(key_file)
                    if key_info.get("type") == "service_account":
                        self.key = key_info

            except ValueError as caught_exc:
                raise exceptions.DefaultCredentialsError(
                    f"The {key} is not valid service account credentials."
                ) from caught_exc

        self.request = transport_req.Request()

    def headers(self, scope: str, current: dict = None, replace: bool = True):

        if self.key:
            cred = service_account.IDTokenCredentials.from_service_account_info(
                self.key,
                target_audience=scope
            )
            cred.refresh(self.request)
            token = cred.token

        else:
            token = id_token.fetch_id_token(self.request, scope)

        header = current or {}
        if ('Authorization' in header or 'authorization' in header) and not replace:
            return header
        if 'Authorization' in header:
            del header['Authorization']

        header['authorization'] = f"Bearer {token}"

        return header
