import os
os.environ['MOESIF_APPLICATION_ID'] = 'eyJhcHAiOiIxMDUxOjg3NCIsInZlciI6IjIuMSIsIm9yZyI6Ijg3OjczMSIsImlhdCI6MTc3NzU5MzYwMH0.R3d7yXUze4eHQAapprsbKuNkpKa2QJUdlI3ZX-soh34'

from moesif_aws_lambda import MoesifLogger

moesif_options = {'log_body': True}

@MoesifLogger(moesif_options)
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': '{"msg": "Hello from Lambda!"}'
    }

# SAHTE EVENT (API Gateway formatında)
mock_event = {
    "httpMethod": "GET",
    "path": "/test-endpoint",
    "headers": {"Host": "example.com"},
    "queryStringParameters": None,
    "body": None,
    "requestContext": {"requestId": "123"}
}

if __name__ == "__main__":
    lambda_handler(mock_event, {})
    print("İstek Moesif'e gönderildi!")