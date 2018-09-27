# -*- coding: utf-8 -*-
# @Author: susanoo
# @Date:   2018-09-26 14:22:25
# @Last Modified by:   susanoo
# @Last Modified time: 2018-09-26 17:35:33

from bs4 import BeautifulSoup
import requests
import xlwt

wbk = xlwt.Workbook()
linenum = 0

sheet = wbk.add_sheet('igxe item list')

url = 'https://www.igxe.cn/pubg/578080?page_no='

for i in range(12):
	# print(url + str(i+1))
	r = requests.get(url + str(i+1))

	soup = BeautifulSoup(r.text, "lxml")

	tag = soup.find_all("a", "single csgo")

	for key in tag:
		itemName = key.find("div", "name").text
		itemAmount = key.find("div", "sum fr").text
		itemPrice = key.find("span").text + key.find("sub").text
		sheet.write(linenum, 1, itemName)
		sheet.write(linenum, 2, itemPrice)
		sheet.write(linenum, 3, itemAmount)
		linenum = linenum + 1
		print(' | ' + itemName + ' | ' + itemPrice + ' | ' + itemAmount + '\n')
	# print('The Price is: ' + itemPrice)
	# print(itemAmount + '\n')

	wbk.save('igxe.xls')
# print(tag)

