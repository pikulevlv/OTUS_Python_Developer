from flask import Flask,request, redirect, render_template
from views import employee_blueprint_app
# from views.employee import employee_app

app = Flask(__name__)

app.register_blueprint(employee_blueprint_app, url_prefix="/employees")



@app.route("/", methods=['POST', 'GET'])
def index():
    user = "Stranger"
    if request.method == 'POST':
        user = request.form.get('user', 'guest')
    browser = request.headers.get('User-Agent')
    return render_template('index.html', browser=browser, user=user)


# @app.route("/user/<name>/")
# def user(name):
#     return f'<h1>Hello, {name}!</h1>'