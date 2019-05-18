from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('landing.html')

@app.route('/sirfameLoginPath', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_login_form()

def do_the_login():
    return 'logging in..'

def show_login_form():
    return render_template('landing.html')

def get_landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')