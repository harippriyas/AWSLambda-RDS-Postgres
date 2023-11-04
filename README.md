# AWSLambda-RDS-Postgres
Connecting to RDS Postgres from AWS Lambda

## Build
To build the zip file for uploading to AWS Lambda
```
Make any necessary changes in the python script.
Zip up the files in this directory.
Upload to AWS Lambda.
```

To update the psycopg to latest, you can check what is available at https://github.com/jkehler/awslambda-psycopg2/tree/master. 

Note: Automatically fetching the library using the ```pip install psycopg2-binary -t . ``` command results in the following Lambda execution error ```Unable to import module 'rds_connector': No module named 'psycopg2._psycopg'```. You need a version of psycopg2 with the libpq.so statically linked. This version of the psycopg2 is pre-built and available in the above GitHub.

https://github.com/NajiAboo/aws-lambda-python/tree/main