import smtplib
from virtual import *

def sendmail():
	gmail_user = 'my.projectexhibition2@gmail.com'
	gmail_password = 'ProjectExhibition@2'
	sent_from = gmail_user
#for speech input we would invoke takecommand function from virtual.py file
	#to=takeCommand()
	speak("Please type email address")	
	to = input("To: ")
	speak("tell me the subject and press enter when done")
	subject=takeCommand()
	#subject = input("Sub: ")
	speak("tell me the content of the mail and press enter when done")
	body=takeCommand()
	#body = input("Body: ")

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, to, subject, body)

	try:
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(gmail_user, gmail_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()
	    print('Email sent!')
	except:
	    print('Something went wrong...')
