# Connecting AWS Lambda and RDS Postgres
This repo is for accessing RDS Postgres database from an AWS Lambda function. The [AWS Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-lambda-tutorial.html) for connecting Lambda to RDS only works for MySQL at the moment and not Postgres.

## Usage Instructions
Requires Python 3.9 and psycopg2 2.9.9<br/>
The steps for configuring AWS services and deploying this as a Lambda function are available in this Medium article.

## Files Walkthrough
##### lambda_function.py
The core functionality for connecting to RDS Postgres. It retrieves the database credentials from AWS Secrets Manager, connects to the DB and returns the results from a table as JSON. The method ```lambda_handler()``` will be invoked by AWS Lambda when a relevant event is triggered. 

Note: AWS Lambda executes ```lambda_function.lambda_handler()``` by default. If you want to use a different filename or function name, update the Lambda Runtime Configuration on the AWS console.

##### psycopg2
psycopg2 is the most popular PostgreSQL database adapter for Python. This is included here in this repo because fetching it automatically using ```pip install psycopg2-binary``` command results in the following Lambda execution error "Unable to import module 'rds_connector': No module named 'psycopg2._psycopg'". 

You need a version of psycopg2 with libpq.so statically linked for using it on AWS. This pre-built version of psycopg2 for Python 3.9 was obtained from https://github.com/jkehler/awslambda-psycopg2. If you need this for later versions of Python, you can also check https://pypi.org/project/aws-psycopg2/

##### AWSLambda-RDS-Postgres-Basic.zip
This contains the psycopg2 directory + a simplified lambda_function.py that does not require setting up AWS Secrets Manager. To use this:
- Create a Lambda Function by choosing the 'From Scratch' option.
- Upload the zip file.
- Edit the database host, username, password and region specified in the lambda_function.py
- Deploy and test.

##### AWSLambda-RDS-Postgres.zip
This contains the files in this repo as-is. Follow the instructions given for using this as the Lamdba source zip.


