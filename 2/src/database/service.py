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


def read_all_cats_image() -> list:
    """
    Получение данных из БД по котам картинки
    :return:
    """
    try:
        logger.info(f"Получаем информацию по котам с картинками")
        return session.query(Cats.id, Cats.img)

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
    print(
        read_all_cats_image()[0].img
    )