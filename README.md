Django Rest API Endpoints


To Add New User
POST requests are accepted
http://127.0.0.1:8000/api/adduser/
Basic Authentication Required.


To retrieve a self User Data 
GET Requests are accepted
http://127.0.0.1:8000/api/user/
Basic Authentication Required.
only self data can be retrieved


To update(patch) a self User Data 
PATCH Requests are accepted
http://127.0.0.1:8000/api/user/
Basic Authentication Required.
only self data can be updated


