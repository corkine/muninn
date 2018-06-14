#/usr/bin/env python
# -*- coding:utf8 -*-
#本模块用来抽象课程结构，用来处理Python和Bootstrap进行笔记文件和网站静态展示的转换工作。
__version__ = "0.0.3"
__log__ = """2018-06-10 0.0.1 重构项目，添加Course类
2018-06-11 0.0.3 添加Note和Chapter类，添加了从源文件中获取数据的方法，添加了单元测试
"""
import random
from bs4 import BeautifulSoup
import lxml
import re

class Course:
    """课程类，课程包含章节类实例。

    初始化课程id、课程名称、课程类型、课程大类
    - get_uri() 返回课程概览及其各部分章节的URI地址（绝对地址）
    - set_config() 通过字典和参数自动化设置课程信息以及其章节信息（但不获取章节包含的标题、概述以及相关笔记）
    - print(Course) 返回一个可读的课程名称，用于进行程序诊断"""
    def __init__(self,id=None,name=None,type=None,fname=None):
        if id:self.id = id
        else:self.id = random.randint(1000,9999)
        self.fname = fname
        self.name = name
        self.type = type
        self.sourceuri = None
        self.chapters = []
        self.havefather = True

    def get_name(self,fname=False):
        """名称接口"""
        if fname:return self.fname
        else:return self.name
        
    def get_type(self):
        return self.type

    def have_father(self):
        """是否有父类的接口"""
        return self.havefather

    def get_uri(self,only_fname=False,only_name=False,full_path=False,is_chapter=False,chapter="",suffix=""):
        """返回课程的实际浏览器访问地址。
        返回的地址直接将name和fname变量替换空格为下划线，并按以下要求返回：
        对于具有大类的课程，返回二级地址 (CourseA/CourseA.1)，对于没有大类的课程，返回一级地址 (CourseA)。
        此处也可用于生成课程总览 (suffix = _overview.html) 地址，
        各章节 (is_chapter=True, chapter="", suffix= _ch_xx.html) 的地址，
        课程所属大类 (only_fname) 地址，课程 (only_name) 地址。
        """
        #只返回父文件夹地址，不可自定义后缀。
        if only_fname:
            res = self.fname.replace(" ","_")
            return res
        #这是程序用来定位文件的URI的地址(用于菜单导航)，每个课程，不论是一级还是二级，均在大类文件夹内。
        #多个属于同一大类的课程也在同一文件夹内
        if full_path: 
            res =  self.fname.replace(" ","_")+"/"+self.name.replace(" ","_")
            return res + suffix
        #返回章节html的地址，格式已经被定义好，不可使用suffix进行重新定义
        if is_chapter and chapter:
            res = self.name.replace(" ","_") + "_ch_%s"%chapter + ".html"
            return res
        #只返回课程名称地址，可自定义后缀。
        #用于返回课程总览界面
        if only_name:res = self.name.replace(" ","_")  
        if not res: raise ValueError("没有接受完全的参数")
        return res + suffix


    def __str__(self):
        """用于在命令行中显示状态信息"""
        if self.havefather:return self.fname + "::" + self.name
        else: return self.name

    def set_config(self,config):
        """用以从muninn_config.py配置文件中自动化配置
        传入一个字典，包含以下字段：
        - 课程名称 show_menu_name_2st
        - 大类名称 show_menu_name_1st
        - 课程类型 2st_addr
        - id信息 id
        - 课程地址 address
        - 章节信息(名称、版本号、章节地址、id信息) chapter_list
        注意，本方法并不对章节相关笔记进行初始化和设置
        
        返回实例本身"""

        c = config
        if "show_menu_name_2st" in c and c["show_menu_name_2st"]:
            self.name = c["show_menu_name_2st"]
            self.fname = c["show_menu_name_1st"]
            self.havefather = True
        else:
            self.name = c["show_menu_name_1st"]
            self.fname = c["show_menu_name_1st"]
            self.havefather = False
            # print(c,"NO FATHER")
        if hasattr(c,"2st_addr") and c["2st_addr"]:
            self.type = c["2st_addr"]
        if hasattr(c,"id") and c["id"]:
            self.id = c["id"]
        self.sourceuri = c["address"]
        for i in c["chapter_list"]:  
            ch = Chapter(course=self,name=i[0],mark=i[1],sourceuri=i[2],id=i[3])
            self.chapters.append(ch)
        return self

    def set_chapter(self,chapter_address="",get_header=False,get_description=False,get_notes=False,reload_info=False):
        """调用Chapter的fetch_from_HTML方法，并且返回此课程实例
        一般在这里进行章节信息的重载"""
        print("%s\n正在进行章节的信息获取，此过程可能需要较长的时间..."%("="*10))
        for ch in self.chapters:
            ch.fetch_from_HTML(chapter_address=chapter_address,get_header=get_header,
                            get_description=get_description,get_notes=get_notes,reload_info=reload_info)
        return self

