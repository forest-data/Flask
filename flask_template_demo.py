# -*- coding:utf-8 -*-

# 1.如何返回一个网页
# 2.如何给模板填充数据

from flask import Flask, render_template

app = Flask(__name__)    # 导入名

@app.route('/', methods = ['GET', 'POST'])
def hello_world():

    # 需要传入一个网址
    url_str = 'www.itheima.com'

    my_list = [1, 3, 4, 6]

    my_dict = {
        "name": "heima",
        "age": 15,
        "sex": "男"
    }
    # print(url_str, my_list, my_dict)
    # 通常，模板中使用的变量名和要传递的数据的变量名保持一致
    return render_template("index.html", url_str=url_str, my_list=my_list, my_dict=my_dict)


if __name__ == '__main__':
    # 执行app.run, 就会将Flask程序运行在一个简单的服务器(Flask提供的，用于测试的)
    app.run(host='0.0.0.0', port=5001, debug=True)