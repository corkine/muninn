#/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys,datetime
import convert
import fatch_data
temperr, tempout = sys.stderr, sys.stdout
#此处的Log不能放在Git文件夹内。
#对于正式部署，需要有相关库的访问权限，有jupyter convent的快捷命令行，
# 安装以下包：lxml，BeautifulSoup4
# sys.stderr = sys.stdout = open("/root/.jupyter/muninn/muninn_server.log","a+")
print("\n"+"="*30+"%s"%str(datetime.datetime.today()),"="*30)
fatch_data.main(update_data=True,file_path="muninn_last.data")
print("正在上传至Github服务器")
convert.submit()
