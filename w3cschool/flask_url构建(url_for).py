from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest/<guest>')

def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

# url_for()函数对于动态构建特定函数的URL非常有用。
# 该函数接受函数的名称作为第一个参数，以及一个或多个关键字(路由的变量)作为参数

if __name__ == '__main__':
   app.run(debug = True)