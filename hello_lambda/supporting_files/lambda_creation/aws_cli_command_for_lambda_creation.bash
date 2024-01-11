#!/bin/bash

aws lambda create-function \
--function-name $1 \
--zip-file fileb://${1}.zip \
--runtime python3.8 \
--role $2 \
--handler hello_lambda.lambda_handler \
--timeout 3 \
--memory-size 256 \
--architectures x86_64 