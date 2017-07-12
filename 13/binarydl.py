#!/usr/bin/env python
# Binary download - Chapter 13 - binarydl.py

from ftplib import FTP

f = FTP('ftp.kernel.org')
f.login()

f.cwd('/pub/linix/kernel/v1.0')
fd = open('patch8.gz', 'wb')
f.retrbinary('RETR patch8.gz', fd.write)
fd.close()

f.quit()