''''''
'''
Домашнее задание по теме "Обзор сторонних библиотек Python"
Цель: познакомиться с использованием сторонних библиотек в Python и применить их в различных задачах.

Задача:
Выберите одну или несколько сторонних библиотек Python, например, 
requests, 
pandas, 
numpy, 
matplotlib, 
pillow.

Если вы выбрали:
requests - запросить данные с сайта 
и вывести их в консоль.

pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) 
и вывести результаты в консоль.

numpy - создать массив чисел, выполнить математические операции с массивом 
и вывести результаты в консоль.

matplotlib - визуализировать данные с помощью библиотеки 
любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, 
применить эффекты и сохранить в другой формат.
Желательно продемонстрировать от 
3-х функций/классов/методов/операций из каждой выбранной библиотеки.
Файл module_11_1.py и загрузите его на ваш GitHub репозиторий. 
В решении пришлите ссылку на него и комментарий к использованным инструментам библиотек(-и).
'''
import requests as rq
import pandas as pd
from datetime import date
import numpy as np
import matplotlib.pyplot as plt


URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
# метод get (библиотека requests): получение данных с сайта в формате JSON
requ = rq.get(URL).json()
print(f'requests {"*" * 5} Вывод запроса {URL} данных сайта: {"*" * 5}\n {requ}')
print()

##метод read_json (библиотека pandas): получение данных с сайта в формате JSON
# и считывает JSON-файл с диска и создает объект DataFrame df
df = pd.read_json(URL)

print(f'pandas {"*" * 5} Вывод запроса {URL} данных сайта '
      f'в массив данных {"*" * 5}\n {df}')
print()
# to_numpy (библиотека pandas):  Преобразование DataFrame в массив NumPy,
# выводим 4 колонку с df с данными валют
np_array = df.to_numpy()[:, 4]
print(f'pandas {"*" * 5} Преобразование df(DataFrame) в массив np_array(NumPy) '
      f'в c данными валют {"*" * 5}\n {np_array} \n\t {type(np_array)}')
print()
# элемент (библиотека numpy):преобразование массива np_array в список, где каждый элемент -
# словарь с данными валюты
# 6 элементов (для наглядности гиксограммы)
list_dict = list(np_array[: 6])
print(
    f'numpy {"*" * 5} преобразование массива np_array в список,где каждый элемент массива -словарь с данными валюты, \n'
    f'6 элементов (для наглядности гиксограммы) {"*" * 5}\n {list_dict}')
print()
# DataFrame (библиотека pandas):  Преобразование словаря list_dict в массив DataFrame (data_value),
# выводим в массив необходимые данные валют
data_value = pd.DataFrame(list_dict, columns=['Name', 'CharCode', 'NumCode', 'Nominal', 'Value', 'Previous'])
#сортировка данных массива по Name - названию валют
data_value = data_value.sort_values(by='Name')
print(f'pandas {"*" * 5} Преобразование словаря list_dict в массив DataFrame (data_value) '
      f'в c данными валют {"*" * 5}\n {data_value} \n\t {type(data_value)}')
print()
#Дата формирования отчёта
date_cur = date.today().strftime('%y.%m.%d')

#ExcelWriter (библиотека pandas): запись данных data_value в файл xls, на страницу файла
with pd.ExcelWriter(f'val_{date_cur}.xlsx') as writer:
    data_value.to_excel(writer, sheet_name=str({date_cur}))
print(f'pandas ExcelWriter{"*" * 5} Запись данных data_value в файл xls, на страницу файла '
      f'в c данными валют {"*" * 5}\n val_{date_cur}.xlsx')
print()

#read_excel (библиотека pandas): чтение данных из exel
chart_file = pd.read_excel(f'val_{date_cur}.xlsx')

#title (библиотека matplotlib интерфейс pyplot): задание заголовка гиксограммы
date_cur = date.today().strftime('%d.%m.%y')
plt.title(f'Курс валют на {date_cur}')
#xlabel (библиотека matplotlib интерфейс pyplot): задание названия оси x гиксограммы
plt.xlabel('Валюта')
#ylabel (библиотека matplotlib интерфейс pyplot): задание названия оси y гиксограммы
plt.ylabel('Курс')
'''
Данные для построения нескольких столбчатых диаграмм берутся в список.
'''
#для оси x
x = chart_file['CharCode']
#для оси y
y1 = chart_file['Previous']
#для оси y
y2 = chart_file['Value']

'''
Функция np.arange( ) из библиотеки numpy используется для создания диапазона значений. 
Cоздаем значения по оси X в зависимости от количества групп.
'''
#arange (библиотека pandas): Cоздаем значения по оси X в зависимости от количества групп.
x_axis = np.arange(len(x))
'''
Построение нескольких столбчатых диаграмм с помощью функции plt.bar( ).
Чтобы избежать перекрытия столбиков в каждой группе, 
столбики сдвинуты на -0,2 единицы и +0,2 единицы по оси X.
Ширина столбиков каждой группы принимается равной 0,4 единицы.
В каждой группе построены множественные столбчатые диаграммы как для Покупка, так и для Продажа.
'''
#bar (библиотека matplotlib): построена столбчатая диаграмма для Покупка.
plt.bar(x_axis - 0.2, y1, 0.4, label='Покупка')
#bar (библиотека matplotlib): построена столбчатая диаграмма для Продажа.
plt.bar(x_axis + 0.2, y2, 0.4, label='Продажа')
'''
установить текущие положения делений и метки оси X.
'''
plt.xticks(x_axis, x)
# plt.legend()
plt.show()
exit()
