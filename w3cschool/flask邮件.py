# Flask Mail - 为Flask应用程序提供SMTP接口

# 步骤1 - 在代码中从flask-mail模块导入Mail和Message类。
from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

# 步骤2 - 然后按照以下设置配置Flask-Mail。
app.config['MAIL_SERVER']='smtp.gmail.com'   # 电子邮件服务器的名称/IP地址
app.config['MAIL_PORT'] = 465    #  使用的服务器的端口号
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'   # 发件人的用户名
app.config['MAIL_PASSWORD'] = '*****'    # 发件人的密码
app.config['MAIL_USE_TLS'] = False    # 启用/禁用传输安全层加密
app.config['MAIL_USE_SSL'] = True    # 启用/禁用安全套接字层加密

# 步骤3 - 创建Mail类的实例。
mail = Mail(app)

# 步骤4 - 在由URL规则（‘/’）映射的Python函数中设置Message对象。
@app.route("/")
def index():
   msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['id1@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"

   # Mail类
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)