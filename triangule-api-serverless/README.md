
# HOW TO DEPLOY

The deployment can be made in automate way using the serverless framework and the AWS CLI

More information about how use the serverless framework on SERVERLESS_DOC.md

``` Work in progess: A script to install all the requirements is in progress ```


![Infrastructure diagram]([infrastructure.drawio.png](..%2Fdoc%2Finfrastructure.drawio.png))


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
``` Configure the AWS CLI with you AWS account ```
> pip install -r requirements.txt

## Deploy the infrastructure

> sls deploy


