from membfuncs import trapeze


class DistanceController:
    """
    Цей клас моделює систему, що контролює дистанцією між автомобілями.
    """

    sets = []
    delta = 0

    def __init__(self, sets, delta):
        """
        :param sets: містить кортежі розміром 4,
                котрі визначають множини дистанцій (точки трапеції в функції належності)
        :param delta: параметр, який корегує зміну дистанції
        """
        self.sets = sets
        self.delta = delta

    def adjust_distance(self, distance):
        """
        Корегує дистанцію
        Використовується формула: S = S + (F1(d) * delta) - (F2(d) * delta), де
        F1(d) - функція належності для множини "близько"
        F2(d) - функція належності для множини "далеко"

        :param distance: дистанція в даний момент часу
        :return: дистанція, після роботи контролера
        """
        sets = self.sets
        set1 = sets[0]
        set2 = sets[1]

        lower = set1[3]
        upper = set2[0]

        while distance < lower or distance > upper:
            distance += (trapeze(distance, set1[0], set1[1], set1[2], set1[3])
                         - trapeze(distance, set2[0], set2[1], set2[2], set2[3])) * self.delta

        return distance
