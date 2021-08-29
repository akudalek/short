# -*- coding: utf-8 -*-

import pandas as pd

from src.getenvironment import logger
from src.database.model import session, Cats


def read_cat(**kwargs) -> Cats:
    """
    Получение данных из БД по котам
    :param kwargs:
    :return:
    """
    try:
        logger.info(f"Получаем информацию по коту с параметрами {kwargs}")
        return session.query(Cats).filter_by(**kwargs).first()

    except Exception as e:
        logger.error(f"Ошибка по получение кота из БД {e}")
        result = Cats()

    logger.info(f"Выгрузка по коту с {kwargs}\n{result}")
    return result


def search_cats(**kwargs) -> Cats:
    """
    Получение данных из БД по котам
    :param kwargs:
    :return:
    """
    try:
        logger.info(f"Ищем котов с параметрами{kwargs}")
        result = session.query(Cats).filter_by(**kwargs).order_by(Cats.id)

    except Exception as e:
        logger.error(f"Ошибка по получение котов из БД {e}")
        result = Cats()

    logger.info(f"Поиск котов с параметрами {kwargs}\n{result}")
    return result


def read_all_cats_image() -> list:
    """
    Получение данных из БД по котам картинки
    :return:
    """
    try:
        logger.info(f"Получаем информацию по котам с картинками")
        result = session.query(Cats.id, Cats.img)

    except Exception as e:
        logger.error(f"Ошибка по получение кота из БД {e}")
        result = Cats()

    logger.info(f"Выгрузка по котам картинки \n{result}")
    return result


def count_cats() -> int:
    """
    Получение информацию по кол-ву котов для пагинации
    :param kwargs:
    :return:
    """
    try:
        logger.info(f"Получаем информацию по кол-ву котов в БД")
        result = pd.read_sql(
            sql=session.query(Cats).statement,
            con=session.bind
        )
    except Exception as e:
        logger.error(f"Ошибка по получение информации по кол-ву котов в БД {e}")
        result = pd.DataFrame()

    logger.info(f"Кол-во котов равно {len(result)}")
    return len(result)


if __name__ == '__main__':
    import os
    import random
    names = ["Абрикос", "Веник", "Фунтик", "Изюмик", "Лавашик", "Зефир"]
    breeds = ["Бурманская кошка", "Норвежский лесной кот", "Мейн-Кун", "Американский керл"]
    descriptions = ["Описание 1", "Описание 2", "Описание 3", "Описание 4", "Описание 5"]

    for _ in range(2):
        for i, name_file in enumerate(os.listdir("../../static/templates/img/")):

            with open(f"../../static/templates/img/{name_file}", 'rb') as file:
                session.add(
                    Cats(

                        name=random.choice(names),
                        breed=random.choice(names),
                        age=random.choice(range(10)),
                        description=random.choice(descriptions),
                        img=file.read()
                    )
                )

                session.commit()