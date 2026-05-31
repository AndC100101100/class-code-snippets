import requests
import json


res = requests.get("https://sans-foundations.com")
#print(res.headers)
print(json.dumps(res.json(), indent=4))

