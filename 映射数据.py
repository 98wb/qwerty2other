# 导入数据库模块并初始化
import sqlite3

con = sqlite3.connect("./base/single.db")
cur = con.cursor()
cur.execute("create table if not exists sing_dic(aim_chars primary key,A_key)")
cur.execute("delete from sing_dic")

txt_name = "./base/MAPPING.txt"

def rd_cont(txt_name):
     rd = open(txt_name, "r",encoding='utf-8')
     while True:
         txt_cont = rd.readline().rstrip()
         if txt_cont == "":
             break
         cut_line = txt_cont.split('\t',1)
         cur.execute("insert into sing_dic values(?,?)", (cut_line[0], cut_line[1]))
#        print("录入：%s ~ %s" %(cut_line[0], cut_line[1]) )
         con.commit()
     rd.close()
     return
# 执行从 TXT 到 SQLite 的转存
rd_cont(txt_name)
print("做完了")

# 关闭 SQLite 接口
cur.close()
con.close()
