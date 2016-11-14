#Getting started

## How to Build


You must have Python version 2.7.x or 3.x installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](http://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Lyft%20API-Python)


## How to Use

The following section explains how to use the LyftAPI SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Lyft%20API-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Lyft%20API-Python&projectName=lyftapilib)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](http://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Lyft%20API-Python&projectName=lyftapilib)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](http://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](http://apidocs.io/illustration/python?step=createFile&workspaceFolder=Lyft%20API-Python&projectName=lyftapilib)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from lyftapilib.lyftapi_client import *
```

![Add a new project in PyCharm - Step 4](http://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Lyft%20API-Python&libraryName=lyftapilib.lyftapi_client&projectName=lyftapilib)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](http://apidocs.io/illustration/python?step=runProject&workspaceFolder=Lyft%20API-Python&libraryName=lyftapilib.lyftapi_client&projectName=lyftapilib)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'nosetests'

## Initialization

### Authentication and 
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| o_auth_access_token | The OAuth 2.0 access token to be set before API calls |



API client can be initialized as following.

```python
# Configuration parameters and credentials
o_auth_access_token = "o_auth_access_token" # The OAuth 2.0 access token to be set before API calls

client = LyftAPIClient(o_auth_access_token)
```

## Class Reference

### <a name="list_of_controllers"></a>List of Controllers

* [PublicController](#public_controller)
* [UserController](#user_controller)
* [SandboxController](#sandbox_controller)

### <a name="public_controller"></a>![Class: ](http://apidocs.io/img/class.png ".PublicController") PublicController

#### Get controller instance

An instance of the ``` PublicController ``` class can be accessed from the API Client.

```python
 public_client = client.public
```

#### <a name="get_cost"></a>![Method: ](http://apidocs.io/img/method.png ".PublicController.get_cost") get_cost

> Cost estimates

```python
def get_cost(self,
                 start_lat,
                 start_lng,
                 ride_type = None,
                 end_lat = None,
                 end_lng = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| startLat |  ``` Required ```  | Latitude of the starting location |
| startLng |  ``` Required ```  | Longitude of the starting location |
| rideType |  ``` Optional ```  | ID of a ride type |
| endLat |  ``` Optional ```  | Latitude of the ending location |
| endLng |  ``` Optional ```  | Longitude of the ending location |



#### Example Usage

```python
start_lat = 181.473676746932
start_lng = 181.473676746932
ride_type = RideType40Enum.LYFT
end_lat = 181.473676746932
end_lng = 181.473676746932

result = public_client.get_cost(start_lat, start_lng, ride_type, end_lat, end_lng)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The 'error' field will be one of the following:
 * `bad_parameter`: A validation error occurred
 * `no_service_in_area`: start location is not within a Lyft service area
 * `ridetype_unavailable_in_region`: ridetype not supported at this start location
 |




#### <a name="get_eta"></a>![Method: ](http://apidocs.io/img/method.png ".PublicController.get_eta") get_eta

> Pickup ETAs

```python
def get_eta(self,
                lat,
                lng,
                ride_type = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lat |  ``` Required ```  | Latitude of a location |
| lng |  ``` Required ```  | Longitude of a location |
| rideType |  ``` Optional ```  | ID of a ride type |



#### Example Usage

```python
lat = 181.473676746932
lng = 181.473676746932
ride_type = RideType40Enum.LYFT

result = public_client.get_eta(lat, lng, ride_type)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The 'error' field will be one of the following:
 * `bad_parameter`: A validation error occurred
 * `no_service_in_area`: location is not within a Lyft service area
 * `ridetype_unavailable_in_region`: ridetype not supported at this location
 |




#### <a name="get_ridetypes"></a>![Method: ](http://apidocs.io/img/method.png ".PublicController.get_ridetypes") get_ridetypes

> Types of rides

```python
def get_ridetypes(self,
                      lat,
                      lng,
                      ride_type = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lat |  ``` Required ```  | Latitude of a location |
| lng |  ``` Required ```  | Longitude of a location |
| rideType |  ``` Optional ```  | ID of a ride type |



#### Example Usage

```python
lat = 181.473676746932
lng = 181.473676746932
ride_type = RideType40Enum.LYFT

result = public_client.get_ridetypes(lat, lng, ride_type)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | A validation error occurred |




#### <a name="get_drivers"></a>![Method: ](http://apidocs.io/img/method.png ".PublicController.get_drivers") get_drivers

> Available drivers nearby

```python
def get_drivers(self,
                    lat,
                    lng)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| lat |  ``` Required ```  | Latitude of a location |
| lng |  ``` Required ```  | Longitude of a location |



#### Example Usage

```python
lat = 181.473676746932
lng = 181.473676746932

result = public_client.get_drivers(lat, lng)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | A validation error occurred |




[Back to List of Controllers](#list_of_controllers)

### <a name="user_controller"></a>![Class: ](http://apidocs.io/img/class.png ".UserController") UserController

#### Get controller instance

An instance of the ``` UserController ``` class can be accessed from the API Client.

```python
 user_client = client.user
```

#### <a name="get_rides"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.get_rides") get_rides

> List rides

```python
def get_rides(self,
                  start_time,
                  limit,
                  end_time = None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| startTime |  ``` Required ```  | Restrict to rides starting after this point in time. The earliest supported date is 2015-01-01T00:00:00+00:00 |
| limit |  ``` Required ```  ``` DefaultValue ```  | The maximum number of rides to return. The default limit is 10 if not specified. The maximum allowed value is 50, an integer greater that 50 will return at most 50 results. |
| endTime |  ``` Optional ```  | Restrict to rides starting before this point in time. The earliest supported date is 2015-01-01T00:00:00+00:00 |



#### Example Usage

```python
start_time = datetime.now()
limit = 10
end_time = datetime.now()

result = user_client.get_rides(start_time, limit, end_time)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | A validation error occurred |




#### <a name="get_profile"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.get_profile") get_profile

> The user's general info

```python
def get_profile(self)
```

#### Example Usage

```python

result = user_client.get_profile()

```


#### <a name="update_rides_destination_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.update_rides_destination_by_id") update_rides_destination_by_id

> Update the destination of the ride

```python
def update_rides_destination_by_id(self,
                                       id,
                                       request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The ID of the ride |
| request |  ``` Required ```  | The coordinates and optional address of the destination |



#### Example Usage

```python
id = 'id'
request = Location()

result = user_client.update_rides_destination_by_id(id, request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The 'error' field will be one of the following:
 * `bad_parameter`: A validation error occurred
 * `invalid_destination`: Destination is generally invalid (eg. not in a Lyft service area)
 * `destination_prohibited`: Lyft drop-offs are not permitted at this location (eg. some airports).
 The 'error_description' field will contain an explaination suitable to display to the user.
 * `ride_is_lyft_line`: Cannot change the destination on Line rides
 * `ride_is_finished`: Ride has already been completed
 |
| 403 | User or client does not have permission to complete this request (`ride_does_not_belong_to_user`)
 |
| 404 | No ride found with provided ride ID |




#### <a name="get_rides_receipt_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.get_rides_receipt_by_id") get_rides_receipt_by_id

> Get the receipt of the rides.

```python
def get_rides_receipt_by_id(self,
                                id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The ID of the ride |



#### Example Usage

```python
id = 'id'

result = user_client.get_rides_receipt_by_id(id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 403 | User or client does not have permission to complete this request |
| 404 | No ride receipt found with provided ride ID |




#### <a name="update_rides_rating_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.update_rides_rating_by_id") update_rides_rating_by_id

> Add the passenger's rating, feedback, and tip

```python
def update_rides_rating_by_id(self,
                                  id,
                                  request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The ID of the ride |
| request |  ``` Required ```  | The rating and optional feedback |



#### Example Usage

```python
id = 'id'
request = RatingRequest()

result = user_client.update_rides_rating_by_id(id, request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The 'error' field will be one of the following:
 * `bad_parameter`: A validation error occurred
 * `user_cannot_rate_this_ride`: Rides can only be rated once, within 24 hours of drop-off, and before
 the user starts another ride
 * `tip_too_large`: tip amount is too large for this ride
 * `tip_currency_not_accepted`: That tip currency is not accepted
 |
| 409 | The 'error' field will be:
 * `ride_not_finished`: Ride is still in progress (not yet in the droppedOff state)
 |




#### <a name="get_rides_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.get_rides_by_id") get_rides_by_id

> Get the ride detail of a given ride ID

```python
def get_rides_by_id(self,
                        id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The ID of the ride |



#### Example Usage

```python
id = 'id'

result = user_client.get_rides_by_id(id)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 403 | User or client does not have permission to complete this request |
| 404 | No ride found with provided ride ID |




#### <a name="create_rides_cancel_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.create_rides_cancel_by_id") create_rides_cancel_by_id

> Cancel a ongoing requested ride

```python
def create_rides_cancel_by_id(self,
                                  id,
                                  request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The ID of the ride |
| request |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
id = 'id'
request = CancellationRequest()

result = user_client.create_rides_cancel_by_id(id, request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Cancellation token required
 * `cancel_confirmation_required`: a cancelation fee applies which the user must accept
 * `invalid_cancel_confirmation`: provided token was invalid or expired
 |
| 403 | User or client does not have permission to complete this request |
| 404 | No ride found with provided ride ID |
| 409 | You cannot cancel this ride |




#### <a name="create_rides"></a>![Method: ](http://apidocs.io/img/method.png ".UserController.create_rides") create_rides

> Request a Lyft

```python
def create_rides(self,
                     request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Ride request information |



#### Example Usage

```python
request = Ride()

result = user_client.create_rides(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | The 'error' field can be one of the following:
 * `bad_parameter`: A validation error occurred
 * `no_service_in_area`: origin is not within a Lyft service area
 * `ridetype_unavailable_in_region`: ridetype not supported at origin
 * `primetime_confirmation_required`: user must accept primetime. A primetime confirmation token and
details will be included in the response
 * `invalid_primetime_confirmation`: supplied token is invalid or expired
 * `destination_prohibited`: Lyft is not allowed to drop off at that destination (e.g. some airports).
 User-displayable details in the 'error_description' field
 * `client_error`: an uncategorized error. Details in the 'error_description' field
 |
| 403 | User or client does not have permission to complete this request. Specific errors include:
 * `user_payment_required`: The user does not have a valid payment method on file.
 They must use the Lyft app to add or update one.
 * `account_disabled`: The user's account has been suspended, and they must contact Lyft support.
 * `user_in_driver_mode`: The user is logged in as a driver and can't request rides until they log out
 * `verified_phone_required`: The user has not provided or verified their phone number.
 They can add one in the Lyft app
 |
| 409 | The 'error' field will be one of the following:
 * `no_drivers_available`: No drivers are available right now
 * `user_already_in_ride`: User cannot request a ride while in a ride
 |




[Back to List of Controllers](#list_of_controllers)

### <a name="sandbox_controller"></a>![Class: ](http://apidocs.io/img/class.png ".SandboxController") SandboxController

#### Get controller instance

An instance of the ``` SandboxController ``` class can be accessed from the API Client.

```python
 sandbox_client = client.sandbox
```

#### <a name="update_sandbox_primetime"></a>![Method: ](http://apidocs.io/img/method.png ".SandboxController.update_sandbox_primetime") update_sandbox_primetime

> Preset Prime Time percentage

```python
def update_sandbox_primetime(self,
                                 request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Prime Time to be preset in the region surrounding the lat, lng |



#### Example Usage

```python
request = SandboxPrimetime()

result = sandbox_client.update_sandbox_primetime(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Validation error occurred |




#### <a name="update_sandbox_ridetypes"></a>![Method: ](http://apidocs.io/img/method.png ".SandboxController.update_sandbox_ridetypes") update_sandbox_ridetypes

> Preset types of rides for sandbox

```python
def update_sandbox_ridetypes(self,
                                 request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| request |  ``` Required ```  | Ridetypes to be preset in the region surrounding the lat, lng |



#### Example Usage

```python
request = SandboxRideType()

result = sandbox_client.update_sandbox_ridetypes(request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Validation error occurred |




#### <a name="update_sandbox_ridetypes_by_ride_type"></a>![Method: ](http://apidocs.io/img/method.png ".SandboxController.update_sandbox_ridetypes_by_ride_type") update_sandbox_ridetypes_by_ride_type

> Driver availability for processing ride request

```python
def update_sandbox_ridetypes_by_ride_type(self,
                                              ride_type,
                                              request)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| rideType |  ``` Required ```  | TODO: Add a parameter description |
| request |  ``` Required ```  | Driver availability to be preset in the region surrounding the lat, lng |



#### Example Usage

```python
ride_type = RideType40Enum.LYFT
request = SandboxDriverAvailability()

result = sandbox_client.update_sandbox_ridetypes_by_ride_type(ride_type, request)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Validation error occurred |
| 404 | ride_type provided in the path is not supported in the current area |




#### <a name="update_sandbox_rides_by_id"></a>![Method: ](http://apidocs.io/img/method.png ".SandboxController.update_sandbox_rides_by_id") update_sandbox_rides_by_id

> Propagate ride through states

```python
def update_sandbox_rides_by_id(self,
                                   id,
                                   status)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| id |  ``` Required ```  | The ID of the ride |
| status |  ``` Required ```  | state to propagate the ride into |



#### Example Usage

```python
id = 'id'
status = RideStatusEnum.PENDING

result = sandbox_client.update_sandbox_rides_by_id(id, status)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 400 | Validation error occurred |
| 403 | User or client does not have permission to complete this request |




[Back to List of Controllers](#list_of_controllers)



