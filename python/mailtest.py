#! /usr/bin/env python
import smtplib
import os,email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText

from email import Encoders
import assets

def send_mail(send_from, send_to, subject, text, file):
    
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = " Use any date time module to insert or use email.utils formatdate"
    msg['Subject'] = subject
    myemail = assets.user
    mypass = assets.pwd
    print myemail
    msg.attach( MIMEText(text) )
    part = MIMEBase('application', "octet-stream")
    fo=open(file,"rb")
    part.set_payload(fo.read() )
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(file))
    msg.attach(part)
    smtp = smtplib.SMTP()
    smtp.connect("smtp.gmail.com",465)
    smtp.ehlo()
    smtp.starttls
    smtp.ehlo()
    smtp.login(myemail, mypass)
    print "logged"
    sent=smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
    return sent
    

s=send_mail(assets.user,assets.recipients,"Mail test","Message",'out.mp4')
if (s.keys()==[]):
    print "Message Sent!!!!!!!!!"
else:
    print "Error!!!!"
