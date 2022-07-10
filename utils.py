# Импорт необходимого модуля

import json

# Определение необходимой константы

CANDIDATES_FILE = 'candidates.json'


def load_candidates(filename=CANDIDATES_FILE):
    """
    Читает файл с данными кандидатов
    :param filename: имя файла
    :return students_list: список словарей с данными кандидатов
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        candidates_list = json.load(file)
    return candidates_list


def get_all(candidates_list=load_candidates()):
    """
    Выводит данные о навыках, должности и имени кандидатов
    :param candidates_list: список каднидатов
    :return: данные о всех кандидатах
    """
    candidates = ''
    for candidate in candidates_list:
        candidates += f'<pre>' \
                      f'Имя кандидата: {candidate["name"]}\n' \
                      f'{candidate["position"]}\n' \
                      f'{candidate["skills"]}\n\n' \
                      f'</pre>'
    return candidates


def get_by_pk(pk, candidates_list=load_candidates()):
    """
    Выводит данные об одном кандидате
    :param pk: номер кандидата
    :param candidates_list: список кандидатов
    :return: изображение кандидата, данные кандидата
    """
    candidate = [candidates_list[pk]]
    return candidate[0]["picture"], get_all(candidate)


def get_by_skill(skill_name, candidates_list=load_candidates()):
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
    return get_all(skilled_candidates_list)
