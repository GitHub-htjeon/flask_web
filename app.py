from flask import Flask, render_template,request

app = Flask(__name__)

# 경로지정 () 후 함수실행 데이터 실어보내기, (@app.route 방식 다른방식 중 하나)
# @app.get('/')
@app.route('/')
def index():
    #return "<h1>Hellow World!</h1>"
    print(request.headers)
    return render_template('index.html', data =request.headers)

if __name__ == "__main__":
    app.run(debug = True , port=8000)
