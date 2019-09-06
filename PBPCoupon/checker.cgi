#!/usr/bin/python3.5

# This is the DISTRIBUTABLE VERSION of the Pinebook Pro preorder system.
# It has been sanitized of hazardous infrastructure information.
#
# Pinebook Pro Pre-order Registration System
# 7/25/19 -- written by Matthew Petry (fire219)

# Client Facing "Checker Script" (checker.cgi)

import sys
import cgi
import hashlib
sys.path.append('<sql_connector_lib_dir>')
import mysql.connector
import smtplib
import datetime
import csv
import mmap

dbuser = 'fakeDBuser'
dbpass = 'fakeSQLpass'

db = mysql.connector.connect (user=dbuser, password=dbpass,
								host='127.0.0.1', database='database_name' charset='utf8')

formData = cgi.FieldStorage()
username = formData.getvalue('username-entry')
password = formData.getvalue('password-entry')

#username = sys.argv[1]
#password = sys.argv[2]

html_upper = ("""
<head>
<title>Pinebook Pro Forum Bonus</title>
<link rel="stylesheet" href="style.css" type="text/css" />
<link rel="stylesheet" href="fade.css" type="text/css" />
<link href="https://fonts.googleapis.com/css?family=Raleway&display=swap" rel="stylesheet">
</head>

<body>
<div class="topimage">
	<a href="https://pine64.org"><img class="navimage" src="pine64_logo.png"></a>
</div>
<div class="header">
	<span>Pinebook Pro Coupon Redemption</span>
</div>
<div class="floater">
	<img class="pineimg" src="count2.jpg">
	<img class="pineimg" src="count3.jpg">
	<img class="pineimg" src="count4.jpg">""")
html_lower = """	</div>
					</div>
					</body>"""
					
email_template = """From: Pine64 <no-reply@pine64.org> 
To: <user> <email>
Subject: Welcome to the Pinebook Pro!

	Dear <user>, Thank you for your interest in the Pinebook Pro. You have successfully reserved a spot in the priority preorder system. Please be on the 
lookout for a member of the PINE64 Sales team to be sending you your Coupon Code.

Please note that this coupon code will be required at time of purchase of a Pinebook Pro. Upon checkout, you must use the same email address which you registered on the PINE64 Forum.
You can only buy a Pinebook Pro and Pinebook Pro accessories per coupon. The NVMe M.2 SSD adapter will be available at checkout for $6.99.

Please note that VAT and any types of import duty and taxes have not been added to the total value of all goods in the consignment. Please note that if your shipping address is located in a remote area, there will be a remote area surcharge on the delivery of your item.

If you encounter any problems during your purchase, you are always welcome to contact us by replying to this email pinebook@pine64.org

The Pinebook warranty period is 30 days and all sales are final, meaning a no return policy.

Please let us know if you need further assistance. 
We will be more than happy to assist you. 

Thank you. 
 
Sincerely, 
PINEBOOK Team 
http://store.pine64.org """

if (password is None) or (username is None):
        print(html_upper)
        print("<p style='color:red;'>Login failure! Please <a href = \"javascript:history.back()\">go back</a> and check your username and password.</p>")
        print(html_lower)
        sys.exit()


rawpasshash = hashlib.md5(password.encode()).hexdigest()
password = '00000000000000000000000000000000000000'

usercursor = db.cursor()

query = "SELECT password, salt, regdate, email FROM <===FAKE_TABLE===> WHERE username=%s"
				
usercursor.execute(query,(username,))
dbrow = usercursor.fetchone()

if dbrow is None:
	print(html_upper)
	print("<p style='color:red;'>Login failure! Please <a href = \"javascript:history.back()\">go back</a> and check your username and password.</p>")
	print(html_lower)
	sys.exit()


dbpass = dbrow[0]
salt = dbrow[1]
regdate = dbrow[2]
useremail = dbrow[3]

rawsalthash = hashlib.md5(salt.encode()).hexdigest()
finalhash = hashlib.md5((rawsalthash + rawpasshash).encode()).hexdigest()

if (finalhash == dbpass):
	print(html_upper)
	print("<p style='color:green;'>Login was successful.</p><br>")
else:
	print(html_upper)
	print("<p style='color:red;'>Login failure! Please <a href = \"javascript:history.back()\">go back</a> and check your username and password.</p>")
	print(html_lower)
	sys.exit()
	
if (regdate > 1561939200):
	print("<p>Sorry, you do not qualify for pre-order priority and eMMC upgrade.</p>")
	print(html_lower)
	sys.exit()

namefile = open('<datadir>/namefile.txt', 'a+')
namebytes = (" "+username+" ").encode()

with mmap.mmap(namefile.fileno(), 0, access=mmap.ACCESS_READ) as s:
	if (s.find(namebytes) != -1):
		print("<p>Sorry, you have already entered the preorder queue.</p>")
		print(html_lower)
		sys.exit()

countfile = open("<datadir>/countfile.txt", "r+")
countnum = int(countfile.read())

if (countnum > 1089):
                print("<p>Sorry, this phase of Pinebook Pro preorders has ended. Look out for more information on our forum and social media channels..</p>")
                print(html_lower)
                sys.exit()

countfile.seek(0)
countfile.write(str(countnum + 1))
	
namefile.write(" " +username+ " ")
namefile.close()
	
print("<p>Congrats, you qualify for pre-order priority and eMMC upgrade!</p>")
print("<p>You have received a confirmation email. If you do not see it, please check your email Spam folder. Expect to hear from a member of the Sales Team soon, as they will be sending you your coupon code.</p>")
print(html_lower)

	
#mailtest = open("email.txt", 'w')

sender = 'no-reply@pine64.org'
receivers = [useremail]

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, email_template.replace("<user>", username).replace("<email>", "<"+useremail+">"))         
   #print("Successfully sent email")
except SMTPException:
   #print("Error: unable to send email")
   pass

#mailtest.write(email_template.replace("<user>", username).replace("<email>", "<"+useremail+">"))
#mailtest.close()

timehandle = datetime.datetime.now()
currenttime = timehandle.strftime("%b-%d-Hour-%H")


with open("<datadir>/indiv_files/"+currenttime+"-"+username+".csv", mode='a') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csv_writer.writerow([username, useremail, datetime.datetime.now()])

with open("<datadir>/PBP-Preorders-"+currenttime+".csv", mode='a') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csv_writer.writerow([username, useremail, datetime.datetime.now()])
