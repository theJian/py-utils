#!/usr/bin/python3
#-*- coding: utf-8 -*-

__author__ = 'a2zh'

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = 'tangsmail@yeah.net'
password = 'Jian.yeah.0505'
pop3_server = 'pop.yeah.net'
pop3_port = '110'

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
        else:
            charset = 'utf-8'
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_email(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % (' ' * indent, header, value))
    if msg.is_multipart():
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % (' ' * indent, n))
            print('%s-----------------' % (' ' * indent))
            print_email(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            print('******** charset: %s *********' % charset)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))

server = poplib.POP3(pop3_server, pop3_port)
server.set_debuglevel(1)

server.user(email)
server.pass_(password)

print('Messages: %s, Size: %s' % server.stat())
resp, mails, octets = server.list()
# print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
print_email(msg)

server.quit()
