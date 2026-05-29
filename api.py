import os
os.environ['MOESIF_APPLICATION_ID'] = 'eyJhcHAiOiIxMDUxOjg3NCIsInZlciI6IjIuMSIsIm9yZyI6Ijg3OjczMSIsImlhdCI6MTc3NzU5MzYwMH0.R3d7yXUze4eHQAapprsbKuNkpKa2QJUdlI3ZX-soh34'

from moesif_aws_lambda import MoesifLogger
# ... geri kalan kodun
moesif_options = {
    'application_id': 'eyJhcHAiOiIxMDUxOjg3NCIsInZlciI6IjIuMSIsIm9yZyI6Ijg3OjczMSIsImlhdCI6MTc3NzU5MzYwMH0.R3d7yXUze4eHQAapprsbKuNkpKa2QJUdlI3ZX-soh34',
    'log_body': True # İsteğe bağlı: API gövdelerini de loglamak istersen True yap
}

@MoesifLogger(moesif_options)
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'isBase64Encoded': False,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': '{"msg": "Hello from Lambda!"}' # Body string formatında olmalı
    }