
import requests, json, sys
import time
from datetime import datetime, date, timedelta
import pprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, operator
from jinja2 import Environment, FileSystemLoader

#####################################################################
### Properties and Variables
#####################################################################

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)



url = sys.argv[1]
headers = {'content-type': 'application/json'}

pp = pprint.PrettyPrinter(indent=4)
hostIDs = []
hostDict = {}
zabbixHostWiseCount = {}
zabbixAlertWiseCount = {}
context = {}

totalCount = 0

logFile = "/tmp/dailyAlertMail.log"
logFH = open(logFile, 'a')

mailFrom = "no-reply@localdomain.com"

mailToStr = "me@example.com"
mailToList = ["me@example.com"]

###################################################################
### Functions 
###################################################################

def render_template(template_filename, context):

    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
 
def getAuthToken():

	authPayload = { 
		"jsonrpc": "2.0", 
		"method": "user.login", 
		"params": {
			"user": "admin", 
			"password": "zabbix"
			}, 
		"id": 1, 
		"auth": None
	}

	authToken = requests.post(url, data = json.dumps(authPayload), headers=headers).json()
	if authToken.has_key('error'):
		return [False, authToken['error']['data']]
	else:
		return [True, authToken['result']]

def getAllHostList():

	authResult = getAuthToken()

	if not authResult[0]:
		# Authentication failed. Retry...
		authResult = getAuthToken()

	if authResult[0]:
		gethosts = {
			"jsonrpc": "2.0",
			"method": "host.get",
			"params": {
				"output": "extend"
				},
			"auth": authResult[1],
			"id": 1
			}

		hostlist = requests.post(url, data=json.dumps(gethosts), headers=headers).json()

		hostDict = {}
		hostIDs = []

		for hostObj in hostlist['result']:
	
			hostDict[hostObj['hostid']] = hostObj['host']
			hostIDs.append(hostObj['hostid'])

		return hostIDs, hostDict

	else:
		sys.exit()
	
def getTime():

	yesterday = date.today() - timedelta(1)
	reqTime = time.mktime(datetime.strptime(yesterday.strftime('%d/%m/%Y'), "%d/%m/%Y").timetuple())
	return reqTime


#######################################################################
### Sending mail
#######################################################################

hostIDs, hostDict = getAllHostList()
reqTime = getTime()

pp.pprint(hostDict)
for hostid in hostIDs:

	#zabbixAlerts[hostDict[hostid]] = {}
	#zabbixAlerts[hostDict[hostid]]['alertWiseCount'] = {}

	#zabbixHostWiseCount[hostDict[hostid]] = {}
	print "working on host = " + hostDict[hostid]
	zabbixAlertWiseCount[hostDict[hostid]] = {}
	#zabbixAlertWiseHost[hostDict[hostid]]['alertWiseCount'] = {}


	#hostWiseAlerts[hostDict[hostid]] = {}

	### Get Alerts Details

	authResult = getAuthToken()

	if not authResult[0]:
		# Authentication failed. Retry...
		authResult = getAuthToken()

	if authResult[0]:

		alertPayload = {
			"jsonrpc": "2.0",
			"method": "alert.get",
			"params": {
				"output": "extend",
				"time_from": reqTime,
				"hostids": hostid
		    },
		    "auth": authResult[1],
		    "id": 1
		}

		alertList = requests.post(url, data=json.dumps(alertPayload), headers=headers).json()

		### Get Events Details

		eventPayload = {
	        	"jsonrpc": "2.0",
		        "method": "event.get",
	        	"params": {
	                	"output": "extend",
		                "time_from": reqTime,
		                "hostids": hostid
		    },
		    "auth": authResult[1],
		    "id": 1
		}

		eventList = requests.post(url, data=json.dumps(eventPayload), headers=headers).json()

		## get only PROBLEM EVENTS

		problemEvents = []
		for prob in eventList['result']:

			if prob['source'] == '0' and prob['value'] == '1':
				problemEvents.append(prob['eventid'])

		#zabbixAlerts[hostDict[hostid]]['totalAlertCount'] = len(problemEvents)
		zabbixHostWiseCount[hostDict[hostid]] = len(problemEvents)
		totalCount += len(problemEvents)

		print "total alerts for host: " + str(zabbixHostWiseCount[hostDict[hostid]])

		for alert in alertList['result']:

			#key = alert['eventid']

			#if alert['eventid'] in problemEvents and not alertDict.has_key(key):

			#	alertDict[key] = {}
			#	alertDict[key]['host'] = hostDict[hostid]
			#	alertDict[key]['message'] = alert['subject']
			#	alertDict[key]['time'] = datetime.fromtimestamp(int(alert['clock'])).strftime('%Y-%m-%d %H:%M:%S')

			if alert['eventid'] in problemEvents:

			#	hostWiseAlerts[hostDict[hostid]][alert['subject']] = hostWiseAlerts[hostDict[hostid]].get(alert['subject'], 0) + 1

				#zabbixAlerts[hostDict[hostid]]['alertWiseCount'][alert['subject']] = zabbixAlerts[hostDict[hostid]]['alertWiseCount'].get(alert['subject'], 0) + 1

				zabbixAlertWiseCount[hostDict[hostid]][alert['subject']] = zabbixAlertWiseCount[hostDict[hostid]].get(alert['subject'], 0) + 1
					
		#pp.pprint(zabbixAlerts[hostDict[hostid]])

		## Get Host wise count
		#hostWiseCount[hostDict[hostid]] = len(problemEvents)

		print "alerts for this host: "
		pp.pprint(zabbixAlertWiseCount[hostDict[hostid]])

		if len(zabbixAlertWiseCount[hostDict[hostid]].keys()) == 0:
			# No alerts for this host. Delete it
			del zabbixAlertWiseCount[hostDict[hostid]]


	else:
		sys.exit()


#######################################################################
### Sending mail
#######################################################################

yesterday = date.today() - timedelta(1)
yesterdayTime = yesterday.strftime('%d/%m/%Y')

msg = MIMEMultipart('alternative')
msg['Subject'] = "Zabbix alerts for " + yesterdayTime
msg['From'] = mailFrom
msg['To'] = mailToStr

context['count'] = totalCount
#context['zabbixAlerts'] = {}

context['zabbixHostWiseCount'] = {}
context['zabbixHostWiseCount'] = zabbixHostWiseCount

context['zabbixAlertWiseCount'] = {}
context['zabbixAlertWiseCount'] = zabbixAlertWiseCount

html = render_template('email_template.html', context)

html = MIMEText(html, 'html')
msg.attach(html)


# Send using postflix
s = smtplib.SMTP('localhost')
s.sendmail(mailFrom, mailToList, msg.as_string())
#s.sendmail("digitalgoldzabbix@local.com", ['sunny1.gupta@paytm.com'], msg.as_string())
s.quit()


logText = "{0} events occured on {1}".format(totalCount, yesterdayTime)
logFH.write(logText)
logFH.write('\n')

logFH.write(str(zabbixHostWiseCount))
logFH.write('\n')

logFH.write(str(zabbixAlertWiseCount))
logFH.write('\n')

logText = "Mail Sent"
logFH.write(logText)
logFH.write('\n')
logFH.write("====================================")

logFH.close()
