# TRIANGLE TYPE API
This project exposes an API that calculates the triangle type given its dimensions

### Live API
https://e20i1w5aog.execute-api.us-east-1.amazonaws.com

### Endpoints

Calculate the triangle type
`/triangle-type`


The API documentation is made using Swagger

## API

### Documentation
The API documentation is provided by Swagger where is possible to see the OpenAPI v3 specification and test the API endpoints 
> https://e20i1w5aog.execute-api.us-east-1.amazonaws.com/swagger


## Infrastructure diagram

![Infrastructure diagram](https://github.com/devtiagomantay/triangule-type-api/blob/13-implement-the-triangule-type-calculations/triangule-api-serverless/infrastructure.png)


## How to run locally

### Install the dependencies:

> pip install -r requirements.txt

### Run the Flask app

Since it's a flask app to run the app run the command (inside de app folder):

> python -m flask run

The standar port of the web server is 5000. The success message should be:

```bash
python -m flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [21/Dec/2022 18:54:33] "GET /swagger/ HTTP/1.1" 200 -
127.0.0.1 - - [21/Dec/2022 18:54:33] "GET /swagger/swagger-ui.css HTTP/1.1" 200 -
127.0.0.1 - - [21/Dec/2022 18:54:33] "GET /swagger/swagger-ui-bundle.js HTTP/1.1" 200 -
127.0.0.1 - - [21/Dec/2022 18:54:33] "GET /swagger/swagger-ui-standalone-preset.js HTTP/1.1" 200 -
127.0.0.1 - - [21/Dec/2022 18:54:33] "GET /static/swagger.json HTTP/1.1" 200 -
127.0.0.1 - - [21/Dec/2022 18:54:33] "GET /swagger/favicon-32x32.png HTTP/1.1" 200 -
```

`OBS: For now the database will not be available locally, so just the /triangle-type endpoint will work properly. So the history of the requests will not be available since there is no persistence`

## How to run tests?

### Test API endpoints

You can use the swagger endpoint, the postman collection or do it manually (using curl or a web browser for instance):
```
URL: https://7c7679299b.execute-api.us-east-1.amazonaws.com/dev/triangle-type
METHOD: POST
BODY: Use JSON/RAW format. Example:
{
    "dimensions": [9,9,9]
}
```

### Unit tests
Unit tests using pytest and are located in the ```triangle_calc_test.py``` file.

To run type the command:

> pytest


## How to deploy in AWS

The deployment can be made in automate way using the **serverless framework** and the **AWS CLI**

More information about how use the serverless framework on SERVERLESS_DOC.md

``` Work in progess: A script to install all the requirements in one command ```

Requirements:
* Python 3.9 (A virtual environment is recommended)
* AWS CLI
> https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
* serverless-python-requirements
> sls plugin install -n serverless-python-requirements
* NodeJS
> https://nodejs.org/en/download/package-manager/
* JDK
> sudo apt install default-jdk



### Deploy the infrastructure
``` Configure the AWS CLI with you AWS credentials before using the deploy command```
> sls deploy
