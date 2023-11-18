from flask import Flask, render_template, request
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)

def send_email(email_sender, email_receiver, subject, body):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, 'your_password')  # Replace 'your_password' with your actual Gmail password
        smtp.sendmail(email_sender, email_receiver, em.as_string())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send_email", methods=["POST"])
def trigger_email():
    email_sender = request.form["email_sender"]
    email_receiver = request.form["email_receiver"]
    subject = request.form["subject"]
    body = request.form["body"]

    send_email(email_sender, email_receiver, subject, body)
    return "Email sent successfully!"

if __name__ == "__main__":
    app.run(debug=True)
