# This is the DISTRIBUTABLE VERSION of the Pinebook Pro preorder system.
# It has been sanitized of hazardous infrastructure information.
#
# Pinebook Pro Pre-order Registration System
# 7/25/19 -- written by Matthew Petry (fire219)

# CSV Sales mailer (CSVhandler.py)


import csv
import smtplib
import datetime
from os.path import basename
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import sys

if (time.time() < 1564056300):
	print("It is not time yet. Not sending files.")
	sys.exit()


sender = 'no-reply@pine64.org'
receivers = ['<sales_team_address>']
filesadded = 0

timehandle = datetime.datetime.now()
if (timehandle.hour == 0):
	prevhour = "23"
	prevhour2 = "22"
	prevhour3 = "21"
	prevday = str(timehandle.day - 1).zfill(2)
	prevtime = timehandle.strftime("%b-"+prevday+"-Hour-"+prevhour)
	prevtime2 = timehandle.strftime("%b-"+prevday+"-Hour-"+prevhour2)
	prevtime3 = timehandle.strftime("%b-"+prevday+"-Hour-"+prevhour3)
else:
	prevhour = str(timehandle.hour - 1).zfill(2)
	prevhour2 = str(timehandle.hour - 2).zfill(2)
	prevhour3 = str(timehandle.hour - 3).zfill(2)
	prevtime = timehandle.strftime("%b-%d-Hour-"+prevhour)
	prevtime2 = timehandle.strftime("%b-%d-Hour-"+prevhour2)
	prevtime3 = timehandle.strftime("%b-%d-Hour-"+prevhour3)
	
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receivers[0]
msg['Subject'] = "PBP Preorders "+prevtime3+"-and-"+prevhour2+"-and-"+prevhour

msg.attach(MIMEText("CSV file(s) attached. Open in Excel."))

print("Looking for PBP-Preorders-"+prevtime3+".csv")
if (os.path.isfile("PBP-Preorders-"+prevtime3+".csv")):
	filesadded = filesadded + 1;
	with open("PBP-Preorders-"+prevtime3+".csv", "rb") as fil:
		ext = "csv"
		attachedfile = MIMEApplication(fil.read(), _subtype = ext)
		attachedfile.add_header(
					'content-disposition', 'attachment', filename=basename("PBP-Preorders-"+prevtime3+".csv") )
		msg.attach(attachedfile)

print("Looking for PBP-Preorders-"+prevtime2+".csv")		
if (os.path.isfile("PBP-Preorders-"+prevtime2+".csv")):
	filesadded = filesadded + 1;
	with open("PBP-Preorders-"+prevtime2+".csv", "rb") as fil:
		ext = "csv"
		attachedfile = MIMEApplication(fil.read(), _subtype = ext)
		attachedfile.add_header(
					'content-disposition', 'attachment', filename=basename("PBP-Preorders-"+prevtime2+".csv") )
		msg.attach(attachedfile)

print("Looking for PBP-Preorders-"+prevtime+".csv")
if (os.path.isfile("PBP-Preorders-"+prevtime+".csv")):
	filesadded = filesadded + 1;
	with open("PBP-Preorders-"+prevtime+".csv", "rb") as fil:
		ext = "csv"
		attachedfile = MIMEApplication(fil.read(), _subtype = ext)
		attachedfile.add_header(
					'content-disposition', 'attachment', filename=basename("PBP-Preorders-"+prevtime+".csv") )
		msg.attach(attachedfile)		


if filesadded > 0:
	smtp = smtplib.SMTP("localhost")
	smtp.sendmail(sender, receivers, msg.as_string())
#	os.rename("PBP-Preorders-"+prevtime+".csv", "bk-PBP-Preorders-"+prevtime+".csv")
	print("Email with "+str(filesadded)+" CSVs sent at "+str(datetime.datetime.now()))
else:
	print("No files found for current period.")