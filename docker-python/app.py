from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title='Docker Python', name='James')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['PORT']) # Chạy project ở PORT nhận vào từ biến môi trường
 # host=0.0.0.0 để nói với project rằng cho phép tất cả các ip truy cập (nếu không có thì chỉ bên trong 
 # container, ta gọi localhost ở máy host cũng không truy cập dc)
 # port=os.environ['PORT']) để chạy project ở PORT nhận vào từ biến môi trường