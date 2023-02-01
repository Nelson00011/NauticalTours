# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))

fname = "John"
lname = "Doe"
from_email = Email("nelson@oakhalo.com")
user = To("aylanelson01@gmail.com")
company = To("nelson@oakhalo.com")
subject = "Confirmation Email: Nautical Tours"

#email to internal
content = Content("text/plain", f"User Submission Here: from {fname} {lname}. Email :{from_email}")
mail = Mail(from_email, company, subject, content)

#email to individual
confirmation =  Content("text/plain", "Thank you for contacting us, we will get back to you shortly.")
confirmation_email = Mail(from_email, user, subject, confirmation)

response = sg.client.mail.send.post(request_body=mail.get())
response = sg.client.mail.send.post(request_body=confirmation_email.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)