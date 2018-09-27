# -*- coding: utf-8 -*-
# @Author: Tabsusanoo
# @Date:   2018-09-24 17:50:47
# @Last Modified by:   susanoo
# @Last Modified time: 2018-09-26 14:18:27

from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.igxe.cn/login/?path=/'

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
# tag = soup.find_all(name='csrfmiddlewaretoken')
# tag = soup.find_all("input")
tag = soup.find_all(type='hidden')
# tag = soup.find(text=re.compile(""))

for key in tag:
	if key.get('name') == 'captcha_id':
		# print(key.attrs)
		form_captcha = key.get('value')
		pass
	elif key.get('name') == 'csrfmiddlewaretoken':
		# print(key.attrs)
		form_xsrf = key.get('value')
		pass
	# print(key.attrs)
# print(tag.attrs)
# print(r.headers)
# print(r.cookies)
print('THE_CAPTCHA_ID IS: ', form_captcha)
print('THE_XSRF_ID IS: ', form_xsrf)

# Login part
login_data = {
	'csrfmiddlewaretoken': form_xsrf,
	'captcha_id': form_captcha,
	'username': 'jhhjdeoahoi',
	'password': 'pomquj-3jiwto-vabbIv',
	'check-user-pro': 'on',
	'path': '/'
}
# Set the header data
headers_base = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'www.igxe.cn',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
	'Referer': 'https://www.igxe.cn/user_login',
	'Upgrade-Insecure-Requests': '1',
	'Cookie': 'aliyungf_tc=AQAAAMCJ+3FMtgwAToaWtiqG3VrJucO8; sessionid=5cagqa423wi18ju3wr7xugirp58xayyy; __cfduid=d6ef53675cd0c3710dd47ae3a745479521537783381; _ga=GA1.2.395719460.1537783383; _gid=GA1.2.1968698915.1537783383; Hm_lvt_fe0238ac0617c14d9763a2776288b64b=1537783383; csrftoken=' + form_xsrf + '; myDateMinutes=5; _gat=1; Hm_lpvt_fe0238ac0617c14d9763a2776288b64b=1537786385'
}
# Use session to login
session = requests.Session()
content = session.post(url, headers = headers_base, data = login_data)
print(content.text)
