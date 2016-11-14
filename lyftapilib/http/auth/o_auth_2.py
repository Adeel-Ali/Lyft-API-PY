# -*- coding: utf-8 -*-

"""
   lyftapilib.http.auth.oauth2

   This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 11/14/2016
"""

from ...configuration import *

class OAuth2:

    @staticmethod
    def apply(http_request):
        """ Add OAuth2 authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which 
                authentication will be added.

        """
        token = Configuration.o_auth_access_token
        header_value = "Bearer {}".format(token)
        http_request.headers["Authorization"] = header_value