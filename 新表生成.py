import sqlite3
import os
import re
import shutil
con = sqlite3.connect("./base/single.db")
cur = con.cursor()

# 获取文件名
file_list = os.listdir(".")
my_list = list(filter(lambda x: re.match('.*txt', x) != None, file_list))


def py_cf(txt_name):
    # 初始化『new_table』为『wb98.txt』
    new_table = open('./TEXT/wb98.txt', "w", encoding='utf-8')
    new_table.close()
    # 写入正文
    new_table = open('./TEXT/wb98.txt', "a", encoding='utf-8')
    rd = open(txt_name, "r", encoding='utf-8')
    while True:
        a = rd.readline().strip()
        if a == "":
            break
        cut_line = a.split('\t', 2)
        codes = cut_line[1].split()
        #print("拿到了：%s"% codes)
        new_table.write('\n' + cut_line[0] + '\t')
        for key in codes:
            #print("key is : %s"% key )
            for word in key:
                cur.execute(
                    "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" % word)
                b = cur.fetchone()
                new_table.write(str(b[0]))
            new_table.write(' ')
        new_table.write('\t' + str(cut_line[2]))
    new_table.close()
    rd.close()


def ci_cf(txt_name):
    # 初始化『new_table』为『ci.txt』
    new_table = open('./TEXT/ci.txt', "w", encoding='utf-8')
    new_table.close()
    # 写入正文
    new_table = open('./TEXT/ci.txt', "a", encoding='utf-8')
    rd = open(txt_name, "r", encoding='utf-8')
    while True:
        a = rd.readline().strip()
        if a == "":
            break
        cut_line = a.split('\t')
        if len(cut_line) == 3:
            #print("当前切片 is : %s"% cut_line )
            codes = cut_line[1].split()
            #print("拿到了：%s"% codes)
            new_table.write('\n' + cut_line[0] + '\t')
            for key in codes:
                #print("key is : %s"% key )
                for word in key:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        word)
                    b = cur.fetchone()
                    new_table.write(str(b[0]))
            new_table.write('\t' + str(cut_line[2]))
        if len(cut_line) == 4:
            #print("当前切片 is : %s"% cut_line )
            codes = cut_line[1].split()
            #print("拿到了：%s"% codes)
            new_table.write('\n' + cut_line[0] + '\t')
            for key in codes:
                #print("key is : %s"% key )
                for word in key:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        word)
                    b = cur.fetchone()
                    new_table.write(str(b[0]))
            new_table.write('\t' + str(cut_line[2]) + '\t')
            rk = cut_line[3].strip()
            #print("拿到了全码：%s"% rk)
            for rk_w in rk:
                #print("rk_w is : %s"% rk_w )
                for kword in rk_w:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        kword)
                    bk = cur.fetchone()
                    new_table.write(str(bk[0]))
    new_table.close()
    rd.close()


def u_cf(txt_name):
    # 初始化『new_table』为『U.txt』
    new_table = open('./TEXT/U.txt', "w", encoding='utf-8')
    new_table.close()
    # 写入正文
    new_table = open('./TEXT/U.txt', "a", encoding='utf-8')
    rd = open(txt_name, "r", encoding='utf-8')
    while True:
        a = rd.readline().strip()
        if a == "":
            break
        cut_line = a.split('\t')
        if len(cut_line) == 2:
            #print("当前切片数为2，它们是: %s"% cut_line )
            codes = cut_line[1].split()
            #print("拿到了：%s"% codes)
            new_table.write('\n' + cut_line[0] + '\t')
            for key in codes:
                #print("key is : %s"% key )
                for word in key:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        word)
                    b = cur.fetchone()
                    new_table.write(str(b[0]))
        if len(cut_line) == 3:
            #print("当前切片 is : %s"% cut_line )
            codes = cut_line[1].split()
            #print("拿到了：%s"% codes)
            new_table.write('\n' + cut_line[0] + '\t')
            for key in codes:
                #print("key is : %s"% key )
                for word in key:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        word)
                    b = cur.fetchone()
                    new_table.write(str(b[0]))
            new_table.write('\t' + str(cut_line[2]))
        if len(cut_line) == 4:
            #print("当前切片 is : %s"% cut_line )
            codes = cut_line[1].split()
            #print("拿到了：%s"% codes)
            new_table.write('\n' + cut_line[0] + '\t')
            for key in codes:
                #print("key is : %s"% key )
                for word in key:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        word)
                    b = cur.fetchone()
                    new_table.write(str(b[0]))
            new_table.write('\t' + str(cut_line[2]) + '\t')
            rk = cut_line[3].strip()
            #print("拿到了全码：%s"% rk)
            for rk_w in rk:
                #print("rk_w is : %s"% rk_w )
                for kword in rk_w:
                    cur.execute(
                        "SELECT A_key FROM sing_dic WHERE aim_chars = '%s'" %
                        kword)
                    bk = cur.fetchone()
                    new_table.write(str(bk[0]))
    new_table.close()
    rd.close()


