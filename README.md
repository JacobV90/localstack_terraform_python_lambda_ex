
# AWS Lambda and Terraform local development using Localstack and Docker

## Why?.. To save time and money

By mocking some of the aws services, we can develop locally without having to deploy to AWS.

This configuration achieves this by mounting our host machines file system to the docker containers starting from localstack, we can develop lambdas locally and have the changes take affect immediately when the lamba is invoked.

### Requirements
  * python3.x
  * terraform
  * docker engine 2.2.5 and docker compose
  

Mac 
``` bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up
```
