import smtplib
from email.message import EmailMessage

def test_alert_me(email_reciever,url):
    sender = "supriyaesham@gmail.com"
    reciever = email_reciever
    password = "esham123"
    msg_body = 'Your product has reached its alert price url - ' + url
    msg = EmailMessage()
    msg['subject'] = 'price alert'   
    msg['from'] = sender
    msg['to'] = reciever
    msg.set_content(msg_body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)

