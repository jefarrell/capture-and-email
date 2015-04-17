#! /usr/bin/env python
import smtplib, os, email, re, sys, glob, string, time, datetime
from subprocess import call
import subprocess as sp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders
import assets

FFMPEG_BIN = "ffmpeg"
gif_title = "output.gif"

compileMovie = [ FFMPEG_BIN,
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
'output.mp4']

movie2gif = [ FFMPEG_BIN,
'-i',
'output.mp4',
'-vf',
'scale=720:-1',
'-t',
'10',
'-r',
'10',
'-y',
gif_title

]


####  TAKE SCREENSHOTS  ####
def screenshot():
	for i in range(2):
		file = 'img00000' + str(i) + '.png'
		print(file)
		os.system("screencapture -t png " + file)
		time.sleep(3)
	call(compileMovie)
	call(movie2gif)





####  SEND EMAIL  ####
def sendEmail(username, userPwd, toAddr, attachmentName, msgSubject):

	# Set your message
	htmlmsgtext = """EMAIL BODY in HTML<br/>
	                Yup. Yup. Yup.</br>
	                <b>Done!</a>"""

	try:

		# Format message
	    msgtext = htmlmsgtext.replace('<b>','').replace('</b>','').replace('<br>',"\r").replace('</br>',"\r").replace('<br/>',"\r").replace('</a>','')
	    msgtext = re.sub('<.*?>','',msgtext)

	    # MIME Encoding
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

	    msg.add_header('From', username)
	    msg.add_header('To', toAddr)
	    msg.add_header('Subject', msgSubject)

	    # Login and send
	    server = smtplib.SMTP('smtp.gmail.com:587')
	    server.set_debuglevel(True) 
	    server.starttls()
	    server.login(username,userPwd)
	    #server.sendmail(msg['From'], [msg['To']], msg.as_string())

	    server.quit() 

	except:
	    print ('Email NOT sent to %s successfully. %s ERR: %s %s %s ', str(toAddr), 'tete', str(sys.exc_info()[0]), str(sys.exc_info()[1]), str(sys.exc_info()[2]) )


screenshot()
sendEmail(assets.user, assets.pwd, assets.recipients, gif_title, 'test')


