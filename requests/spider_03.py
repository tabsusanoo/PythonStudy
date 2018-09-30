# -*- coding: utf-8 -*-
# @Author: susanoo
# @Date:   2018-09-26 14:22:25
# @Last Modified by:   Tabsusanoo
# @Last Modified time: 2018-09-27 17:31:01

from bs4 import BeautifulSoup
import requests
import xlwt
import time


def getData(urls):
	# 创建空的饰品集合列表
	returnData = []
	for url in urls:
		# 获取url集合里面的每个链接,分别爬取其中需要的数据
		r = requests.get(url)
		soup = BeautifulSoup(r.text, "lxml")
		tag = soup.find_all("a", "single csgo")
		# 获取到武器卡片的列表，遍历其中每个饰品，获取其中的饰品名称，价格及库存，将这三个属性保存到一个元祖当中，再将这个元祖保存到一个列表
		for key in tag:
			# 新建一个新的空列表用于存放单个饰品信息
			weapon = []
			itemName = key.find("div", "name").text
			itemAmount = key.find("div", "sum fr").text
			itemPrice = key.find("span").text + key.find("sub").text
			weapon.append(itemName)
			weapon.append(itemAmount)
			weapon.append(itemPrice)
			# 将完整的单个饰品信息添加到饰品集合中
			returnData.append(weapon)
	# 返回饰品集合
	return returnData

# creating igxeURLlist
igxeurllist = []
for i in range(12):
	igxeurllist.append('https://www.igxe.cn/pubg/578080?page_no='+str(i+1))

# 获取igxe中的名称数量及价格
igxelist = getData(igxeurllist)
# # to show igxe infos in my syntax
# for single in igxelist:
# 	print(single[0] + ' | ' + single[1] + ' | ' + single[2])
# 将饰品名称与网站链接拼接成steam市场的商品链接

steamurllist = []
for single in igxelist:
	url = 'https://steamcommunity.com/market/listings/578080/' + single[0]
	# print(url)
	steamurllist.append(url)

# print(steamurllist)

# for url in steamurllist:
p = {
	'http': 'socks5://127.0.0.1:1086',
	'https': 'socks5://127.0.0.1:1086'
}
r = requests.get('https://steamcommunity.com/market/listings/578080/Baggy%20Pants%20(Brown)', proxies = p)
soup = BeautifulSoup(r.text, "lxml")
buyfield = soup.get_text()
print(buyfield)
	# sellfield = soup.find_all("div", class_="market_commodity_orders_block")















# # creating steamURLlist
# steamurllist = []
# for i in range(29):
# 	steamurllist.append('https://steamcommunity.com/market/search?appid=578080#p' + str(i+1) + '_price_desc')

# # 创建空的饰品集合列表
# steamlist = []
# p = {
# 	'http': 'socks5://127.0.0.1:1086',
# 	'https': 'socks5://127.0.0.1:1086'
# }
# # r = requests.get('https://steamcommunity.com/market/search?appid=578080#p2_price_desc', proxies = p)
# # soup = BeautifulSoup(r.text, "lxml")
# # result = soup.find(id="result_0")
# # iName = soup.find(id="result_0_name").get_text()
# # iSto = ''
# # iPrice = ''
# # print(result.get_text())
# # print(r.text)

# # for url in steamurllist:
# # 	# 获取url集合里面的每个链接,分别爬取其中需要的数据
# # 	time.sleep(1)
# # 	r = requests.get(url)
# 	# soup = BeautifulSoup(r.text, "lxml")
# 	# tag = soup.find_all("a", "single csgo")
# 	# # 获取到武器卡片的列表，遍历其中每个饰品，获取其中的饰品名称，价格及库存，将这三个属性保存到一个元祖当中，再将这个元祖保存到一个列表
# 	# for key in tag:
# 	# 	# 新建一个新的空列表用于存放单个饰品信息
# 	# 	weapon = []
# 	# 	itemName = key.find("div", "name").text
# 	# 	itemAmount = key.find("div", "sum fr").text
# 	# 	itemPrice = key.find("span").text + key.find("sub").text
# 	# 	weapon.append(itemName)
# 	# 	weapon.append(itemAmount)
# 	# 	weapon.append(itemPrice)
# 	# 	# 将完整的单个饰品信息添加到饰品集合中
# 	# 	steamlist.append(weapon)
# 	# # 返回饰品集合




