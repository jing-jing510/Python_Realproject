from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/login')
def login():

    return render_template("login.html")


@app.route('/index')
def index():  # put application's code here
    username = request.args.get("username")
    return f"主页!!欢迎登录 {username}"


if __name__ == '__main__':
    app.run(debug=True)
