from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)



class HelloLambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        # RestAPI - this create proxy on sub route
        # / - NOK, /test - OK
        integration = apigateway.LambdaIntegration(my_lambda)
        api = apigateway.RestApi(self, "qe-be-kamil-demo", 
            default_integration=integration)
        api.root.add_proxy(default_integration=integration)
    
        # higher level construct for RestAPI - this works for both cases
        simple_rest_api = apigateway.LambdaRestApi(self, 'qe-be-kamil-demo-oneliner', handler=my_lambda)

      