#/usr/bin/env python3
# -*- coding: utf8 -*-
GITHUB_REP_ADDRESS = "https://github.com/corkine/muninn"

JUPYTER_NOTEBOOK_ROOT_FOLDER = "/root/.jupyter"
# JUPYTER_NOTEBOOK_ROOT_FOLDER = "C:/Users/Administrator/Desktop/.jupyter"

JUPYTER_NOTEBOOK_ALLOWED_FOLDER = [
    "coursera_learn_ml",
    "coursera_learn_models",
    "coursera_learn_perception",
    "book_learn_stats",
    "learn_c",
    "learn_machine_learning",
]

HTML_DST_FOLDER = "./source"

COURSE_INFO = {
    "pr1":
    {
        "show_menu_name_1st":"Probability",
        "show_menu_name_2st":None,
        "2st_addr":None,
        "address":"/book_learn_stats",
        "id":"pr1",
        "chapter_list":[
            ("概率导论","0.9","book_learn_stats/Week1&2_Probability.html","w12"),
            ("独立概率和古典概率","0.9","book_learn_stats/Week_3.html","w3"),
            ("离散分布模型","0.8","book_learn_stats/Week4_PMF_CDF.html","w4"),
            ("连续分布模型","0","book_learn_stats/week5.html","w5"),
        ],
    },
    "mt":
    {
        "show_menu_name_1st":"Model Thinking",
        "show_menu_name_2st":None,
        "2st_addr":None,
        "address":"/coursera_learn_models",
        "id":"mt",
        "chapter_list":[
            ("[O] Aggragation(S) & Decision(P)","1.3","coursera_learn_models/WEEK2_model_thinking.html","ad"),
            ("[I] How People Think & Modeling Data","1.1","coursera_learn_models/Week3_Model_Thinking.html","pd"),
            ("[F] Tipping Point & Growth Model","0.8","coursera_learn_models/week4_tipping_point.html","tg"),
            ("[F] Perspectives & Marklv Processing","0.8","coursera_learn_models/week5_problem_soving.html","pm"),
            ("Lyapunov Functions","0.8","coursera_learn_models/week7_lyapunov_functions.html","lf"),
        ],
    },
    "c1":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"可计算思想和计算机概论",
        "2st_addr":None,
        "address":"/learning_c",
        "id":"c1",
        "chapter_list":[
            ("可计算思想和计算机概论","1.3","learn_c/learn_c_1.html","lc"),
        ],
    },
    "c2":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"C Primer Plus",
        "2st_addr":"读书笔记",
        "address":"/learning_c",
        "id":"c2",
        "chapter_list":[
            ("数据和C","1","learn_c/chapter_3_data_and_c.html","da"),
            ("字符串、格式化输入输出","1","learn_c/chapter_4_string_and_scanf.html","ss"),
            ("操作符、表达式和语句","1","learn_c/chapter_5_operator.html","op"),
            ("控制语句","","learn_c/chapter6_control.html","c6")
        ],
    },
    "cpp":
    {
        "show_menu_name_1st":"Computer Science",
        "show_menu_name_2st":"C++ Primer",
        "2st_addr":None,
        "2st_addr":"读书笔记",
        "address":"/learning_c",
        "id":"cpp",
        "chapter_list":[],
    },
    "visual1":
    {
        "show_menu_name_1st":"Neuro Science",
        "show_menu_name_2st":"Visual Percipience",
        "2st_addr":None,
        "address":"/coursera_learn_perception",
        "id":"visual1",
        "chapter_list":[
            ("角度、长度、大小、距离、深度感知","1","coursera_learn_perception/Week 3_see_space.html","sp"),
            ("运动、方向、速度感知","1","coursera_learn_perception/Week_4_Seeing_Motion.html","sm"),
            ("一个整合视觉错觉的统一理论","1","coursera_learn_perception/Week_5_SumUp.html","su"),
        ],
    },
    "ml1":
    {
        "show_menu_name_1st":"Machine Learning",
        "show_menu_name_2st":"Andrew Ng ML",
        "2st_addr":"课程笔记",
        "address":"/learn_machine_learning",
        "id":"ml1",
        "chapter_list":[
            ("K-Means & PCA","1","learn_machine_learning/chapter7_clustering.html","cl"),
            ("异常检测 & 推荐系统","1","learn_machine_learning/chapter8.html","ca"),
        ],
    },
    "mluw":
    {
        "show_menu_name_1st":"Machine Learning",
        "show_menu_name_2st":"UW GraphLab",
        "2st_addr":"课程笔记",
        "address":"/learn_machine_learning",
        "id":"mluw",
        "chapter_list":[
            ("使用回归预测房价","0.9","learn_machine_learning/Regression_Predicting_house_prices.html","re"),
            ("使用分类预测商品评分","0.9","learn_machine_learning/logistic_classification_ex.html","lo"),
            ("使用聚类评估多人关系(KNN)","0.9","learn_machine_learning/knn_model.html","kn"),
            ("使用因式分解推荐歌曲","0.9","learn_machine_learning/song_recommender.html","sr"),
        ],
    }
}

COURSE_INFO2 = {
    "mt":
    {
        "show_menu_name_1st":"Model Thinking",
        "show_menu_name_2st":None,
        "2st_addr":None,
        "address":"/coursera_learn_models",
        "id":"mt",
        "chapter_list":[
            ("[O] Aggragation(S) & Decision(P)","1.3","coursera_learn_models/WEEK2_model_thinking.html","ad"),
            ("[I] How People Think & Modeling Data","1.1","coursera_learn_models/Week3_Model_Thinking.html","pd"),
            ("[F] Tipping Point & Growth Model","0.8","coursera_learn_models/week4_tipping_point.html","tg"),
            ("[F] Perspectives & Marklv Processing","0.8","coursera_learn_models/week5_problem_soving.html","pm"),
            ("Lyapunov Functions","0.8","coursera_learn_models/week7_lyapunov_functions.html","lf"),
        ],
    },
}



