from flask import Flask, render_template
from random import randint

app = Flask(__name__)

heros = ['黑暗之女', "狂战士", "正义巨像", "卡牌大师", "德邦总管", "无畏战车", "诡术妖姬", "猩红收割者", "远古恐惧",
         "正义使者", "无极剑圣", "牛头酋长", "符文法师", "亡灵战神", "战争女神", "众星之子"]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/index')
def index():
    return render_template("index.html", heros=heros)


@app.route('/choujiang')
def choujiang():
    num = randint(0, len(heros))
    return render_template("index.html", heros=heros, hero=heros[num])


if __name__ == '__main__':
    app.run(debug=True)
