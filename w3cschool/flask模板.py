from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('hello.html')

@app.route('/')
def index():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('hello.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )

# 模板中的取值 . []

if __name__ == '__main__':
   app.run(debug = True)