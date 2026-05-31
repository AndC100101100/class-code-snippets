import requests
import json

res = requests.get("https://api.site.test/users/octodog")
print(json.dumps(res.json(), indent=4))

# we could specify the exact data to get within the json object:

print("long name: " + res.json()["name"])
