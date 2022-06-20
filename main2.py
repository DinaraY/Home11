from flask import Flask, request, render_template
from utils import load_candidates, load_candidates_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def pages_index():
    """ Главная страница """
    candidates: list[dict] = load_candidates()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:index>")
def pages_profile(index):
    candidate = load_candidates_id(index)
    # if not candidate:
    #     return "Кандидат не найден"
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def pages_search(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def pages_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template("skill.html", skill=skill_name, candidates=candidates)


app.run()
