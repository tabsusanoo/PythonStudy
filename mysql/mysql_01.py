# -*- coding: utf-8 -*-
# @Author: susanoo
# @Date:   2018-09-26 16:50:56
# @Last Modified by:   susanoo
# @Last Modified time: 2018-09-26 17:09:30

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","susanoo","susanoo","ssfun" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()
