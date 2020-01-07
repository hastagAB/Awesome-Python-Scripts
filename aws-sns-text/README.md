Hello! Thank you for using aws-sns-text.py! 
This script should be used to send a text message using the AWS SNS service. 

BEFORE USING
1. In AWS IAM, create a user that has "AmazonSNSFullAcces" privileges
2. Be sure your environment satisfies the reqirements listed in the requirements.txt file

USAGE INSTRUCTIONS
1. Navigate to your folder containing aws-sns-text.py
2. type "python aws-sns-text.py" to launch the program
3. Enter the key ID obtained through the AWS IAM service
4. Enter the key secret obtained through the AWS IAM service
5. Enter the AWS region where your IAM credentials were created
6. Enter the phone number you wish to send the text
7. Enter the message you wish to send

Your console output should resemble the following:
Enter AWS key ID: SD78GHMW56BFRWQ3
Enter AWS key secret: skjef789sdfJOSD9893^&ww90$nweq
Enter AWS region: us-east-1
Enter phone number: +16248973287
Enter message: hello world!

If all fields are entered correctly, the message will send successfully!




