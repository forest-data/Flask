# Session（会话）数据存储在服务器上。
# 会话是客户端登录到服务器并注销服务器的时间间隔（作用的时间段）。 需要在该会话中保存的数据会存储在服务器上的临时目录中。

# Cookies 和 Session 的相同点和不同点
# 相同点 > 1. 目的都是 跟踪用户使用的数据，以获得更好的访问者体验和网站统计信息。  2. 都是一个字典对象
# 不同点 > cookies 将数据存放在客户端   session将数据存放在服务器端
# 为每个客户端的会话分配会话ID。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。对于此加密，Flask应用程序需要一个定义的SECRET_KEY。

from flask import Flask, make_response, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
   if 'username' in session:
       username = session['username']
       return """Logged in as &plus; username &plus; '<br>' &plus; \
          "<b><a href = '/logout'>click here to log out</a></b>"""

   return """You are not logged in <br><a href = '/login'></b>" &plus; \
      "click here to log in</b></a>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''

   <form action = "" method = "post">
      <p><input type = text name = username/></p>
      <p<<input type = submit value = Login/></p>
   </form>

   '''