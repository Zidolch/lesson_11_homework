# Импорт необходимого модуля

import json

# Определение необходимой константы

CANDIDATES_FILE = 'candidates.json'


def load_candidates_from_json(filename=CANDIDATES_FILE):
    """
    Читает файл с данными кандидатов
    :param filename: имя файла
    :return students_list: список словарей с данными кандидатов
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list


def get_by_id(id, candidates_list=load_candidates_from_json()):
    """
    Выводит данные об одном кандидате
    :param id: номер кандидата
    :param candidates_list: список кандидатов
    :return: данные кандидата
    """
    for candidate in candidates_list:
        if candidate["id"] == id:
            return candidate


def get_by_skill(skill_name, candidates_list=load_candidates_from_json()):
    """
    Выводит данные о всех кандидатах, обладающих определенным навыком
    :param skill_name: название навыка
    :param candidates_list: список кандидатов
    :return: данные о всех кандидатах, обладающих данным навыком
    """
    skilled_candidates_list = []
    for candidate in candidates_list:
        if skill_name.lower() in candidate["skills"].lower():
            skilled_candidates_list.append(candidate)
    return skilled_candidates_list


def get_by_name(name, candidates_list=load_candidates_from_json()):
    """
    Выводит данные о всех кандидатах, обладающих определенным именем
    :param name: имя кандидата
    :param candidates_list: список кандидатов
    :return: данные о всех кандидатах, обладающих данным именем
    """
    named_candidates_list = []
    for candidate in candidates_list:
        if name.lower() in candidate["skills"].lower():
            named_candidates_list.append(candidate)
    return named_candidates_list
