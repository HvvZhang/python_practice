# -*- coding: utf-8 -*-
#将激活码存入sqlite数据库中

import sqlite3
import activation_key
# 创建数据库
conn = sqlite3.connect('keys.db')
# 创建游标
curs = conn.cursor()
# 建立表
creat_table = '''create table if not exists keys(
            id  INT PRIMARY KEY,
            key TEXT)'''

curs.execute(creat_table)

# 插入数据
i=0;
for key in activation_key.keys1:
    
    curs.execute('''insert into keys
                    (id, key)
                    values
                    (?, ?)''',(i, key))
    i+=1

# 查询数据
query = "select * from keys"
curs.execute(query)
rows = curs.fetchall()

for row in rows:
    print(" ",row)
    
curs.close()
conn.close()
