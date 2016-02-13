#!/usr/bin/python3
#-*- coding: utf-8 -*-

__author__ = 'a2zh'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# Settings
from_addr = None
from_name = None

password = None

to_addr = None
to_name = None

smtp_server = None
smtp_port = None

subject = None
message = None

def _format_addr(name, addr):
    return formataddr((Header(name, 'utf-8').encode(), addr))

msg = MIMEText(message, 'plain', 'utf-8')
msg['From'] = _format_addr(from_name, from_addr)
msg['To'] = _format_addr(to_name, to_addr)
msg['Subject'] = Header(subject, 'utf-8').encode()


server = smtplib.SMTP(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