for list_n in my_list:
    #print("当前是：%s"% list_n)
    if list_n == 'py.txt':
        py_cf(list_n)
        # 改格式
        new_table = open('./TEXT/py.txt', "w", encoding='utf-8')
        new_table.close()
        new_table = open('./TEXT/py.txt', "w", encoding='utf-8')
        rd_conf = open('./TEXT/wb98.txt', "r", encoding='utf-8')
        while True:
            conf_line = rd_conf.readline()
            py_line = conf_line.strip().split('\t')
            if len(py_line) == 1:
                new_table.write('')
            else:
                new_table.write(py_line[0] + '\t' + py_line[1].strip() + '\t' +
                                py_line[2] + '\n')
            if conf_line == "":
                break
        rd_conf.close()
        new_table.close()
        # 拼音表生成
        # 写表头
        # 写入表头
        py_table = open('./TEXT/new_py.txt', "w", encoding='utf-8')
        py_conf = open('./base/added/title-dict3.txt', "r", encoding='utf-8')
        while True:
            conf_line = py_conf.readline()
            py_table.write(conf_line)
            if conf_line == "":
                break
        py_conf.close()
        py_table.close()
        # 写正文
        py_table = open('./TEXT/new_py.txt', "a", encoding='utf-8')
        py_cont = open('./TEXT/py.txt', "r", encoding='utf-8')
        while True:
            conf_line = py_cont.readline()
            py_table.write(conf_line)
            if conf_line == "":
                break
        py_cont.close()
        py_table.close()
        os.rename('./TEXT/new_py.txt', './new-tables/py.dict.yaml')
    elif list_n == 'wubi98_ci.txt':
        ci_cf(list_n)
        # 含词表生成
        # 写表头
        # 写入表头
        ci_table = open('./TEXT/new_ci.txt', "w", encoding='utf-8')
        ci_conf = open('./base/added/title-dict.txt', "r", encoding='utf-8')
        while True:
            conf_line = ci_conf.readline()
            ci_table.write(conf_line)
            if conf_line == "":
                break
        ci_conf.close()
        ci_table.close()
        # 写正文
        ci_table = open('./TEXT/new_ci.txt', "a", encoding='utf-8')
        ci_cont = open('./TEXT/ci.txt', "r", encoding='utf-8')
        while True:
            conf_line = ci_cont.readline()
            ci_table.write(conf_line)
            if conf_line == "":
                break
        ci_cont.close()
        ci_table.close()
        # 写表尾
        # 写入表尾
        ci_table = open('./TEXT/new_ci.txt', "a", encoding='utf-8')
        rd_tail = open('./base/added/tail-dict.txt', "r", encoding='utf-8')
        while True:
            tail_line = rd_tail.readline()
            ci_table.write(tail_line)
            if tail_line == "":
                break
        rd_tail.close()
        ci_table.close()
        os.rename('./TEXT/new_ci.txt', './new-tables/wubi98_ci.dict.yaml')
    elif list_n == 'wubi98_U.txt':
        u_cf(list_n)
        u_table = open('./TEXT/new_u.txt', "w", encoding='utf-8')
        u_conf = open('./base/added/title-dict2.txt', "r", encoding='utf-8')
        while True:
            conf_line = u_conf.readline()
            u_table.write(conf_line)
            if conf_line == "":
                break
        u_conf.close()
        u_table.close()
        # 超集表生成
        # 写正文
        u_table = open('./TEXT/new_u.txt', "a", encoding='utf-8')
        u_cont = open('./TEXT/U.txt', "r", encoding='utf-8')
        while True:
            conf_line = u_cont.readline()
            u_table.write(conf_line)
            if conf_line == "":
                break
        u_cont.close()
        u_table.close()
        # 写表尾
        # 写入表尾
        u_table = open('./TEXT/new_u.txt', "a", encoding='utf-8')
        rd_tail = open('./base/added/tail-dict.txt', "r", encoding='utf-8')
        while True:
            tail_line = rd_tail.readline()
            u_table.write(tail_line)
            if tail_line == "":
                break
        rd_tail.close()
        u_table.close()
        os.rename('./TEXT/new_u.txt', './new-tables/wubi98_U.dict.yaml')
    else:
        print("请看使用说明")
cur.close()
con.close()
print("YAML表制作成功！")
