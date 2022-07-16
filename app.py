# Импорт необходимых функций и классов

from flask import Flask, render_template
import utils

# Создание приложения Flask с необходимыми представлениями

app = Flask(__name__)


@app.route("/")
def main_page():
    """
    Создает главную страницу
    :return: информация о всех кандидатах
    """
    candidates_list = utils.load_candidates_from_json()
    return render_template('list.html', candidates_list=candidates_list)


@app.route("/candidate/<int:id>")
def candidate_page(id):
    """
    Создает страницу для отдельного кандидата
    :param id: номер кандидата
    :return: информация о данном кандидате
    """
    candidate = utils.get_by_id(id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_page(candidate_name):
    """
    Создет страницу для поиска кандидатов по имени
    :param candidate_name: имя кандидата
    :return: информация о всех кандидатах, обладающих данным именем
    """
    named_candidates_list = utils.get_by_name(candidate_name)
    named_candidates_count = len(named_candidates_list)
    return render_template('search.html', candidate_name=candidate_name,
                           named_candidates_list=named_candidates_list,
                           named_candidates_count=named_candidates_count)


@app.route("/skills/<skill_name>")
def skill_page(skill_name):
    """
    Создет страницу для выбранного навыка
    :param skill_name: название навыка
    :return: информация о всех кандидатах, обладающих данным навыком
    """
    skilled_candidates_list = utils.get_by_skill(skill_name)
    skilled_candidates_count = len(skilled_candidates_list)
    return render_template('skill.html', skill_name=skill_name,
                           skilled_candidates_list=skilled_candidates_list,
                           skilled_candidates_count=skilled_candidates_count)


if __name__ == "__main__":
    app.run()
