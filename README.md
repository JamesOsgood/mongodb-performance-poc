# mongodb-performance-poc
Framework for collecting data around Performance PoCs

## Server ##

The server is configured by copying 

```config/server.js.tmpl -> config/server.js```

and updating server.js, in particular, update the mongodb connection string

To start the server

```
cd server\src
node index.js
```

# REST API #

The API provides the following methods

| URL  | Verb | Body  | Description  |
|---|---|---|---|
|  /test_run/\<id\> | POST | N/A | Create a test run with the given id  |
|  /test_run/\<id\> | GET | N/A | Get a test run with the given id  |
|  /test_run/\<id\> | DELETE | N/A | Delete a test run with the given id  |
|  /test_run/\<id\> | PATCH | measurements to add | Add a measurement to a test run  |

## Examples ##
__POST__ - Create a test run

```
POST http://localhost:3334/test_run/Test_2019-07-31T12:08:46.130899
```
Returns
```json
{"test_id": "Test_2019-07-31T12:08:46.130899", "message": "Created test run: Test_2019-07-31T12:08:46.130899"}
```

<br/>

__DELETE__ - Delete a test run

```
DELETE http://localhost:3334/test_run/Test_2019-07-31T12:08:46.130899
```
Returns
```json
{"message": "Deleted test run: Test_2019-07-31T12:08:46.130899"}
```

<br/>

__PATCH__ - Add measurements to a test run

```
PATCH http://localhost:3334/test_run/Test_2019-07-31T12:08:46.130899
```
with body
```json
{"measurement_name": "total_documents", "measurements": [{"timestamp": "2019-07-31T16:25:27.465980", "value": 40}]}
```

Returns
```json
{"message": "ok"}
```

This method does a ```$push``` to add the measurements to the appropriate sub document in the test run.
<br/>

__GET__ - Get measurements for a test run

```
GET http://localhost:3334/test_run/Test_2019-07-31T12:08:46.130899
```

Returns
```json
{
    "_id": "Test_2019-07-31T12:08:46.130899", 
    "last_modified": "2019-07-31T15:30:15.221Z", 
    "total_documents": [{"timestamp": "2019-07-31T16:30:14.284963", "value": 0}, 
                        {"timestamp": "2019-07-31T16:30:14.552173", "value": 20}, 
                        {"timestamp": "2019-07-31T16:30:14.843060", "value": 40}, 
                        {"timestamp": "2019-07-31T16:30:15.112255", "value": 60}], 
    "cpu": [{"timestamp": "2019-07-31T16:30:14.414098", "value": 10}, 
            {"timestamp": "2019-07-31T16:30:14.689399", "value": 30}, 
            {"timestamp": "2019-07-31T16:30:14.966002", "value": 50}]}
```

# TESTS #

The tests are written in python using [PySys](https://github.com/pysys-test/pysys-test)

Run all the tests 

```
cd testcases/test_run
pysys.py run
```
