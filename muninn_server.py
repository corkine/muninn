#/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys,datetime
import convert
import fatch_data
temperr, tempout = sys.stderr, sys.stdout
__version__ = "0.1.1"
__log__ = """
0.1.0 Alpha 上线测试
0.1.1 2018年6月18日 添加了 ‘explain’ 类型的笔记。给每个笔记添加了链接。解决了目录显示顺序随机的问题。
"""
#此处的Log不能放在Git文件夹内。
#对于正式部署，需要有相关库的访问权限，有jupyter convent的快捷命令行，
# 安装以下包：lxml，BeautifulSoup4
sys.stderr = sys.stdout = open("/root/.jupyter/muninn/muninn_server.log","a+")
print("\n"*3,"="*30,"...%s..."%str(datetime.datetime.today()),"="*30)
print("正在迁移 Jupyter Notebook 文件夹，并进行文件转换")
convert.get_file()
print("正在构建HTML文档...")
fatch_data.main(update_data=True,file_path="muninn_last.data")
print("正在上传至Github服务器")
convert.submit()
