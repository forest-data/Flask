# -*- coding:utf-8 -*-
# 1. 导入 flask 扩展
from flask import Flask

# 2. 创建Flask应用程序实例
# 需要传入__name__， 作用是为了确定资源所在的路径
app = Flask(__name__)    # 导入名

# 3. 定义路由及视图函数
# 通过装饰器实现路由定义
# 路由默认只支持GET，如果需要增加，需要自行指定。
@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return "Hello Forrest!"


# 使用同一个视图函数 来显示不同用户的订单信息
# <> 定义路由参数， <> 内需要起个名字
@app.route('/order/<int:order_id>')
def get_order_id(order_id):
    # 需要在视图函数的()内填入参数名， 那么后面的代码才能去使用。
    return "order_id  %s " % order_id

    # 参数类型，默认是字符串， unicode
    print(type(order_id))

    # 有的时候，需要对路由做访问优化，订单ID应该是int类型。 @app.route('/order/<int:order_id>')   float


# 4. 启动程序
if __name__ == '__main__':
    # 执行app.run, 就会将Flask程序运行在一个简单的服务器(Flask提供的，用于测试的)
    app.run()