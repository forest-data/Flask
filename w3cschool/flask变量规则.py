# Flask变量规则 > 说白了就是URL参数的规则

from flask import Flask
app = Flask(__name__)

# 参数传递用 <> 括起来。

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name
# http://127.0.0.1:5000/hello/Forest

# 用转换器构建URL（int 接受整数  float对于浮点值   path接受用作目录分隔符的斜杠）
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

# 注意 下面的区别  后面是否加了 /      如果是第一个规则，/flask/ URL会产生“404 Not Found”页面
@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'


if __name__ == '__main__':
   app.run(debug = True)

# Werkzeug > 中间件实现者   web服务器 与 web应用程序
# 它是一个WSGI工具包，它实现了请求，响应对象和实用函数。 这使得能够在其上构建web框架。 Flask框架使用Werkzeug作为其基础之一。