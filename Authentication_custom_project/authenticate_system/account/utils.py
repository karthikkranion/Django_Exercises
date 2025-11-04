import threading
from django.core.mail import EmailMultiAlternatives # type: ignore
from django.utils.html import strip_tags# type: ignore
from django.template.loader import render_to_string # type: ignore
from django.conf import settings# type: ignore


class SendEmailThread(threading.Thread):
    def __init__(self,email):
        self.email=email
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.email.send()
        except Exception as e:
            print("EMAIL SEND ERROR:", e)

def send_activation_email(recipient_email,activation_url):
    subject='your actiavtion link sent via mail check it'
    from_email = 'noreply@example.com'

    to_email=[recipient_email]

    #load html template
    html_content=render_to_string('account/activation_email.html',{'activation_url':activation_url})
    text_content=strip_tags(html_content)

    email=EmailMultiAlternatives(subject,text_content,from_email,to_email)
    email.attach_alternative(html_content,'text/html')
    SendEmailThread(email).start()

def reset_password_email(recipient_email,reset_url):
    subject='your reset link sent via mail check it'+settings.SITE_DOMAIN
    from_email = 'noreply@example.com'

    to_email=[recipient_email]

    #load html template
    html_content=render_to_string('account/reset_password.html',{'reset_url':reset_url})
    text_content=strip_tags(html_content)

    email=EmailMultiAlternatives(subject,text_content,from_email,to_email)
    email.attach_alternative(html_content,'text/html')
    SendEmailThread(email).start()