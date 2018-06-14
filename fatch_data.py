#/usr/bin/env python3
# -*- coding: utf8 -*-
__version__ = "0.0.4"
__log__ = """2018-06-11 0.0.3 使用model提供的类方法而不是对象属性重构了项目，使用API解耦合。
添加了Pickle存储对象，方便进行调试。
对于从源HTML中获取Chapter的信息，提供了一个类方法，现在只需要一句话就可以完全自动构建Course对象，
其中自动化Course的信息、包含章节的信息以及每个章节相关笔记的信息。
2018-06-11 0.0.4 完善related_notes笔记接口，提供三种标准（问题、名言、博客类型），整个程序大体完成。
"""

from muninn_config import *
import random,os,re,pickle
from model import *

def constructWorld(courses,notes=None):
    """构建OO对象，仅初始化课程及其包含的章节，不包括章节具体标题、描述和相关笔记。"""
    clist = []
    for key in courses:
        #从config.py中配置Course信息，包括Course信息，其包含的Chapter信息（构建Chapter对象）
        # 以及对应地址包含的Chapter标题、描述和相关Note对象信息
        c = Course().set_config(courses[key]).set_chapter(chapter_address="source/",
            get_header=True,get_description=True,get_notes=True,reload_info=True)
        #顺手读取了关联章节名称、id、地址和版本号
        clist.append(c)
    return clist

def main(update_data=False,file_path="data.pkl"):
    #首先调用构建OO对象的函数，构建课程集
    print("="*20,"开始处理数据","="*20)
    if update_data:
        print("正在构建项目")
        clist = constructWorld(COURSE_INFO)
        p = pickle.dump(clist,open(file_path,"wb"))
        print("项目构建完毕，并且存放在:%s"%file_path)
    else:
        print("从备份中读取项目")
        clist = pickle.load(open(file_path,"rb"))
    #首先根据所有项目生成一个HTML页面的菜单，点击链接到下面创建的html文件中
    menu_html = makeHead(clist)
    # #接着根据每个页面的信息生成单独的页面，每个页面的命名根据课程名称进行命名
    for c in clist: 
        overview = makeHTMLPage(c,menu_html)
        print("\t生成HTML::课程总览",c)
        writeToFile(c,overview)
        for ch in c.chapters:
            print("\t\t生成HTML::章节信息",ch)
            ch_html = makeHTMLPage(c,menu_html,is_chapter=True,chapter_id=ch.id)
            writeToFile(c,ch_html,suffix="_ch_%s.html"%ch.id)
    print("="*20,"FINISHED","="*20)

def makeHead(clist):
    """根据所有的课程信息返回一个HTML语言的导航条"""
    out_html = ""
    dropdown_html = ""
    finished_2st = []
    for c in clist:
        if not c.have_father():
            out_html += """ <li class="nav-item">
                                <a class="nav-link" href="%s">%s</a>
                            </li>
                            """%("/"+c.get_uri(full_path=True,suffix="_overview.html"),c.get_name())
            #print("here :",c.get_uri(full_path=True,suffix="_overview.html"))
        else:
            rand_a = random.randint(1000,9999)
            sub_html = ""
            for cs in clist:
                if (cs.get_name(fname=True) in finished_2st) or (not cs.have_father()) or\
                         (cs.get_name(fname=True) != c.get_name(fname=True)):
                    continue
                else:
                    if not cs.get_type():
                        _type = ""
                    else: _type = cs.get_type()
                    sub_html += """         
                                        <a class="dropdown-item" href="%s">%s <small>%s</small></a>
                            """%("/"+cs.get_uri(full_path=True,suffix="_overview.html"),cs.get_name(),_type)
            if not c.get_name(fname=True) in finished_2st:
                dropdown_now_html = """  
                                <li class="nav-item dropdown">
                                    <a class="nav-link dropdown-toggle" href="#" id="%s" data-toggle="dropdown">%s</a>
                                    <div class="dropdown-menu" aria-labelledby="%s">%s</div>
                                </li>"""%(rand_a,c.get_name(fname=True),rand_a,sub_html)
                out_html += dropdown_now_html
            finished_2st.append(c.get_name(fname=True))
            
    menu_html = """
                <nav class="navbar navbar-expand navbar-dark bg-dark">
                    <a class="navbar-brand" href="#">MUNINN <small>by Corine Ma</small></a>
                    <div class="navbar-collapse collapse justify-content-between">
                        <ul class="navbar-nav">
                            %s
                        </ul>
                    </div>
                    <div class="collapse navbar-collapse justify-content-end"></div>
                </nav>
                """%out_html
    return menu_html