class Chapter:
    """章节类
    初始化包含所属课程、章节id、名称、章节地址、章节版本、章节描述
    - print(Chapter) 返回课程名称和章节名称
    - get_related_notes() 返回相关笔记
    - get_version() 返回版本号和地址
    - get_header() 返回章节包含的h1和h2标题
    - get_description() 返回章节的描述
    - fetch_from_HTML() header、description、related_notes都需要从此函数获取，不自动初始化"""
    def __init__(self, course=None, id=None, name=None, sourceuri=None, mark=None, description="", *args, **kwargs):
        if id:self.id = id
        else: self.id = random.randint(1000,9999)
        self.course = course
        self.name = name
        self.sourceuri = sourceuri
        self.mark = mark
        self.related_notes = []
        self.description = description
        self.chapter_head = None

    def __str__(self):
        return str(self.course)+"::"+self.name

    def get_name(self):
        return self.name

    def get_related_notes(self):
        return self.related_notes

    def get_id(self):
        return self.id

    def get_version(self,only_mark=False,only_url=False,only_id=False):
        if only_url and only_mark and only_id: raise ValueError("参数传入错误")
        if only_mark:return self.mark
        elif only_url:return self.sourceuri
        elif only_id: return self.id
        else: return self.name, self.id, self.mark, self.sourceuri

    def get_header(self):
        return self.chapter_head

    def get_description(self):
        return self.description

    def fetch_from_HTML(self,chapter_address="",get_header=False,get_description=False,get_notes=False,reload_info=False):
        """获取课程描述信息以及构建相关笔记信息"""
        #获取标题信息，并返回到chapter_head中。
        if get_header:
            f = open(chapter_address + self.sourceuri,"r",encoding="utf8")
            print(self,"正在解析HTML文档")
            print("\t\t获取标题信息中，请稍后...")
            h1_rules = re.compile("<h1[^>]*>(.*?)<")
            h2_rules = re.compile("<h2[^>]*>(.*?)<")
            #对于每一行，使用正则表达式搜索一级标题和二级标题，这里没有使用BS，因为太TM慢了。
            self.chapter_head = []
            current_h1 = ""
            for l in f:
                if (not l) or (not "h" in l):continue
                h1 = h2 = ""
                h1 = h1_rules.findall(l)
                h2 = h2_rules.findall(l)
                if h1:
                    h1 = h1[0]
                    self.chapter_head.append("<h1>"+h1)
                #是否存在一段中含有H1和H2？
                if h2:
                    h2 = h2[0] 
                    self.chapter_head.append("<h2>"+h2)
            f.close()
        #获取描述信息，并填充到description中。
        if get_description:
            f = open(chapter_address + self.sourceuri,"r",encoding="utf8")
            print("\t\t获取描述性信息中，请稍后...")
            soup = BeautifulSoup(f,"lxml")
            res = soup.find_all("intro")
            if res: 
                #因为只有一个结果，所以选用索引的第一个即可
                self.description = str(res[0]).replace("<intro>","").replace("</intro>","").replace("¶","")
            f.close()
        #获取相关笔记描述，并且构建Note OO对象。
        if get_notes:
            f = open(chapter_address + self.sourceuri,"r",encoding="utf8")
            print("\t\t获取相关笔记信息中，请稍后...")
            soup = BeautifulSoup(f,'lxml')
            res = soup.find_all("div",type="related_note")
            if res:
                for note in res:
                    try:
                        footer = note["footer"]
                    except:
                        footer = ""
                    try:
                        description = note["description"]
                    except:
                        description = ""
                    try:
                        mold = note["mold"]
                    except:
                        mold = "blog"
                    try:
                        sourceuri = note["url"]
                    except:
                        sourceuri = "#"
                    try:
                        modified_date = note["update"]
                    except:
                        modified_date = "0000-00-00"
                    # print(description,sourceuri,mold,footer)
                    n = Note(name=note.get_text(),description=description,
                            sourceuri=sourceuri,mold=mold,footer=footer,
                            modified_date=modified_date)
                    self.related_notes.append(n)

            if reload_info:
                print("\t\t检测到源文件的名称和标题，正在获取并配置，请稍后...")
                res2 = soup.find_all("div",type="chapter_info")
                if res2:res2 = res2[0]
                if "title" in res2:self.name = res2["title"] 
                if "mark" in res2:self.mark = res2["mark"]                     
            f.close()


        
class Note:
    """基本的笔记类"""
    def __init__(self, id=None, name="", sourceuri=None, description="", footer="", mold="", \
                    modified_date="2018-06-11", *args, **kwargs):
        if id:self.id = id
        else: self.id = random.randint(1000,9999)
        self.name = name
        self.sourceuri = sourceuri
        self.description = description
        self.mold = mold
        self.footer = footer
        self.modified_date = modified_date
    def __str__(self):
        return self.name


if __name__ == "__main__":
    temp_dict = {
        "show_menu_name_1st":"Probability",
        "show_menu_name_2st":None,
        "2st_addr":None,
        "address":"/probability",
        "id":"pr1",
        "chapter_list":[
            ("概率导论","0.9","probability/Week1&2_Probability.html","w12"),
            ("独立概率和古典概率","0.9","probability/Week_3.html","w3"),
            ("离散分布模型","0.8","probability/Week4_PMF_CDF.html","w4"),
        ],
    }
    c = Course().set_config(temp_dict).set_chapter("source/",True,True,True,True)
    print(c)
    for ch in c.chapters:
        print(ch,ch.get_description(),ch.get_version(),ch.get_header(),ch.get_related_notes())


