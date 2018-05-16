#!/usr/bin/python3

import json
import cgi

fs = cgi.FieldStorage()

print("Content-Type: application/json")
print("\n")
print("\n")

result = {}
result['success'] = True
result['message'] = "Command completed"
result['keys']    = ",".join(fs.keys())

d = {}
for k in fs.keys():
	d[k] = fs.getvalue(k)
	
result['data'] = d

print(json.dumps(result, indent=1))
print("\n")