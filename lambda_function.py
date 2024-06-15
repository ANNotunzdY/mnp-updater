import json
import requests

def lambda_handler(event, context):
    url = "https://g4bvjgz8cj.execute-api.ap-northeast-1.amazonaws.com/Prod/update"
    response = requests.get(url)
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
