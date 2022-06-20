import json


def load_candidates():
    """ Загружает кандидатов из файла в список """
    with open("candidates.json", 'r', encoding="utf-8") as f:
        candidates = json.load(f)

    return candidates


load_candidates = load_candidates()


def load_candidates_from_json(id: int):
    """Выводит информацию о кандидате по id"""
    for i in load_candidates:
        if id == i["id"]:
            return f"{i['name']}"



def load_name_candidates():
    """ Выводит список кандидатов"""
    spisok = []
    for i in load_candidates:
        spisok.append(
            f"""<pre>Имя кандидата - {i['name']}</pre>""")

    return f"{' '.join(spisok)}"


print(load_name_candidates())


def page_profile(id: int):
    """Выводит информацию о кандидате по id"""
    for i in load_candidates:
        if id == i["id"]:
            return i["picture"], i['name'], i['position'], i['skills'].lower()


def page_names(name):
    """Выводит кандидатов по имени"""
    names = []
    for i in load_candidates:
        if name.lower() in i["name"].lower():
            names.append(
                f"""Имя кандидата - {i['name']}\nПозиция кандидата {i['position']}\nНавыки {i['skills']}""")
    return ''.join(names)


def page_skills(skill):
    """Выводит кандидатов по навыку"""
    skills = []
    for i in load_candidates:
        if skill.lower() in i["skills"].lower().split(", "):
            skills.append(
                f"""Имя кандидата - {i['name']}\nПозиция кандидата {i['position']}\nНавыки {i['skills']}""")
    return ''.join(skills)
