#/usr/bin/env python3
# -*- encoding:utf8 -*-
from shutil import *
import os,sys,datetime
import subprocess
from subprocess import PIPE
from pprint import pprint
from muninn_config import JUPYTER_NOTEBOOK_ALLOWED_FOLDER,JUPYTER_NOTEBOOK_ROOT_FOLDER,HTML_DST_FOLDER


def convert(filename,fname):
    """调用命令行工具对ipynb文件进行html转换，
    放在其原始文件夹下，fname为其所在文件夹，filename为其文件名"""
    current = os.getcwd()
    os.chdir(fname)
    c = "jupyter nbconvert %s"%filename
    p = subprocess.Popen(c,shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
    # print(str(p.communicate()[0],"utf-8"),p.communicate()[1])
    p.wait()
    if p.returncode != 0:
        print("转换失败!")
        os.chdir(current)
        return 0
    os.chdir(current)
    return 1

def convert_all(root_folder=".",file_type=".ipynb"):
    """对于一个目录内所有文件夹和子文件夹进行遍历，
    对指定文件类型的文件进行转换，并存放在原始目录下
    root_folder为根目录，file_type为需要转换的文件特征"""
    error = []
    for fo in os.walk(root_folder):
        for f in fo[2]:
        #对于每个文件夹进行遍历
            if (f.endswith(file_type) and 
                str(fo[0]).split("\\")[-1] in JUPYTER_NOTEBOOK_ALLOWED_FOLDER):
                #如果以ipynb结尾，那么进行转换
                try:
                    if convert(f,fo[0]):
                        print("Find ipynb file ",str(fo[0]),str(f)," == Convert Suscessful")
                except Exception as _e:
                    error.append(str(_e))
    if error:print("在转换过程中发生以下错误：%s"%error)
    return 1

def transfile(reset=False,fast=True,from_source="source",to_source="new_source",allowed_folder=[]):
    "只拷贝出现在允许列表的文件夹以及其文件"
    if reset:
        try:
            rmtree(to_source)
        except FileNotFoundError as _e1:
            pass
        copytree(from_source,to_source)
        return 1
    if fast:
        fast_copytree(src=from_source,dst=to_source,symlinks=False,allowed_folder=allowed_folder)
    return 1

def fast_copytree(src,dst,symlinks=False,ignore_exist_dirs=True,allowed_folder=[]):
    """一个copytree的简化版本"""
    names = os.listdir(src)
    if ignore_exist_dirs:
        if dst.split("\\")[-1] in allowed_folder:
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
                fast_copytree(srcname,dstname,symlinks,allowed_folder=allowed_folder)
            else:
                if src.split("\\")[-1] in allowed_folder:
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
    c = "git commit -m %s"%i
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

def submit():
    if get_status():
        if add_stuff():
            if commit_stuff():
                    if push_stuff():
                        print("成功！")
                        return 1
    print("失败！")
    return 0

def main():
    if transfile(from_source=JUPYTER_NOTEBOOK_ROOT_FOLDER,
                to_source=HTML_DST_FOLDER,
                allowed_folder=JUPYTER_NOTEBOOK_ALLOWED_FOLDER):
        if convert_all(root_folder=HTML_DST_FOLDER):
            print("Convert all done!")




if __name__ == "__main__":
    # convert("week5_problem_soving.ipynb","notebook")
    # if transfile(fast=True,from_source=from_source,\
    #     to_source=to_source): submit()
    # main()
    submit()
    