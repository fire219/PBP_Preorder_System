#!/usr/bin/python3

# This is the DISTRIBUTABLE VERSION of the Pinebook Pro preorder system.
# It has been sanitized of hazardous infrastructure information.
#
# Pinebook Pro Pre-order Registration System
# 7/25/19 -- written by Matthew Petry (fire219)

# Clean Start Script (redbutton[bk].py)

import os
from sys import argv

print("Content-type:text/html\r\n\r\n")
if (__file__ != "<webdir>/PBPCoupon/9NgwkQLt/redbutton.cgi"):
	print("<html><body>Not the correct copy of the file!</body></html>")
	sys.exit()
print("<html><body>")
print("<p>")
os.system("rm <datadir>/preorder_files/PBP-Preorders*")
namefile = open("<datadir>/preorder_files/namefile.txt", "w")
namefile.write("loltotallyfakenamenotreal")
namefile.close()
namefile = open("<datadir>/preorder_files/countfile.txt", "w")
namefile.write("0")
namefile.close()
print("</p>")
print("	Red Button activated.")
print(" This script will now self destruct. Good luck, Agent Lukasz.</p></body></html>")
os.remove(argv[0]) 
