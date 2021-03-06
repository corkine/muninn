#/usr/bin/env python3
# -*- coding: utf8 -*-

JUPYTER_NOTEBOOK_ROOT_FOLDER = "/root/.jupyter"
#JUPYTER_NOTEBOOK_ROOT_FOLDER = """C:\\Users\\Administrator\\Desktop\\jupyter"""

# JUPYTER_NOTEBOOK_ALLOWED_FOLDER = [
#     "coursera_learn_ml",
#     "coursera_learn_models",
#     "coursera_learn_perception",
#     "book_learn_stats",
#     "learn_c",
#     "learn_machine_learning",
#     "coursera_learn_computer",
# ]
#for debug

HTML_DST_FOLDER = "source"

COURSE_HEAD = ["mt","pr1","pandas","plot","sklearn","matlab","introc","cst","langc","javase","javaee","design_pattern","database","js","python","visual1","neuro","ml1"]
#for debug
# COURSE_HEAD = ["mt","c3"]

COURSE_INFO = {
    "pr1":
    {
        "show_menu_name_1st":"Data Science",
        "show_menu_name_2st":"Probability",
        "2st_addr":None,
        "address":"book_learn_stats",
        "id":"pr1",
        "chapter_list":[
            ("概率导论","0.9","Week1_2_Probability.html","w12"),
            ("独立概率和古典概率","0.9","Week_3.html","w3"),
            ("离散分布模型","0.8","Week4_PMF_CDF.html","w4"),
            ("连续分布模型","0","week5.html","w5"),
            ("连续分布期望值","0","week6.html","w6"),
        ],
    },
    "pandas":
    {
        "show_menu_name_1st":"Data Science",
        "show_menu_name_2st":"Pandas & Numpy",
        "2st_addr":None,
        "address":"book_learn_stats",
        "id":"pandas",
        "chapter_list":[
        ],
    },
    "plot":
    {
        "show_menu_name_1st":"Data Science",
        "show_menu_name_2st":"Plot with Matplotlib",
        "2st_addr":None,
        "address":"book_learn_stats",
        "id":"plot",
        "chapter_list":[
        ],
    },
    "sklearn":
    {
        "show_menu_name_1st":"Data Science",
        "show_menu_name_2st":"SKlearn",
        "2st_addr":None,
        "address":"book_learn_stats",
        "id":"sklearn",
        "chapter_list":[
        ],
    },
    "matlab":
    {
        "show_menu_name_1st":"Data Science",
        "show_menu_name_2st":"MATLAB & PTB",
        "2st_addr":None,
        "address":"book_learn_stats",
        "id":"matlab",
        "chapter_list":[
        ],
    },
    "mt":
    {
        "show_menu_name_1st":"Model Thinking",
        "show_menu_name_2st":None,
        "2st_addr":None,
        "address":"coursera_learn_models",
        "id":"mt",
        "chapter_list":[
            ("[O] Aggragation(S) & Decision(P)","1.3","WEEK2_model_thinking.html","ad"),
            ("[I] How People Think & Modeling Data","1.1","Week3_Model_Thinking.html","pd"),
            ("[F] Tipping Point & Growth Model","0.8","week4_tipping_point.html","tg"),
            ("[F] Perspectives & Marklv Processing","0.8","week5_problem_soving.html","pm"),
            ("Lyapunov Functions","0.8","week7_lyapunov_functions.html","lf"),
            ("path dependent","","week8_path_dependent.html","pq"),
            ("random","","week9_random_walk.html","w9"),
            ("dilemma","","week10_prisoner_dilemma.html","w10"),
            ("replicator","","week11_replicator_dynamics.html","w11"),
        ],
    },
    "introc":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Introduction to Computer",
        "2st_addr":None,
        "address":"learn_c",
        "id":"c1",
        "chapter_list":[
            ("可计算思想和计算机概论","1.3","learn_c_1.html","lc"),
        ],
    },
    "langc":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"C Primer Plus",
        "2st_addr":"读书笔记",
        "address":"learn_c",
        "id":"c2",
        "chapter_list":[
            ("数据、字符串、格式化输入输出","1","chapter_4_string_and_scanf.html","w3"),
            ("操作符、表达式、语句、字符串I/O机制","1","chapter_5_operator.html","w4"),
            ("函数、指针和数组","1","chapter6_function.html","w5"),
            ("结构体和链表","1","chapter7_struct.html","w6"),
        ],
    },
    "cst":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Computer Structure",
        "2st_addr":"学习笔记",
        "address":"coursera_learn_computer",
        "id":"c3",
        "chapter_list":[
            ("intro","0","chapter1_intro.html","w1"),
            ("x86_mips","0","chapter2_x86_mips.html","w2"),
            ("ALU","0","chapter3_alu.html","w3"),
            ("multi","0","chapter4_mult.html","w4"),
            ("design_a_cpu","0","chapter5_design_a_cpu.html","w5"),
            ("pipe_cpu","0","chapter6_pipe.html","w6"),
            ("cache","0","chapter7_cache.html","w7"),
            ("interrupt","0","chapter8_interrupt.html","w8"),
            ("io","0","chapter9_io.html","w9"),
            
        ],
    },
    "javase":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Thinking in Java",
        "2st_addr":"读书笔记",
        "address":"learn_java",
        "id":"c3",
        "chapter_list":[
            ("对象、操作符和流程控制","0","chapter1_play_java.html","w1"),
            ("初始化和清理","0","chapter2_init_finalize.html","w2"),
            ("权限、类重用","0","chapter3_permission.html","w3"),
            ("多态","0","chapter4_cast.html","w4"),
            ("接口","0","chapter5_interface.html","w5"),
            ("内部类","0","chapter6_innerclass.html","w6"),
            ("容器","0","chapter7_container.html","w7"),
            ("异常","0","chapter8_exception.html","w8"),
            ("字符串","0","chapter9_string.html","w9"),
            ("类型信息","0","chapter10_rtti.html","w10"),
            ("泛型","0","chapter11_generics.html","w11"),
            ("数组","0","chapter12_array.html","w12"),
            ("IO","0","chapter13_io.html","w13"),
            ("J8","0","chapter14_java8.html","w14"),
        ],
    },    
    "design_pattern":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Design Pattern",
        "2st_addr":None,
        "2st_addr":"读书笔记",
        "address":"learn_design_pattern",
        "id":"dp",
        "chapter_list":[
            ("策略模式，观察者模式和装饰器模式","0","chapter1_design_pattern_intro.html","w1"),
            ("工厂模式","0","chapter2_factory.html","w2"),
            ("单件模式和命令模式","0","chapter3_singleton_command.html","w3"),
            ("适配器模式和外观模式","0","chapter4_adaptor_skin.html","w4"),
            ("模板方法模式，迭代器和组合模式","0","chapter5_template_iterator.html","w5"),
            ("状态模式和策略模式","0","chapter6_status.html","w6"),
            ("代理模式","0","chapter7_proxy.html","w7"),
            ("复合模式","0","chapter8_combination.html","w8"),
            ("MVC模式","0","chapter9_mvc.html","w9"),
            ("特定领域设计模式","0","chapter10_other_design_patterns.html","w10"),
            
        ],
    },
    "javaee":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Learn Java EE",
        "2st_addr":None,
        "2st_addr":"读书笔记",
        "address":"learn_javaee",
        "id":"js",
        "chapter_list":[
            ("serlvet_jsp_basic","0","chapter1_servelt_basic.html","c1"),
            ("action_el","0","chapter2_action_el.html","c2"),
            ("jstl_taglib","0","chapter3_jstl_taglib.html","c3"),
            ("deploy_secret_filter_wrapper","0","chapter4_deploy_security_filter_wrapper.html","c4"),
            ("spring_ioc","0","chapter5_spring_ioc.html","c5"),
            ("spring_aop","0","chapter6_spring_aop.html","c6"),
            ("jdbc","0","chapter7_jdbc.html","c7"),
            ("jdbc_transaction","0","chapter8_spring_jdbc_transaction.html","c8"),
            ("hibernate_without_jpa","0","chapter9_hibernate_basic.html","c9"),
            ("spring_mvc","0","chapter10_spring_mvc.html","c10"),
            ("SSH","0","chapter11_ssh.html","c11"),
            ("maven","0","chapter12_maven.html","c12"),
        ],
    },
    "database":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Learn Database",
        "2st_addr":None,
        "address":"learn_database",
        "id":"mysql",
        "chapter_list":[
            ("mysql学习指南","0","book1_mysql_learn_guide.html","b1"),
        ],
    },
    "js":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Using JavaScript",
        "2st_addr":None,
        "2st_addr":"读书笔记",
        "address":"learn_javascript",
        "id":"js",
        "chapter_list":[],
    },
    "python":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"Using Python",
        "2st_addr":None,
        "address":"learn_python",
        "id":"mysql",
        "chapter_list":[
            ("play_with_django","0","learn_django_1.html","c1"),
            ("django_deployed","0","django_deployed.html","c2"),
        ],
    },
    "visual1":
    {
        "show_menu_name_1st":"Neuro Science",
        "show_menu_name_2st":"Visual Percipience",
        "2st_addr":None,
        "address":"coursera_learn_perception",
        "id":"visual1",
        "chapter_list":[
            ("角度、长度、大小、距离、深度感知","1","Week3_see_space.html","sp"),
            ("运动、方向、速度感知","1","Week_4_Seeing_Motion.html","sm"),
            ("一个整合视觉错觉的统一理论","1","Week_5_SumUp.html","su"),
        ],
    },
    "neuro":
    {
        "show_menu_name_1st":"Neuro Science",
        "show_menu_name_2st":"Medical Neuroscience",
        "2st_addr":None,
        "address":"learn_neuroscience",
        "id":"neuro",
        "chapter_list":[
            ("导论","0","chapter1_intro.html","c1"),
            ("静息态神经元膜和动作电位","0","chapter2_how_neuro_works_1.html","c2"),
        ],
    },
    "ml1":
    {
        "show_menu_name_1st":"Machine Learning",
        "show_menu_name_2st":"Andrew Ng ML",
        "2st_addr":"课程笔记",
        "address":"learn_machine_learning",
        "id":"ml1",
        "chapter_list":[
            ("K-Means & PCA","1","chapter7_clustering.html","cl"),
            ("异常检测 & 推荐系统","1","chapter8.html","ca"),
        ],
    },
    # "mluw":
    # {
    #     "show_menu_name_1st":"Machine Learning",
    #     "show_menu_name_2st":"UW GraphLab",
    #     "2st_addr":"课程笔记",
    #     "address":"learn_machine_learning",
    #     "id":"mluw",
    #     "chapter_list":[
    #         ("使用回归预测房价","0.9","Regression_Predicting_house_prices.html","re"),
    #         ("使用分类预测商品评分","0.9","logistic_classification_ex.html","lo"),
    #         ("使用聚类评估多人关系(KNN)","0.9","knn_model.html","kn"),
    #         ("使用因式分解推荐歌曲","0.9","song_recommender.html","sr"),
    #     ],
    # }
}



