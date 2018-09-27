# -*- coding: utf-8 -*-
# @Author: Tabsusanoo
# @Date:   2018-09-24 17:01:50
# @Last Modified by:   Tabsusanoo
# @Last Modified time: 2018-09-24 17:21:33

import requests

payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
url = 'https://susanoo.me'
headers = {'user-agent': 'my-app/0.0.1'}

# r = requests.get('https://susanoo.me', params = payload)
r = requests.get(url, headers = headers, timeout = 0.1)

print(r.url)
# print(r.content)
# print(r.json)
print(r.status_code)
# print(r.headers)
print(r.cookies)
