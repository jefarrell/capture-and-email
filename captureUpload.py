from subprocess import call
import time
import smtplib
import pyscreenshot as ImageGrab
import assets


####  GMAIL SMTP LOGIN  ####
GMAIL_USERNAME = assets.user
GMAIL_PWD = assets.pwd
recipients = assets.recipients
email_subject = "testing"
body_of_email = "did the body work?"

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login(GMAIL_USERNAME, GMAIL_PWD)


####  TAKE SCREENSHOTS  ####
def screenshot():
	for i in range(1):
		print(i)
		#call(['screencapture','-x','test',str(i),'.png'])
		#ImageGrab.grab_to_file('img'+str(i)+'.png')
		time.sleep(5)

while True:
	screenshot()

####  COMPILE AND SEND EMAIL  ####
headers = "\r\n".join(["from: " + GMAIL_USERNAME,
	"subject: " + email_subject,
	"to : " + recipients,
	"mime-version: 1.0",
	"content-type: text/html"])

content = headers + "\r\n\r\n" + body_of_email
session.sendmail(GMAIL_USERNAME, recipients, content)