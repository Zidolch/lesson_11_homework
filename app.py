# Импорт необходимых функций и классов

from flask import Flask
import utils

# Создание приложения Flask с необходимыми представлениями

app = Flask(__name__)


@app.route("/")
def main_page():
    """
    Создает главную страницу
    :return: информация о всех кандидатах
    """
    return utils.get_all()


@app.route("/candidate/<int:pk>")
def candidate_page(pk):
    """
    Создает страницу для отдельного кандидата
    :param pk: номер кандидата
    :return: информация о данном кандидате
    """
    picture_url, candidate_info = utils.get_by_pk(pk)
    return f'<img src="({picture_url})">' \
           f'{candidate_info}'


@app.route("/skills/<skill_name>")
def skill_page(skill_name):
    """
    Создет страницу для выбранного навыка
    :param skill_name: название навыка
    :return: информация о всех кандидатах, обладающих данным навыком
    """
    return utils.get_by_skill(skill_name)


if __name__ == "__main__":
    app.run()
