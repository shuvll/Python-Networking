import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Email number one:
#Setting up email that we are going to send to.
server = smtplib.SMTP('smtp.temp-mail.org', 25)

server.ehlo()

#Logging into that same email.
server.login('kalaya1942@hbehs.com', '')

#Creating what the email will contain and adding some formalities.
msg = MIMEMultipart()
msg['From'] = 'kalaya1942@hbehs.com'
msg['To'] = 'kalaya1942@hbehs.com'
msg["subject"] = 'Just A Test'

#Opening the text message that will be in the body of the email.
with open('message.txt', 'r') as f:
    message = f.read()

#Setting the message as the text, making sure its normal.
msg.attach(MIMEText(message, 'plain'))

#Setting up an image to be an attachment.
filename = 'coding.jpg'
attachment = open(filename, 'rb')

#Making sure the image is functional.
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

#Setting up the header and the attachment.
encoders.encode_base64
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

#Setting up the message as a string and sending it.
text = msg.as_string()
server.sendmail('kalaya1942@hbehs.com', 'kalaya1942@hbehs.com', text)

#Basically the same comments for the rest of the emails that we will be sending. Also, the email that was chosen is a spam email account.

#Email number two:
server = smtplib.SMTP('smtp.temp-mail.org', 25)

server.ehlo()

server.login('kalaya2001@hbehs.com', '')

msg = MIMEMultipart()
msg['From'] = 'kalaya2001@hbehs.com'
msg['To'] = 'kalaya2001@hbehs.com'
msg["subject"] = 'Just A Test'

with open('message_1.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('kalaya2001@hbehs.com', 'kalaya2001@hbehs.com', text)

#Email number three:
server = smtplib.SMTP('smtp.temp-mail.org', 25)

server.ehlo()

server.login('kalaya2022@hbehs.com', '')

msg = MIMEMultipart()
msg['From'] = 'kalaya2022@hbehs.com'
msg['To'] = 'kalaya2022@hbehs.com'
msg["subject"] = 'Just A Test'

with open('message_2.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('kalaya2022@hbehs.com', 'kalaya2022@hbehs.com', text)