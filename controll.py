from flask import Flask,send_file
from flask import render_template
import os
from flask import send_from_directory

app = Flask(__name__)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)))

@app.route('/welcome_xiaoyue')
def index():
        # return render_template("index.html")
        # return send_from_directory(root, "index.html")
        return send_file("./index.html")
        
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)