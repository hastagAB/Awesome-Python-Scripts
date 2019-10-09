#!/bin/python   
# -*- coding: utf-8 -*-

# Using curl to get data from https://ipinfo.io/json
# Template from pycurl documentation
# http://pycurl.io/docs/latest/quickstart.html#examining-response-headers

import pycurl #curl library
import certifi #HTTP over TLS/SSL library
from io import BytesIO #Buffered I/O implementation using an in-memory bytes buffer.

#set header, '--header' or -H
header = ['Accept: application/json']

buffer = BytesIO()
c = pycurl.Curl() #curl
c.setopt(c.HTTPHEADER, header) #header
c.setopt(c.URL, 'https://ipinfo.io/json') #URL
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where()) # SSL certificates
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))