def makeHTMLPage(course_info,menu_html,is_chapter=False,chapter_id="",chapter_address="source/"):
    """对于课程总览，在此返回HTML页面。对于每个章节，也在此返回HTML页面。"""
    c = course_info
    chapter_html = ""
    notes_html = ""
    html_now = ""
    intro_content = "尚未添加内容"
    detail_map = {
        "h1_title":"",
        "h2_html":"",
    }
    for ch in c.chapters:
        #如果需要处理的是章节页面，找到当前章节并进行以下处理：
        if is_chapter and ch.id == chapter_id:
            #左侧上方标题
            chapter_html += """<a href="%s" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center active">
                                %s<span class="badge badge-primary badge-pill">%s</span></a>"""%(c.get_uri(is_chapter=True,chapter=ch.id),ch.name,ch.mark)

            #左侧下方章节内容
            current_h1 = ""
            html_now = """  <ul class="list-group">
                            <li class="list-group-item list-group-item-light">章节目录</li>"""
            for head in ch.get_header():
                if not current_h1: current_h1 = head
                if head.startswith("<h1>") and current_h1 != head:
                    html_now += """</ul>
                        </li>"""
                    current_h1 = head                   
                if head.startswith("<h1>"):
                    html_now += """
                    <li class="list-group-item">
                            %s
                            <ul class="list-group list-group-flush">"""%head.replace("<h1>","")
                if head.startswith("<h2>"):
                    html_now += """<li class="list-group-item">%s</li>"""%head.replace("<h2>","")
            html_now += """</ul></li>"""

            #这里是寻找<intro>标签，然后返回右侧上方的章节总体概要信息。
            intro_content = ch.get_description()

            #返回右下角的笔记信息
            notes = ch.get_related_notes()
            # print("get notes",notes)
            notes_html = ""
            blog_mold = """             
            <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">
                            <a class="card-link" href="{note_url}">{note_title}</a> </h5>
                        <p class="card-text">{note_description}</p>
                        <small class="card-text text-muted">{note_date}</small>
                    </div>
                </div>"""
            quote_mold = """
            <div class="card text-right p-3">
                    <blockquote class="blockquote mb-0">
                        <p>{note_title}</p>
                        <footer class="blockquote-footer">
                            <small class="text-muted">{note_footer}</small>
                        </footer>
                    </blockquote>
                </div>"""
            question_mold = """
            <div class="card border-danger">
                    <div class="card-body">
                        <p class="card-text">{note_title}</p>
                        <span class="card-text"><small>{note_date}</small></span>
                    </div>
                </div>"""
            for note in notes:
                note_map = {
                "note_url":note.sourceuri,
                "note_title":note.name,
                "note_description":note.description,
                "note_date":note.modified_date,
                "note_footer":note.footer,
                }
                if note.mold == "blog":
                    notehtml = blog_mold.format_map(note_map)
                elif note.mold == "quote":
                    notehtml = quote_mold.format_map(note_map)
                elif note.mold == "question":
                    notehtml = question_mold.format_map(note_map)
                notes_html += notehtml

                
        else:
            #全局页面，非单个章节
            chapter_html += """<a href="%s" class="list-group-item list-group-item-action d-flex justify-content-between align-items-center">
                                %s<span class="badge badge-primary badge-pill">%s</span></a>
                                """%(c.get_uri(is_chapter=True,chapter=ch.get_id()),\
                                                ch.get_name(),ch.get_version(only_mark=True))

    isc = isc2 = overview_href = ""
    if is_chapter:
        isc = ""
        isc2 = "active"
        overview_href = c.get_uri(only_name=True,suffix="_overview.html")
    else:
        isc = "active"
        isc2 = "disabled"
        overview_href = "#"
    map_c = {
        "title": c.get_name(),
        "nb_href":"#",
        "single_chapter":chapter_html,
        "overview":isc,
        "notebook":isc2,
        "overview_href":overview_href,
        "html_now":html_now,
        "intro_content":intro_content,
        "notes_html":notes_html,
        "page_name":c.get_name(),
    }
    head_nav = """
        <nav class="nav nav-tabs bg-light">
            <li class="nav-item">
                <small><a class="nav-link">{title}</a></small>
            </li>
            <li class="nav-item">
                <small><a class="nav-link {overview}" href="{overview_href}">Overview</a></small>
            </li>
            <li class="nav-item">
                <small><a class="nav-link" href="#">Course Info</a></small>
            </li>
            <li class="nav-item">
                <small><a class="nav-link {notebook}" href="{nb_href}">Notebook</a></small>
            </li>
        </nav>""".format_map(map_c)

    #row和container不闭合
    left_nav = """
            <div class="container mt-5 ml-auto">
                <div class="row">
                    <!--左侧-->
                    <div class="col-md-4">
                        <!--章节名称-->
                        <div class="list-group list-group-flush">
                            {single_chapter}
                        </div>
                        <!--章节详细信息-->
                        <div class="card mt-4">
                            {html_now}
                        </div>
                    </div>
            """.format_map(map_c)

    header = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>{page_name} - 笔记和写作扩展</title>
                <link href="https://cdn.bootcss.com/bootstrap/4.1.1/css/bootstrap.css" rel="stylesheet">
                <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://cdn.bootcss.com/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
                <script src="https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            </head>
            <body>""".format_map(map_c)

    footer = """
            <footer class="mt-5 pt-5 pl-5 text-muted text-center text-small">
                <ul class="list-inline">
                    <li class="list-inline-item">&copy; 2017-2018 Marvin Studio</li>
                    <li class="list-inline-item"><a href="#">About Project Muninn</a></li>
                </ul>
            </footer>
            </body>
            </html>"""

    #此处闭合contaioner和row
    intro_html = """<!--右侧-->
        <div class="col-md-8 pl-3">
            <!--本章概览-->
            <div class="card">
                <div class="card-header">本章概览</div>
                <div class="card-body">
                    <p class="card-text">
                        {intro_content}
                    <p class="card-text">
                        <small class="text-muted">最后更新于 2018-06-09 <a href="http://blog.mazhangjing.com/notebook" class="card-link">查看笔记</a></small>
                    </p>
                </div>
            </div>
            <!--笔记详情-->
            <div class="card-columns mt-5">
                {notes_html}
            </div>
        </div>
    </div>
</div>""".format_map(map_c)
    
    output_html = header + menu_html + head_nav + left_nav + intro_html  + footer
    return output_html

            # <script src="js/jquery.slim.min.js"></script>
            # <script src="js/popper.min.js"></script>
            # <script src="js/bootstrap.min.js"></script>
    
def writeToFile(c,html,suffix="_overview.html"):
    fname_uri = c.get_uri(only_fname=True)
    if os.path.isdir(fname_uri):pass
    else: os.mkdir(fname_uri)
    f = open(c.get_uri(full_path=True,suffix=suffix),"w+",encoding="utf8")
    f.write(html)
    f.close()
    
    
if __name__ == "__main__":
    main(update_data=True,file_path="2018-06-12.data")
    input()
    