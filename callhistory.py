from datetime import datetime, timedelta
from collections import Counter
import boto3
import json

# In this example, the IAM User in my account that I will scan is Alice.
username = "alice"
total_api_calls = []

# Get the regions CloudTrail is available in minus ap-east-1,
# because my account has not opted in and ap-east-1 is an opt-in region.
available_cloudtrail_regions = boto3.Session().get_available_regions("cloudtrail")
available_cloudtrail_regions.remove("ap-east-1")

# Make the call to CloudTrail for each available region.
for region in available_cloudtrail_regions:
    cloudtrail = boto3.client("cloudtrail", region_name=region)

    # I'm calling the LookupEvents API and filtering out only events where the username attribute is equal to alice.
    response = cloudtrail.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'Username',
                'AttributeValue': username
            },
        ],
        # Getting the events from the past 24 hours
        StartTime=datetime.utcnow() - timedelta(hours=24),
        EndTime=datetime.utcnow()
    )

    # The response is a dictionary, and I'm interested in the Events key.
    events = response["Events"]

    # For each event in the region, if it is an AwsApiCall, I record the eventName and the eventSource.
    regional_api_calls = []
    for event in events:
        cloudtrail_event = json.loads(event["CloudTrailEvent"])
        if cloudtrail_event["eventType"] == "AwsApiCall":
            api_call = (cloudtrail_event["eventName"], cloudtrail_event["eventSource"])
            regional_api_calls.append(api_call)
            total_api_calls.append(api_call)

    # Printing the total API calls made by the user for the given region
    print("{}:\n{}\n".format(region, dict(Counter(regional_api_calls))))

# Printing the total API calls made by the user
print("Total API calls made by {}:\n{}\n".format(username, dict(Counter(total_api_calls))))