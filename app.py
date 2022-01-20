#!/usr/bin/env python3

import aws_cdk as cdk

from infrastructure.hello_lambda import HelloLambdaStack


app = cdk.App()
HelloLambdaStack(app, "hello-lambda")

app.synth()
