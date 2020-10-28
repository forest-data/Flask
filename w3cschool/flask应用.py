from flask import Flask
app = Flask(__name__)    # 确定资源所在的路径

@app.route('/')     # route类实现url+函数 绑定
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()    # run()方法在本地开发服务器上运行应用程序。

# WSGI > 规范
# Web Server Gateway Interface（Web服务器网关接口，WSGI）
# Web开发，浏览器发送请求 > 服务器 > 服务器处理响应


# app.add_url_rule(‘/’, ‘hello’, hello_world)  也可用于路由绑定
# def hello_world():
#    return ‘hello world’
# app.add_url_rule(‘/’, ‘hello’, hello_world)