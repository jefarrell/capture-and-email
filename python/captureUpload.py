import smtplib, os, email, re, sys, glob, string, time, datetime
from subprocess import call
import subprocess as sp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import assets

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



####  GMAIL WORKING  ####
# GMAIL_USERNAME = assets.user
# GMAIL_PWD = assets.pwd
# recipients = assets.recipients
# email_subject = "test"
# body_of_email = "working"

# session = smtplib.SMTP('smtp.gmail.com', 587)
# session.ehlo()
# session.starttls()
# session.login(GMAIL_USERNAME, GMAIL_PWD)
# print("logged in")

# ####  COMPILE AND SEND EMAIL  ####
# headers = "\r\n".join(["from: " + GMAIL_USERNAME,
# 	"subject: " + email_subject,
# 	"to : " + recipients,
# 	"attachments: " + '/out.mp4',
# 	"mime-version: 1.0",
# 	"content-type: text/html"])

# content = headers + "\r\n\r\n" + body_of_email
# print("compiled")
# session.sendmail(GMAIL_USERNAME, recipients, content)
# print("sent")




attachmentname = 'h92yr.gif'
username = assets.user
password = assets.pwd
fromaddr = assets.user
toaddr  = assets.recipients


msgsubject = 'Here is another subject'

htmlmsgtext = """EMAIL BODY in HTML<br/>
                Yup. Yup. Yup.</br>
                <b>Done!</a>"""

try:

    msgtext = htmlmsgtext.replace('<b>','').replace('</b>','').replace('<br>',"\r").replace('</br>',"\r").replace('<br/>',"\r").replace('</a>','')
    msgtext = re.sub('<.*?>','',msgtext)

    msg = MIMEMultipart()
    msg.preamble = 'This is a multi-part message in MIME format.\n'
    msg.epilogue = ''

    body = MIMEMultipart('alternative')
    body.attach(MIMEText(msgtext))
    body.attach(MIMEText(htmlmsgtext, 'html'))
    msg.attach(body)

    # Is there an attachment?
    if 'attachmentname' in globals(): 
        f = attachmentname
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    msg.add_header('From', fromaddr)
    msg.add_header('To', toaddr)
    msg.add_header('Subject', msgsubject)

    # Login and send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.set_debuglevel(True) 
    server.starttls()
    server.login(username,password)
    server.sendmail(msg['From'], [msg['To']], msg.as_string())

    server.quit() 




except:
    print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', str(toaddr), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )







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


