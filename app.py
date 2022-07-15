# Импорт необходимых функций и классов

from flask import Flask, request, render_template
import utils

# Создание приложения Flask с необходимыми представлениями

app = Flask(__name__)


@app.route("/")
def main_page():
    """
    Создает главную страницу
    :return: информация о всех кандидатах
    """
    return render_template('list.html', candidates_list=utils.load_candidates_from_json)


@app.route("/candidate/<int:pk>")
def candidate_page(pk):
    """
    Создает страницу для отдельного кандидата
    :param pk: номер кандидата
    :return: информация о данном кандидате
    """

    pass


@app.route("/skills/<skill_name>")
def skill_page(skill_name):
    """
    Создет страницу для выбранного навыка
    :param skill_name: название навыка
    :return: информация о всех кандидатах, обладающих данным навыком
    """
    pass


if __name__ == "__main__":
    app.run()
