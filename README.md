# PINE64 Pinebook Pro Forum preorder system

*This is the complete codebase for the preorder system which ran at [this page](https://pine64.org/PBPCoupon/index.html)* from July 25th through August 25th, 2019.

It has been sanitized of any critical infrastructure data (web directory structure, credentials, SQL db info), but is otherwise identical to the "production" version.

File structure:

	=data-directory= (recommended to NOT be in a web-accessible directory)
	¦	- countfile.txt: persistent file used to count how many users have passed through the system
	¦ 	- CSVhandler.py: mails CSV files to sales team
	¦ 	- namefile.txt:  persistent file used to keep track of users who have passed through system (to prevent repeat entries)
	¦
	+ PBPCoupon (web-facing directory)
	¦	+ secret-script (randomly named in production)
	¦	¦	+ redbutton.cgi:    System Clearing script, self-deleting (must be created from redbutton.cgi)
	¦	¦	+ redbutton-bk.cgi: backup copy of redbutton.cgi
	¦ 	¦	
	¦	+ .htaccess:         to enable CGI without Apache config modification
	¦	+ checker.cgi:	     primary script for checking user eligibility and sending confirmation email
	¦	+ count2.jpg:        image on webpage
	¦	+ count3.jpg:        image on webpage
	¦	+ count4.jpg:        image on webpage
	¦	+ forum-header2.png: image on webpage
	¦	+ index.html:        login page
	¦	+ pine64-logo.png:   image on webpage
	¦	+ style.css:         webpage stylesheet
	¦

## License
Copyright 2019 Matthew Petry (fireTwoOneNine) and PINE64

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.