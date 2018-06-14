#/usr/bin/env python3
# -*- encoding:utf8 -*-
from shutil import *
import os,sys
import subprocess
from subprocess import PIPE
from pprint import pprint
import datetime
from_source = "source"
to_source = "new_source"

def transfile(reset=False,fast=True,from_source="source",to_source="new_source"):
    if reset:
        try:
            rmtree(to_source)
        except FileNotFoundError as _e1:
            pass
        copytree(from_source,to_source)
        return 1
    if fast:
        fast_copytree(src=from_source,dst=to_source,symlinks=False)
    return 1

def fast_copytree(src,dst,symlinks=False,ignore_exist_dirs=True):
    """一个copytree的简化版本"""
    names = os.listdir(src)
    if ignore_exist_dirs:
        try: os.makedirs(dst)
        # except: print("文件夹已存在，跳过创建文件夹...")
        except: pass
    else:  os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src,name)
        dstname = os.path.join(dst,name)
        try:
            if os.path.isdir(srcname):
                fast_copytree(srcname,dstname,symlinks)
            else:
                copy2(srcname,dstname)
        except OSError as why:
            errors.append((srcname,dstname,str(why)))
        except Error as err:
            errors.extend(err.args[0])
    try:
        copystat(src, dst)
    except OSError as why:
        # can't copy file access times on Windows
        if why.winerror is None:
            errors.extend((src, dst, str(why)))
    if errors:
        raise Error(errors)

def get_status():
    c = "git status"
    process = subprocess.Popen(c,shell=True,stdout=PIPE,stdin=PIPE)
    process.wait()
    rc = process.returncode
    print("正在检查状态信息\n")
    print(process.communicate()[0])
    if rc != 0:
        print("初始化状态检查出错:",process.communicate())
        return 0
    else: return 1

def add_stuff():
    c = "git add --all"
    process = subprocess.Popen(c,shell=True,stdout=PIPE,stdin=PIPE)
    print("正在添加到本地缓冲区\n")
    print(process.communicate()[0])
    process.wait()
    if process.returncode != 0:
        print("添加到缓存区出错",process.communicate())
        return 0
    else: return 1

def commit_stuff():
    # i = input("请输入提交内容：____\b\b\b\b")
    i = datetime.datetime.today()
    c = "git commit -m 2018-06-14"
    process = subprocess.Popen(c,shell=True,stdout=PIPE,stdin=PIPE)
    print("提交本地仓库中...\n")
    print(process.communicate()[0])
    process.wait()
    if process.returncode != 0:
        print("提交到本地仓库失败",process.communicate())
        return 0
    else: return 1

def pull_stuff():
    c = "git pull"
    process = subprocess.Popen(c,shell=True,stdout=PIPE,stdin=PIPE)
    print("正在拉取远程代码\n")
    print(process.communicate()[0])
    process.wait()
    if process.returncode != 0:
        print("拉取远程代码失败",process.communicate())
        return 0
    else: return 1

def push_stuff():
    c = "git push"
    process = subprocess.Popen(c,shell=True,stdout=PIPE,stdin=PIPE)
    print("正在上传到服务器\n")
    print(process.communicate()[0])
    process.wait()
    if process.returncode != 0:
        print("上传到远程服务器失败",process.communicate())
        return 0
    else: return 1

def submit(pull_first=True):
    if pull_first:
        if not pull_stuff():        
            print("失败！")
            return 0
    if get_status():
        if add_stuff():
            if commit_stuff():
                    if push_stuff():
                        print("成功！")
                        return 1
    print("失败！")
    return 0
    
if __name__ == "__main__":
    if transfile(fast=True,from_source=from_source,\
        to_source=to_source): submit()