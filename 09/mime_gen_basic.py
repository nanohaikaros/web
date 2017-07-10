#!/usr/bin/env python
# MIME attachment generation - Chapter 9 - mime_gen_basic.py
# This program requires python 2.2.2 or above

from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import utils, Encoders
import mimetypes, sys

def attrachment(filename):
    fd = open(filename, 'rb')
    mimetype, mimeencoding = mimetypes.guess_type(filename)
    if mimeencoding or (mimetype is None):
        mimetype = 'application/octet-stream'
    maintype, subtype = mimetype.split('/')
    if maintype == 'text':
        retval = MIMEText(fd.read(), _subtype=subtype)
    else:
        retval = MIMEBase(maintype, subtype)
        retval.set_payload(fd.read())
        Encoders.encode_base64(retval)
    retval.add_header('Content-Disposition', 'attachment', filename=filename)
    fd.close()
    return retval

message = """Hello,

This is a test message from Chapter 9. I hope you enjiy it!

-- Anonymous"""

msg = MIMEMultipart()
msg['TO'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subject'] = 'Test Message, Chapter 9'
msg['Date'] = utils.formatdate(localtime=1)
msg['Message-ID'] = utils.make_msgid()

body = MIMEText(message, _subtype='plain')
msg.attach(body)
for filename in sys.argv[1]:
    msg.attach(attrachment(filename))
print msg.as_string()