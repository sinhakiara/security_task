#!/usr/bin/python3
import argparse
import requests
import os
import subprocess as mk
parser = argparse.ArgumentParser(description="check URL is accessible")
parser.add_argument("-apk", type=str, help="enter apk to check avilability", required=True)
l = parser.parse_args()

p = mk.getoutput("strings {} | egrep -o 'https\:\/\/(.*).firebaseio.com'".format(l.apk))

u = "/.json"
h = p + u
r=requests.get(h)
code=r.status_code

if code == 200:
    a = 1
else:
    a = 0

payload = {'name':'Mr. X','text':'blablabla'}
r=requests.put(h, data=payload)
c=r.status_code

if (c == 200 or c == 201):
    b = 1
else:
    b = 0

if (a == 1 and b == 1):
     print("readable and Writable")
elif (a == 1 and b == 0):
    print("only Readable")
elif (a == 0 and b ==1):
    print("only Writable")
else:
    print("nothing")
