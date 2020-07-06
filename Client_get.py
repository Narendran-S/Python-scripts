import http.client
conn=http.client.HTTPSConnection("www.uci.edu")
conn.request("GET","/")
re=conn.getresponse()
print(re.status,re.reason)
print(re.readlines(300))
conn.close()