#!/usr/bin/python3

import cgi
form = cgi.FieldStorage()

lastName = form.getvalue("lastName")
firstName = form.getvalue("firstName")

print("Content-Type: text/html; charset=utf-8\n\n")
print("<html>")
print("<head>")
print("<title>Get Information</title>")
print("</head>")
print("<body>")
print("<h1>Name is: {} {}</h1>".format(firstName, lastName))
print("</body>")
print("</html>")