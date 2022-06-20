from flask import Flask, request, render_template
from utils import load_name_candidates, load_candidates_from_json, page_profile

app = Flask(__name__)


@app.route("/")
def pages_index():
    """ Главная страница """
    return render_template("list.html", name1=load_candidates_from_json(1), name2=load_candidates_from_json(2),
                           name3=load_candidates_from_json(3), name4=load_candidates_from_json(4),
                           name5=load_candidates_from_json(5), name6=load_candidates_from_json(6),
                           name7=load_candidates_from_json(7))


@app.route("/candidates/<int:index>")
def pages_profile(index):
    return render_template("single.html", index=page_profile(index))


# @app.route('/')
# def index():
#     return render_template("list.html", name="Adela Hendricks")


app.run()
