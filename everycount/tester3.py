import smtplib, ssl
import requests
import json
import socket
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

start = time.perf_counter()

url = "https://embassy.goabroad.com/api/embassies?host_country_id=91&limit=986"
response = requests.get(url)
data = response.text
parsed = json.loads(data) 

for i in range(0,985): #def func and run with diff positional values a,b

    email = parsed['embassies'][i]['email']
    whom = parsed['embassies'][i]['title']

    sender_email = "ethansmitheron@gmail.com"
    receiver_email = "dylandagoat505@gmail.com" 
    password = 'atanqlrtwqhrlwfm'  

    message = MIMEMultipart("alternative")
    message["Subject"] = "Pin Collection"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f" Dear {whom},\n\nHope you are doing well!\n\nHello, I am Ethan and I am high school student.\n\nI have been collecting pins and flags of countries for the past 5 years.\n\nIt just so happens that one of the last pin I need is yours!\n\nMy address: 1871 Alemany Blvd, San Francisco CA 94112\n\nThanks,\n Ethan Smitheron"

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

    print("Email sent to: ",whom)
    print("Email number: ",i+1)

end = time.perf_counter()

print(f'Finished in {round(end-start,2)} seconds')


#raise SMTPServerDisconnected("Connection unexpectedly closed")
#smtplib.SMTPServerDisconnected: Connection unexpectedly closed