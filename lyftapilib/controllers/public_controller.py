# -*- coding: utf-8 -*-

"""
    lyftapilib.controllers.public_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 11/14/2016
"""

from .base_controller import *
from ..models.cost_estimate_response import CostEstimateResponse
from ..models.eta_estimate_response import EtaEstimateResponse
from ..models.ride_types_response import RideTypesResponse
from ..models.nearby_drivers_response import NearbyDriversResponse
from ..exceptions.error_exception import ErrorException

class PublicController(BaseController):

    """A Controller to access Endpoints in the lyftapilib API."""

    def get_cost(self,
                 start_lat,
                 start_lng,
                 ride_type = None,
                 end_lat = None,
                 end_lng = None):
        """Does a GET request to /cost.

        Cost estimates

        Args:
            start_lat (float): Latitude of the starting location
            start_lng (float): Longitude of the starting location
            ride_type (RideType40Enum, optional): ID of a ride type
            end_lat (float, optional): Latitude of the ending location
            end_lng (float, optional): Longitude of the ending location

        Returns:
            CostEstimateResponse: Response from the API. An object with an
                array of cost estimates by ride type

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/cost'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Process optional query parameters
        _query_parameters = {
            'start_lat': start_lat,
            'start_lng': start_lng,
            'ride_type': ride_type,
            'end_lat': end_lat,
            'end_lng': end_lng
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Apply authentication.
        OAuth2.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Endpoint error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('400 - The \'error\' field will be one of the following:  * `bad_parameter`: A validation error occurred  * `no_service_in_area`: start location is not within a Lyft service area  * `ridetype_unavailable_in_region`: ridetype not supported at this start location ', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, CostEstimateResponse.from_dictionary)



    def get_eta(self,
                lat,
                lng,
                ride_type = None):
        """Does a GET request to /eta.

        Pickup ETAs

        Args:
            lat (float): Latitude of a location
            lng (float): Longitude of a location
            ride_type (RideType40Enum, optional): ID of a ride type

        Returns:
            EtaEstimateResponse: Response from the API. An object with an
                array of ETAs by ride type for the given location

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/eta'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Process optional query parameters
        _query_parameters = {
            'lat': lat,
            'lng': lng,
            'ride_type': ride_type
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Apply authentication.
        OAuth2.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Endpoint error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('400 - The \'error\' field will be one of the following:  * `bad_parameter`: A validation error occurred  * `no_service_in_area`: location is not within a Lyft service area  * `ridetype_unavailable_in_region`: ridetype not supported at this location ', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, EtaEstimateResponse.from_dictionary)



    def get_ridetypes(self,
                      lat,
                      lng,
                      ride_type = None):
        """Does a GET request to /ridetypes.

        Types of rides

        Args:
            lat (float): Latitude of a location
            lng (float): Longitude of a location
            ride_type (RideType40Enum, optional): ID of a ride type

        Returns:
            RideTypesResponse: Response from the API. An object with an array
                of available Ride Types for the given location

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/ridetypes'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Process optional query parameters
        _query_parameters = {
            'lat': lat,
            'lng': lng,
            'ride_type': ride_type
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Apply authentication.
        OAuth2.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Endpoint error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('400 - A validation error occurred', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, RideTypesResponse.from_dictionary)



    def get_drivers(self,
                    lat,
                    lng):
        """Does a GET request to /drivers.

        Available drivers nearby

        Args:
            lat (float): Latitude of a location
            lng (float): Longitude of a location

        Returns:
            NearbyDriversResponse: Response from the API. An object with an
                array of available drivers sorted by eta for the given
                location

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.base_uri
 
        # Prepare query string for API call
        _query_builder += '/drivers'

        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Process optional query parameters
        _query_parameters = {
            'lat': lat,
            'lng': lng
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare the API call.
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Apply authentication.
        OAuth2.apply(_request)

        # Execute the request.
        _context = self.execute_request(_request)        

        # Endpoint error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('400 - A validation error occurred', _context)

        # Global error handling using HTTP status codes.
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, NearbyDriversResponse.from_dictionary)


