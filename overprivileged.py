from datetime import datetime, timedelta
import boto3
import json

cloudtrail = boto3.client("cloudtrail")
print(cloudtrail)

response = cloudtrail.lookup_events(
    LookupAttributes=[
        {
            'AttributeKey': 'EventName',
            'AttributeValue': 'CreateAccessKey'
        },
    ],
    StartTime=datetime.utcnow() - timedelta(hours=24),
    EndTime=datetime.utcnow()
)

print(json.dumps(response, sort_keys=True, indent=4, default=str))