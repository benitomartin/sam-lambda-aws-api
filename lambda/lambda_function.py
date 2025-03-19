import json
import random

def lambda_handler(event, context):
    try:
        # Extract min and max from event body
        body = json.loads(event.get('body', '{}'))
        min_value = int(body.get('min', 1))  # Default min is 1
        max_value = int(body.get('max', 100))  # Default max is 100

        # Generate random number within the specified range
        random_number = random.randint(min_value, max_value)

        # Return the random number as part of the response
        return {
            'statusCode': 200,
            'body': json.dumps({'random_number': random_number})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
