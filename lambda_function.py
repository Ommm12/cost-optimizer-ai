import json
import boto3
import datetime

sns = boto3.client('sns')
ce = boto3.client('ce')

TOPIC_ARN = "arn:aws:sns:ap-northeast-1:584570449633:cost-alert"

def lambda_handler(event, context):
    today = datetime.date.today()
    start = today - datetime.timedelta(days=7)

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': str(start),
            'End': str(today)
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    total_cost = 0
    for day in response['ResultsByTime']:
        total_cost += float(day['Total']['UnblendedCost']['Amount'])

    message = f"🚨 Weekly AWS Cost: ${total_cost:.2f}"

    print(message)

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="AWS Cost Alert"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }