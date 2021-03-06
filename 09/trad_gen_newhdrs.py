#!/usr/bin/env python
# Traditional Message Generation with Date and Message-ID -- Chapter 9
# trad_gen_bewhdrs.py
# This program requires python 2.2.2 or above

from email.MIMEText import MIMEText
from email import utils
message = """Hello,

This is a test message from Chapter 9. I hope you enjoy it!

-- Anonymous"""

msg = MIMEText(message)
msg['TO'] = 'recipient@example.com'
msg['From'] = 'Test Sender <sender@example.com>'
msg['Subhect'] = 'Test Message, Chapter 9'
msg['Date'] = utils.make_msgid()

print msg.as_string()