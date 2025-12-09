import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import jsonify

def send(data):
    sender_email="khetmitra26@gmail.com"
    reciver_email=data['to']
    message = data['text']

    msg=MIMEMultipart()
    msg['From']=sender_email
    msg['To']=reciver_email
    msg['Subject']="KhetMitra"
    msg.attach(MIMEText(message,'html'))
    try:

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email,'daes bhdo brkx vwci')
        server.sendmail(sender_email,reciver_email,msg.as_string())

        return {"status":"mail sent"}
    except Exception as e:
        return {"status":"mail not sent"}



