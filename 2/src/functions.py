import math
from base64 import b64encode

from src.database.model import Cats
from src.database.service import read_cat, read_all_cats_image
from src.getenvironment import show_pagination


def get_list_sheets(count_sheets=10, number_sheets=0):
    """
    Функция формирования словаря для пагинации
    :param count_sheets: Кол-во страниц пагинации
    :param number_sheets: Номер страницы - текущий
    :return: Словарь для пагинации на UI
    """
    count_sheets = count_sheets if count_sheets >= 0 else 0
    count_sheets = math.ceil(count_sheets)
    show_pag = show_pagination - ((show_pagination + 1) % 2)

    # старт конец для отображение пагинации
    start = number_sheets // show_pag * show_pag
    end = start + show_pag

    # Страницы первая и последняя
    start_0 = 0
    end_last = count_sheets

    # Страницы предыдущая и последующая
    count_sheets += 1
    if start - show_pag < 0:
        start_pre = 0
        end_pre = start_pre + show_pag
        start = 0
        end = start + show_pag

    elif start + show_pag > count_sheets:
        start = start
        end = count_sheets + 1
        start_pre = start - show_pag
        end_pre = end - 1
    else:
        start_pre = start - show_pag
        end_pre = end + show_pag

    end_pre = end_pre if end_pre < count_sheets else end if end < count_sheets else count_sheets - 1
    end_pre = 0 if end_pre < 0 else end_pre

    list_show = list(range(count_sheets)[start:end])

    dict_show = {"Первая": start_0,
                 "Предыдущая": start_pre}
    dict_show.update({i + 1: i for i in list_show})
    dict_show.update({
        "Следующая": end_pre,
        "Последняя": end_last
    })

    return dict_show


def get_cats_image():
    """
    Транспонирование всех картинок в base64 для отображения на UI
    :param kwargs:
    :return:
    """
    return [
            Cats(id=cat.id,
                 img=b64encode(cat.img).decode("utf-8") if cat.img else None)
            for cat in read_all_cats_image()
       ]


if __name__ == '__main__':
    print(
        get_cats_image()[0:0+5]
    )
