import requests

res = requests.get("https://andc.dev")
#print(res.status_code)
#print(res.content) # this will return the bytes received, represented by the content being wrapped around b''

print(res.text) # if we do not want raw bytes but the actual formatted content
