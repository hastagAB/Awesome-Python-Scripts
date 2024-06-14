#Send a text using AWS sns
import boto3

#Retrieve information from the user
key_ID = raw_input("Enter AWS key ID: ")
key_secret = raw_input("Enter AWS key secret: ")
region = raw_input("Enter AWS region: ")
phone = raw_input("Enter phone number: ")
message = raw_input("Enter message: ")

#create the client
client = boto3.client(
    "sns",
    aws_access_key_id=key_ID,
    aws_secret_access_key=key_secret,
    region_name=region
)

# Send your sms message.
client.publish(
    PhoneNumber=phone,
    Message=message
)


