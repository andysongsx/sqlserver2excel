import pandas as pd
import os,pymssql
import time
import re
print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

sql = "SELECT   *  FROM a"
conn = pymssql.connect(host="xxx", port='123', user="aaa", password="aaa", database="aaa", charset='utf8')
df0 = pd.read_sql(sql,conn)
df=pd.DataFrame(df0)
writer=pd.ExcelWriter("test2.xlsx", engine='xlsxwriter')
df.to_excel(writer,"ttt")
writer.save()

print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
