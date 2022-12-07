# Stores_REST_API_with_Flask_in_Python

Note:- Project still in development not completed yet.

## Commands to run the dockerfile

docker build -t rest-api-python-flask .

docker run --name rest_api_project -dp 5005:5000 rest-api-python-flask


################################

Flask smorest abort will help in documentation of the APIs. because return message with error code for not found is a manual thing and it will create issues that is why we use flask_smorest

### To use docker with HOT RELOADING

docker build -t restapi-python-flask-smorest .

docker run -dp 5000:5000 -w /app -v "/d/REST_API_Flask:/app" restapi-python-flask-smorest


### Swagger UI
http://127.0.0.1:5000/swagger-ui


### Notes
1. Adding Blueprints & MethodViews - swagger 1
2. Adding marshmellow schemas - swagger 2
3. Validation using marshmellow schemas  - swagger 2
4. Decorating response from Flask smorest API - swagger 3