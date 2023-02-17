import boto3

def gettestmail():
    accesskey = ""
    secretkey = ""
    region = ""
    topic_arn = ""
    sns = boto3.resource("sns", aws_access_key_id=accesskey, aws_secret_access_key=secretkey, region_name=region)
    response = sns.Topic(topic_arn).publish(
        Message="This is a test message!!",
        Subject="TEST"
        )
    print("response is {}".format(response))
