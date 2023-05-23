# 让我们的电脑可以支持服务访问
# 需要一个web 框架
# pip install Flask  在命令行里面

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

heros = ['黑暗之女', "狂战士", "正义巨像", "卡牌大师", "德邦总管", "无畏战车", "诡术妖姬", "猩红收割者", "远古恐惧",
         "正义使者", "无极剑圣", "牛头酋长", "符文法师", "亡灵战神", "战争女神", "众星之子"]


@app.route("/hello")
def index():
    return render_template('index.html', heros=heros)


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
