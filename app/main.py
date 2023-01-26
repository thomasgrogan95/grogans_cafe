from flask import Flask, render_template, url_for, request, make_response 

from werkzeug.datastructures import ImmutableMultiDict

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

app = Flask(__name__)

HOST_NAME = "localhost"
HOST_PORT = 80
MAIL_FROM = "sys@site.com"
MAIL_TO = "thomasgrogan95@gmail.com"
MAIL_SUBJECT = "Contact Form"

@app.route('/')
def home():
    returnData = {}
    returnData['Title'] = "Grogan's Café and Ice Cream Parlour"
    return render_template('index.html', **returnData)

# (C3) SEND CONTACT FORM
@app.route("/send", methods=["POST"])
def foo():
  # EMAIL HEADERS
  mail = MIMEMultipart("alternative")
  mail["Subject"] = MAIL_SUBJECT
  mail["From"] = MAIL_FROM
  mail["To"] = MAIL_TO
 
  # EMAIL BODY (BOOKING DATA)
  data = dict(request.form)
  msg = "<html><head></head><body>"
  for key, value in data.items():
    msg += key + " : " + value + "<br>"
    msg += "</body></html>"
    mail.attach(MIMEText(msg, "html"))
 
  # SEND MAIL
  mailer = smtplib.SMTP("localhost")
  mailer.sendmail(MAIL_FROM, MAIL_TO, mail.as_string())
  mailer.quit()
 
  # HTTP RESPONSE
  res = make_response("OK", 200)
  return res 

if __name__ == "__main__":
    app.run(HOST_NAME, HOST_PORT, debug=True)