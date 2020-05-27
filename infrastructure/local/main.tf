provider "aws" {
  access_key                  = "mock_access_key"
  region                      = "us-east-1"
  secret_key                  = "mock_secret_key"
  s3_force_path_style         = true
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    lambda         = "http://localstack:4574"
  }
}

variable PROJECT_ABS_PATH {
  type    = "string"
  default = ""
}

variable PYTHON_LIB_PATH {
  type    = "string"
  default = ""
}

resource "aws_lambda_function" "lambda_function" {
  s3_bucket     = "__local__"
  s3_key        = "${var.PROJECT_ABS_PATH}"

  function_name = "lambda-function"
  handler       = "src.lambda_function.handler"
  runtime       = "python3.7"

  role          = ""

  environment {
    variables = {
      PYTHONPATH  = "/var/task/${var.PYTHON_LIB_PATH}"

      DB_HOST     = "mysql"
      DB_NAME     = "example"
      DB_USER     = "root"  
      DB_PASSWORD = "password"
    }
  }
}