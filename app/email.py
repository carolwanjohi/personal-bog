from flask_mail import Message
from flask import render_template
from . import mail

subject_pref = 'the C blog'
sender_email = 'wanjohi.carol75@gmail.com'

def mail_message(subject,template,to,**kwargs):
    email = Message(subject_pref+subject,sender=sender_email,recipients= [user for user in to.split(',')])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)