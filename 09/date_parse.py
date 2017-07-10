#!/usr/bin/env python
# Date Parsing - Chapter 9 - date_parse.py
# This program requires python 2.2.2 or above

import sys, email, time
from email import utils

def getdate(msg):
    """Return the date/time from msg in seconds-since-epoch, if possible.
    Otherwise, return None."""

    if not 'date' in msg:
        # No Date header present.
        return None

    datehdr = msg['date'].strip()

    try:
        return utils.mktime_tz(utils.parsedate_tz(datehdr))
    except:
        # Some sort of error occured, likely because of an invalid date.
        return None

msg = email.message_from_file(sys.stdin)

dateval = getdate(msg)
if dateval is None:
    print "No valid date was found."
else:
    print "Message was sent on", time.strftime('%A, %B %d %Y at %I:%M %p', time.localtime(dateval))