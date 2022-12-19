# TRIANGLE TYPE API
This project exposes an API that calculates the triangle type given its dimensions

The API documentation is made using Swagger `under construction`

# Infrastructure diagram

![Infrastructure diagram](https://github.com/devtiagomantay/triangule-type-api/blob/13-implement-the-triangule-type-calculations/triangule-api-serverless/infrastructure.png)


# HOW TO DEPLOY

The deployment can be made in automate way using the serverless framework and the AWS CLI

More information about how use the serverless framework on SERVERLESS_DOC.md

``` Work in progess: A script to install all the requirements is in progress ```

Requirements:
* Python 3.9
* AWS CLI
> https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
* serverless-python-requirements
> sls plugin install -n serverless-python-requirements
* NodeJS
> https://nodejs.org/en/download/package-manager/
* JDK
> sudo apt install default-jdk

## Install the dependencies:

> pip install -r requirements.txt

## Deploy the infrastructure
``` Configure the AWS CLI with you AWS account before using the deploy command```
> sls deploy


