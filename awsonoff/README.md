Hello! Thank you for using awsonoff.py! 
This python script is a handy tool for starting and stopping your aws-ec2 instances

USAGE INSTRUCTIONS
1. Configure your aws connection using the command "aws configure"
	-Ensure that you provide the proper public and secret keys, and region name
	-these keys can be retrieved through the aws IAM service 

2. Navigate to the location that you have saved the awsonoff.py file

3. To run type...
	- python awsonoff.py [region of instance] [instance id] [on/off]
	- example: "python awsonoff.py us-west-1 i-asc563varg4 on" 
