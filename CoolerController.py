from membfuncs import trapeze

class CoolerController:
    """
    Цей клас моделює систему, що керує кулером комп'ютера.
    """

    sets = []
    delta = 0 # параметр, який корегує швидкість кулера: delta = max_speed / len(sets), де len(sets)
              # кількість множин, на які розбивається лінгвістична змінна "температура"

    def __init__(self, sets, max_speed):
        """
        :param sets: містить кортежі розміром 4,
                котрі визначають множини температури (точки трапеції в функції належності)
        :param max_speed: максимальна швидкість кулера (оберти за хвилину).
        """
        self.sets = sets
        self.delta = max_speed / len(sets)

    def fan_speed(self, temperature):
        """
        Розраховує швидкість кулера, для підтримки отпимальної температури.
        Використовується формула: S = Fi(t) * i * delta, де Fi(t) - функція належності і-ї множини,
        t - температура, i - номер множини.

        :param temperature: температура
        :return: швидкість кулера (оберти за хвилину)
        """
        sets = self.sets
        speed = 0

        for i in range(sets):
            tuple = sets[i]
            speed += trapeze(temperature, tuple[0], tuple[1], tuple[2], tuple[3]) * (i + 1) * self.delta

        return speed