# 在 Flask 中处理文件上传非常简单。它需要一个 HTML 表单，其 ​enctype​ 属性设置为“​multipart / form-data”​，将文件发布到 URL。
# URL 处理程序从 ​request.files[]​ 对象中提取文件，并将其保存到所需的位置。


# java小例子： int a=2,b=2;
# 硬编码：if(a==2) return false;
# 不是硬编码 if(a==b) return true;
# 不过软编码比硬编码要复杂一些，对以后的考虑要周到一些。
# 软编码是一种设计，而硬编码不过是一种具体的实现。

# app.config[‘UPLOAD_FOLDER’] 定义上传文件夹的路径
# app.config[‘MAX_CONTENT_PATH’] 指定要上传的文件的最大大小（以字节为单位）


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/upload'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run()