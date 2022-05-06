import smtplib
from email.message import EmailMessage

# content
sender = ""
reciever = "vineethnreddy@gmail.com "
password = ""
msg_body = 'Your product has reached its alert price url - https://www.amazon.in/Samsung-23-5-inch-Curved-Monitor/dp/B01GFPGHSM/ref=lp_1375425031_1_2?smid=A14CZOWI0VEHLG&th=1'


# action
msg = EmailMessage()
msg['subject'] = 'price alert'   
msg['from'] = sender
msg['to'] = reciever
msg.set_content(msg_body)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender,password)
    
    smtp.send_message(msg)

