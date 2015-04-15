from subprocess import call
import subprocess as sp
import time
import smtplib
import pyscreenshot as ImageGrab
import assets
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
FFMPEG_BIN = "ffmpeg"



command = [ FFMPEG_BIN,
'-framerate',
'1/5', 
'-pattern_type',
'glob',
'-i',
'*.png',
'-c:v', 
'libx264',
'-pix_fmt',
'yuv420p',
'-y',
'out.mp4']

timestamp = time.strftime("%H:%M:%S")

####  TAKE SCREENSHOTS  ####
def screenshot():
	for i in range(2):
		file = 'img00000' + str(i) + '.png'
		print(file)
		#call(['screencapture','-x','test',str(i),'.png'])
		#ImageGrab.grab_to_file('img'+str(i)+'.png')
		# im = ImageGrab.grab()
		# im.save('img'+str(i)+'.png',format=None)
		os.system("screencapture -t png " + file)
		time.sleep(3)
	call(command)


screenshot()




####  GMAIL SMTP LOGIN  ####
GMAIL_USERNAME = assets.user
GMAIL_PWD = assets.pwd
recipients = assets.recipients
email_subject = "testing"
body_of_email = "did the body work?"
file_path = 'out.mp4'

msg = MIMEMultipart()
msg.attach(MIMEText(body_of_email))
part = MIMEBase('application', "octet-stream")
fo = open(file_path,'rb')
part.set_payload(fo.read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
msg.attach(part)

mailer = smtplib.SMTP('smtp.gmail.com', 587)
mailer.ehlo()
mailer.starttls()
mailer.login(GMAIL_USERNAME,GMAIL_PWD)
sent = mailer.sendmail(GMAIL_USERNAME, recipients, msg.as_string())
mailer.close





# session = smtplib.SMTP('smtp.gmail.com', 587)
# session.ehlo()
# session.starttls()
# session.login(GMAIL_USERNAME, GMAIL_PWD)

# ####  COMPILE AND SEND EMAIL  ####
# headers = "\r\n".join(["from: " + GMAIL_USERNAME,
# 	"subject: " + email_subject,
# 	"to : " + recipients,
# 	"attachments: " + '/out.mp4',
# 	"mime-version: 1.0",
# 	"content-type: text/html"])

# content = headers + "\r\n\r\n" + body_of_email
# session.sendmail(GMAIL_USERNAME, recipients, content)











# ####  TAKE SCREENSHOTS  ####
# def screenshot():
# 	for i in range(3):
# 		file = 'test'+str(i)+'.png'
# 		print(i)
# 		#call(['screencapture','-x','test',str(i),'.png'])
# 		#ImageGrab.grab_to_file('img'+str(i)+'.png')
# 		# im = ImageGrab.grab()
# 		# im.save('img'+str(i)+'.png',format=None)
# 		#os.system("screencapture -t png " + file)
# 		time.sleep(5)

# while True:
# 	screenshot()


