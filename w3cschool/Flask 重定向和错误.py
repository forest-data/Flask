# redirect()函数用于在登录尝试失败时再次显示登录页面。

#
from flask import Flask, redirect, url_for, render_template, request, abort

# Initialize the Flask application
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('login.html')
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST' and request.form['nm'] == 'admin':
#         return redirect(url_for('success'))
#     return redirect(url_for('index'))
#
#
# @app.route('/success')
# def success():
#     return 'logged in successfully'


@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      if request.form['nm'] == 'admin' :
         return redirect(url_for('success'))
      else:
         abort(401)
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
   app.run(debug = True)

