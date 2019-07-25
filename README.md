# aws-user-call-history
Python script to fetch and count the API calls made by an AWS IAM User that were logged in CloudTrail's [Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the last 24hrs.
<br/>
<br/>
In the script, this is accomplished by calling [lookup_events()](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudtrail.html#CloudTrail.Client.lookup_events) for each region and noting the eventName and eventSource if the event is an AwsApiCall. It then counts and prints the totals for each API call.
<br/>
<br/>
**Sample output:**
<br/>
`
Total API calls made by Shaun in the last 24 hours:
{('LookupEvents', 'cloudtrail.amazonaws.com'): 361, ('ListBuckets', 's3.amazonaws.com'): 5, ('DeleteBucket', 's3.amazonaws.com'): 1, ('GetBucketObjectLockConfiguration', 's3.amazonaws.com'): 2}...
`

**TODO:**
Note that this CloudTrail API limits results returned by a call to 50. I need to adjust the script to account for pagination.
