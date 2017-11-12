from DistanceController import DistanceController

import random
import matplotlib.pyplot as plt


def demo_controller(controller, count):
    """
    Демонстрація роботи контролера, котрий регулює дистанцію між автомобілями

    :param controller: об'єкт класу DistanceController
    :param count: кількість ітерацій для демо
    """
    last = len(controller.sets) - 1
    d_last = len(controller.sets[last]) - 1

    lower = controller.sets[0][0]  # найменша дистанція
    upper = controller.sets[last][d_last]  # найбільша дистанція

    b_list = []  # список дистанцій до
    e_list = []  # список дистанцій після

    for i in range(count):
        distance = random.randint(lower, upper)  # генерація випадкової дестанції до роботи контролера
        b_list.append(distance)
        e_list.append(controller.adjust_distance(distance))

    draw_membfunc(controller.sets)
    draw_plots(b_list, e_list)
    plt.show()


def draw_plots(b_list, e_list):
    """
    Виводить графіки дистанцій до і після роботи контролера

    :param b_list: список дистанцій до
    :param e_list: список дистанцій після
    """
    plt.figure(2)
    plt.subplot(211)
    plt.plot(b_list)
    plt.ylabel('distance before')
    plt.xlabel('index')

    plt.subplot(212)
    plt.plot(e_list)
    plt.ylabel('distance after')
    plt.xlabel('index')


def draw_membfunc(d_sets):
    """
    Виводить графіки функцій належності

    :param d_sets: список множин "дистанцій"
    """
    max = d_sets[1][3]

    xs = [0, max / 3, 2 * max / 3, max]

    plt.figure(1)
    for set in d_sets:
        plt.plot(set, [0, 1, 1, 0])

    plt.xlabel('Distance, m')
    plt.ylabel('DOM')
    plt.axis([0, max, 0, 2])


# Клієнтський код
distance_sets = [
    (0, 0, 2.5, 3),  # близько
    (4, 4.5, 7, 7)   # далеко
]

delta = 1
demo_it_count = 100

controller = DistanceController(distance_sets, delta)
demo_controller(controller, demo_it_count)