#!/usr/bin/env python3

import aws_cdk as cdk

from iot_sqs_lambda_cdk.iot_sqs_lambda_cdk_stack import IotSqsLambdaCdkStack


app = cdk.App()
IotSqsLambdaCdkStack(app, "IotSqsLambdaCdkStack")

app.synth()
