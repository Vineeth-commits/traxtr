import smtplib
from email.message import EmailMessage

# content
sender = ""
reciever = ""
password = ""
msg_body = 'test alert mail'


# action
msg = EmailMessage()
msg['subject'] = 'notify'   
msg['from'] = sender
msg['to'] = reciever
msg.set_content(msg_body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender,password)
    
    smtp.send_message(msg)

