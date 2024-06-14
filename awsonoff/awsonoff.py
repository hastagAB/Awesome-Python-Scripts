#*****************************************************************
#	Author: 		Cody WIlliams	
#
#	Date: 			2020-01-06	
#
#	Program Name: 	awspower.py
#
#	Description: 	This script should be ran from the command line
# 					with the purpose of starting / stopping an 
#					AWS ec2 instance. This utilizes the
#					AWS boto3 API. To use, type...
#					python awspower.py [region] [instance-id] [on/off]				
#*****************************************************************


import boto3 #used to interact with AWS API
import sys #used to support command line functionality

#Prints the usage of the script
def print_usage():
	print('USAGE: python awspower.py [region] [instance-id] [on/off]')

#function for the creation of a session in a specified region
def get_session(r):
    return boto3.session.Session(region_name=region)

#Retrieve arguements from the command line
region = sys.argv[1]
ID = sys.argv[2]
action = sys.argv[3]

#Create the session and client
session = get_session(region)
client = session.client('ec2') 

#start the instance or stop the instance
if action == 'on':
	client.start_instances(InstanceIds=[ID])
	print('ec2 instance ' + ID + ' turned on!')
elif action == 'off': 
	client.stop_instances(InstanceIds=[ID])
	print('ec2 instance ' + ID + ' turned off!')
else: 
	print_usage()
   