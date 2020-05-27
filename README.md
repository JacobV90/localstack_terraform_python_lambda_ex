
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

Create a **.env** file in the top level directory with these variables:
```
TF_VAR_PROJECT_ABS_PATH={your_absolute_path_to_this_project}
TF_VAR_PYTHON_LIB_PATH={relative_path_to_python_packages}
```

## Running the example project
```
docker-compose up
```

After the docker images are pulled down and built, you should see Localstack outputting logs when its container is started. *The infrastructure service will wait for Localstack to be ready inorder to deploy the lambda function.* 

Once the lambda function is deployed, run in a python virtual environment activated terminal:
```
awslocal lambda invoke --function-name lambda-function response.json
```
>[awslocal](https://github.com/localstack/awscli-local) is python package that mimics the **awscli** tool but is tailored towards Localstack. It makes it very easy to interact with Localstack like you normally would with AWS.

The lambda function should have been successfully invoked and should return its connection status to the MySql database.

**And thats it!**

You can now make changes to the lambda functions code without having to deploy to AWS or redeploy to Localstack. 