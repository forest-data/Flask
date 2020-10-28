# Http协议是万维网中数据通信的基础。在该协议中定义了从指定URL检索数据的不同方法。
# Flask路由响应GET请求
# 可以通过为route()装饰器提供methods参数来更改此首选项

# jinja2.exceptions.TemplateNotFound
# 第一种情况：
#   没有templates文件夹，因为默认情况下，Flask在程序文件夹中的templates子文件夹中寻找模板。
# 解决方案：
#   在程序文件夹下边新建一个templates文件夹，将index.html和user.html模板文件放进

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')    # args是包含表单参数对及其对应值对的列表的字典对象。
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)