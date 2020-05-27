
# AWS Lambda and Terraform local development using Localstack and Docker

## Why?.. To save time and money

By mocking some AWS services, we can develop locally without having to deploy to AWS. This capability will help increase the development cycle by reducing the feedback time.

This example project leverages a docker compose file to spin up a local Localstack instance and an infrastructure service that uses terraform to deploy an AWS Lambda Function to the running Localstack instance on your computer.

The docker-compose configuration will mount the projects directory to the docker containers started by localstack. This is done to enable rapid development. Any changes made will take effect when the file is saved so theres no need to redeploy the lambda function to localstack.

## Requirements
  * python3.x
  * docker and docker compose

## Installation

### Mac/Linux 
``` bash
cd localstack_terraform_python_lambda_ex
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows
``` powershell
cd localstack_terraform_python_lambda_ex
python3 -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

Now run:
```
docker-compose up
```

You should see localstack outputting logs. The infrastructure service will wait for Localstack to be ready inorder to deploy the lambda function. 

Once the lambda function is deployed, run in an acivated terminal:
```
awslocal lambda invoke --function-name lambda-function response.json
```

The lambda function should have been successfully invoked and should return its connection status to the MySql database.

And thats it! You can now make changes to the lambda functions code without having to deploy to AWS or redeploy to Localstack. 