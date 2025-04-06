import smtplib as smpt;

from email.mime.text import MIMEText

# Email credentials
sender_email = "hamzaraheem06@gmail.com"
receiver_email = "hraheem.bsds24seecs@seecs.edu.pk"
password = "03361520834hamza"

# Email content
subject = "MSE exam tommorrow"
body = "Dear Hamza!\nThis email is sent to remind you that you have a MSE of the course MATH-234: Multivariable Calculus. Please make sure to cover all the topics and revise all the concepts before 12:00 tomorrow. \nWe wish you a very best in your exams."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Sending email
try:
    with smpt.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)