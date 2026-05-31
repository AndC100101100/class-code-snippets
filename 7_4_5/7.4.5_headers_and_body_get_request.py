import requests

payload = {'key1': 'value1', 'key2': 'value2'}
# when making a request Python will take our provided GET data and 
# apply it as parameters to the URL its requesting in the typical query string
# format, we should see something like > https://sans-foundations.com/?key1=value1&key2=value2
res = requests.get("https://sans-foundation.com", params=payload) 
print(res.url)
