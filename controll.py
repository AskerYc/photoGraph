from flask import Flask,send_file
from flask import render_template
import os
from flask import send_from_directory

app = Flask(__name__)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)))

@app.route('/jinrong')
def index():
        # return render_template("index.html")
        # return send_from_directory(root, "index.html")
        return send_file("./index.html")

@app.route('/css/style.css')
def index1():
        return send_file("./css/style.css")
        
@app.route('/img/01.png')
def index2():
        return send_file("./img/01.png")

@app.route('/img/02.png')
def index3():
        return send_file("./img/02.png")
        
@app.route('/img/03.png')
def index4():
        return send_file("./img/03.png")
        
@app.route('/img/04.png')
def index5():
        return send_file("./img/04.png")

@app.route('/img/05.png')
def index6():
        return send_file("./img/05.png")
        
@app.route('/img/06.png')
def index7():
        return send_file("./img/06.png")
        
@app.route('/img/1.png')
def index8():
        return send_file("./img/1.png")

@app.route('/img/2.png')
def index9():
        return send_file("./img/2.png")
        
@app.route('/img/3.png')
def index10():
        return send_file("./img/3.png")
        
@app.route('/img/4.png')
def index11():
        return send_file("./img/4.png")

@app.route('/img/5.png')
def index12():
        return send_file("./img/5.png")
        
@app.route('/img/6.png')
def index13():
        return send_file("./img/6.png")
        
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8088)
