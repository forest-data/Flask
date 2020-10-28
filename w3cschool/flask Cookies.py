# Cookie以文本文件的形式存储在客户端的计算机上。
# 其目的是记住与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。

from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool", "w3cshool",max_age=3600)
    return resp

@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("w3cshool")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1

@app.route("/delete_cookies")    # 删除cookie
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("w3cshool")

    return resp

if __name__ == '__main__':
    app.run(debug=True)