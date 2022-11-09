# Импортировать объект-шаблон из модуля jinja2
from jinja2 import Template

# В начале программы импортировать модуль для построения графиков
import matplotlib.pyplot as plt

# # ----------
# # Задание 1
# # ----------

# # Определить функции для построения графика по спискам координат x и y
# def create_pict(x, y):
#     # Построить линию графика, установить для нее цвет и толщину:
#     line = plt.plot(x, y)
#     plt.setp(line, color="blue", linewidth=2)
#     # Вывести 2 оси, установить их в позицию zero:
#     plt.gca().spines["left"].set_position("zero")
#     plt.gca().spines["bottom"].set_position("zero")
#     plt.gca().spines["top"].set_visible(False)
#     plt.gca().spines["right"].set_visible(False)
#     # Сохранить результат построения в файл:
#     plt.savefig("pict.jpg")
#     # Вернуть имя созданного файла
#     return "pict.jpg"

# # Описать функцию, в качестве параметра передать значение аргумента x
# # функция должна возвращать значение заданной функции, вычисленной от x
# def func(x):
#     return round(pow(x, 3) - 6 * pow(x, 2) + x + 5, 4)


# # Задать начало a и конец b интервала построения функции,
# # количество точек построения.
# a = -2
# b = 6
# n = 30

# # Вычислить шаг
# h = (b - a) / n

# x_list = []
# f_list = []

# # Сформировать список со значениями аргумента
# for i in range(n):
#     x_list.append(round(a + i * h, 4))

# # Сформировать список со значениями функции для
# # каждого элемента списка x_list
# for i in x_list:
#     f_list.append(func(i))

# # Прочитать шаблон из файла function_template.html
# f_template = open('function_template.html', 'r', encoding='utf-8-sig')
# html = f_template.read()
# f_template.close()
#
# # Создать объект-шаблон
# template = Template(html)
#
# template.globals["len"] = len
#
# # Создать файл для HTML-страницы
# f = open('function.html', 'w', encoding='utf-8-sig')
#
# name_pict = create_pict(x_list, f_list)
#
# # Сгенерировать страницу на основе шаблона
# result_html = template.render(x=x_list, y=f_list, len=len, pict=name_pict)
#
# # Вывести сгенерированную страницу в файл
# f.write(result_html)
# f.close()

# # ----------
# # Задание 2
# # ----------

def create_pict(x, y, var):
    # Построить линию графика, установить для нее цвет и толщину:
    line = plt.plot(x, y)
    if var == 0:
        plt.setp(line, color="blue", linewidth=2)
    elif var == 1:
        plt.setp(line, color="yellow", linewidth=2)
    elif var == 2:
        plt.setp(line, color="green", linewidth=2)
    # Вывести 2 оси, установить их в позицию zero:
    plt.gca().spines["left"].set_position("zero")
    plt.gca().spines["bottom"].set_position("zero")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    # Сохранить результат построения в файл:
    plt.savefig("pict.jpg")
    # Вернуть имя созданного файла
    return "pict.jpg"


# Описать функцию, в качестве параметра передать значение аргумента x
# функция должна возвращать значение заданной функции, вычисленной от x
def func_x(x, var):
    if var == 0:
        y = x ** 3 - 6 * x ** 2 + x + 5
    elif var == 1:
        y = x ** 2 - 5 * x + 1
    elif var == 2:
        y = 1 / (x ** 2 + 1)
    return round(y, 4)


# переменная для указания номера варианта функции
n_var = 1
# список с названиями функций
list_name_f = ["f(x)", "y(x)", "z(x)"]
# начало a и конец b интервала построения функции
a = -2
b = 6
# количество точек построения
n = 15

# # Вычислить шаг
h = (b - a) / n

x_list = []
f_list = []

# # Сформировать список со значениями аргумента
for i in range(n):
    x_list.append(round(a + i * h, 4))

# # Сформировать список со значениями функции для
# # каждого элемента списка x_list
for i in x_list:
    f_list.append(func_x(i, n_var))

# Прочитать шаблон из файла function_template.html
f_template = open('functions_template_2.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

# Создать объект-шаблон
template = Template(html)
template.globals["len"] = len

# Создать файл для HTML-страницы
f = open('function_2.html', 'w', encoding='utf-8-sig')

name_pict = create_pict(x_list, f_list, n_var)

# Сгенерировать страницу на основе шаблона
result_html = template.render(a=a, b=b, n=n, x=x_list, y=f_list,
                              list_f=list_name_f, n_var=n_var, pict=name_pict, len=len)

# Вывести сгенерированную страницу в файл
f.write(result_html)
f.close()
