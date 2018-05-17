#!/usr/bin/python3

import cgi
import pymysql
import json

form = cgi.FieldStorage()

lastName = form.getvalue("lastName")
firstName = form.getvalue("firstName")

print("Content-Type: application/json")
print("\n")
print("\n")

conn = pymysql.connect(
	db='example',
	user='root',
	passwd='KittyKat',
	host='localhost')

curs = conn.cursor()

curs.execute("INSERT INTO persons (FirstName, LastName) VALUES('{}', '{}');".format(firstName, lastName))
conn.commit()

result = {}
result['success'] = True
result['message'] = "Inserte into the database, maybe"

print(json.dumps(result, indent=1))
print("\n")