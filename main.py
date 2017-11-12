from CoolerController import CoolerController

import random
import matplotlib.pyplot as plt


def demo_controller(controller, count):
    """
    Демонстрація роботи контролера кулера

    :param controller: об'єкт класу CoolerController
    :param count: кількість ітерацій для демо
    """
    last = len(controller.sets) - 1
    t_last = len(controller.sets[last]) - 1

    lower = controller.sets[0][0]  # найменша температура
    upper = controller.sets[last][t_last]  # найбільша температура

    t_list = []  # список температур
    s_list = []  # список швидкостей

    for i in range(count):
        temperature = random.randint(lower, upper)  # генерація випадкової температури
        t_list.append(temperature)
        s_list.append(controller.fan_speed(temperature))

    draw_membfunc(controller.sets)
    draw_plots(t_list, s_list)
    plt.show()


def draw_plots(t_list, s_list):
    """
    Виводить графіки температур і швидкостей кулера

    :param t_list: список температур
    :param s_list: список швидкостей
    """
    plt.figure(2)
    plt.subplot(211)
    plt.plot(t_list)
    plt.ylabel('temperature')
    plt.xlabel('index')

    plt.subplot(212)
    plt.plot(s_list)
    plt.ylabel('fan speed')
    plt.xlabel('index')


def draw_membfunc(t_sets):
    """
    Виводить графіки функцій належності

    :param t_sets: список множин "температури"
    """
    xs = [0, 33, 66, 100]

    plt.figure(1)
    for set in t_sets:
        plt.plot(set, [0, 1, 1, 0])

    plt.xlabel('temperature')
    plt.ylabel('DOM')
    plt.axis([0, 100, 0, 2])


# Клієнтський код
temperature_sets = [
    (0, 25, 25, 25),
    (26, 50, 50, 50),
    (51, 75, 75, 75),
    (76, 100, 100, 100)
]

max_speed = 6000

demo_it_count = 100

controller = CoolerController(temperature_sets, max_speed)
demo_controller(controller, demo_it_count)