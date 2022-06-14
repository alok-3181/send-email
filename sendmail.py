import smtplib
import time
import re
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

from datetime import datetime, timedelta
D1 = datetime.today()
Date = D1.strftime("%m-%d-%Y %H:%M")
 
fromaddr = "user1@company.com"
toaddr = "user@company.com"


msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Load Balancer mapping"
 
body = "Run date is " + str(Date)
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "combine_export.xls"
attachment = open("/root/Load_balancer/combine_export.xls", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.company.com')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
