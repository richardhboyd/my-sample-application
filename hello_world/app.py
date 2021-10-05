import json
from datetime import date
import calendar

def lambda_handler(event, context):
    my_date = date.today()
    weekday = calendar.day_name[my_date.weekday()]
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": weekday,
        }),
    }
