import json


def load_candidates():
    """ Загружает кандидатов из файла в список """
    with open("candidates.json", 'r', encoding="utf-8") as f:
        return json.load(f)


def load_candidates_id(id: int):
    """Выводит информацию о кандидате по id"""
    for i in load_candidates():
        if id == i["id"]:
            return i


def get_candidates_by_name(name):
    """Выводит кандидатов по имени"""
    names = []
    for i in load_candidates():
        if name.lower() == i["name"].lower():
            names.append(i)
    return names


def get_candidates_by_skill(skill):
    """Выводит кандидатов по навыку"""
    skills = []
    for i in load_candidates():
        if skill.lower() in i["skills"].lower().split(", "):
            skills.append(i)
    return skills
