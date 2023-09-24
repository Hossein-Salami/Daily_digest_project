import smtplib, json
from email.message import EmailMessage # for a simple text email
from email.mime.text import MIMEText # for html formatted email
import f_content

class DailyEmail():

    def __init__(self):
        self.content = {
                         'weather': f_content.retrive_forecast()
                        }
        self.recipient = [
                            'x@x.com'
                         ]
        
        with open('credentials', 'r') as f:
            self.sender_credentials = json.load(f)

    def email_content_prep(self):
        """
        A method that prepares the daily email that to be sent. The method uses attribute
        content to get the information needed and format an email
        """
        # daily digest info to be included in the email
        information_weather = self.content['weather']

        # HTML backbone for the email format
        email_html = f"""
        <html>
        <head>
            <title> </title>
        </head>

        <body>

            <header>
                <h1> Good Morning My Friend! </h1>
                <p> Here is all you need to know to start a great day! </p>
            </header>

            <section>
                <h2> Weather forecast </h2>
                <p> The weather forecast for the next 24 hours is {self.content['weather']} </p>
            </section>

        </body>

        </html>
        """

        return email_html

    def send_email(self):
        email_html = self.email_content_prep()

        
        msg = MIMEText(email_html, 'html')
        msg["From"] = self.sender_credentials['email']
        msg["To"] = self.recipient[0]
        msg["Subject"] = 'Good Morning App! :)'

        # for a text-based email
        #msg = EmailMessage()
        #msg.set_content(email_html)

        with smtplib.SMTP("smtp.mail.x.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(self.sender_credentials['email'],
                         self.sender_credentials['password'])
            server.send_message(msg)
            server.quit()


############################################# test
if __name__ == "__main__":
    test_email = DailyEmail()
    test_email.send_email()

    with open('test_email.html', 'w') as f:
        f.write(test_email.email_content_prep())


