import boto3
from botocore.exceptions import ClientError
import os


def send_email(name, email, message):
    sender_email = os.getenv("SENDER_EMAIL_ADDRESS")
    receiver_email = os.getenv("RECEIVER_EMAIL_ADDRESS")
    aws_region = os.getenv("AWS_REGION")
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY_ID")

    client = boto3.client(
        'ses',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    )

    subject = "New Contact Form Message"
    body_text = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    body_html = f"""<html>
    <head></head>
    <body>
      <h1>New Contact Form Message</h1>
      <p>Name: {name}<br>
         Email: {email}<br>
         Message: {message}</p>
    </body>
    </html>
                """
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    receiver_email,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=sender_email,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
