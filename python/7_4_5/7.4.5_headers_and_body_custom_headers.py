import requests


'''
requests you make to a url typically contain a user-agent
especially on the web to identify the browser you are using
'''

# original with normal request, will identify it as python-requests/2.25.1
response = requests.get('https://httpbin.test')



# Example 1 - being Firefox
headers = {
    'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
}
response = requests.get('https://httpbin.test/news-page', headers=headers)

# Example 2 - being Googlebot
headers['User-Agent'] = 'Googlebot/2.1 (+http://www.google.com/bot.html)'
response = requests.get('https://httpbin.test/restricted-article', headers=headers)

# Example 3 - being something else
headers['User-Agent'] = 'PickleBrowser/1.337'
response = requests.get('https://httpbin.test/admin/login', headers=headers)
