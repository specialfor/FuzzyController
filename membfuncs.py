def trapeze(value, left, left_trap, right_trap, right):
    """
     Membership function which models trapeze profile
     e.g
     ^                     ^
     |* * * *              |  ******
     |*      *             | *       *
     |*       *            |*          *
     ----------->    or    ---------------->

     ----------------------------------------------------

     Функція належності, котра схожа на трапецію
    :param value: значення параметру
    :param left: ліва нижня точка
    :param left_trap: ліва верхня точка
    :param right_trap: права верхня точка
    :param right: права нижня точка
    :return: число в діапазоні [0, 1]
    """
    if value < left or value > right:
        return 0
    elif left <= value < left_trap:
        return (value - left) / (left_trap - left)
    elif left_trap <= value <= right_trap:
        return 1
    elif right_trap < value <= right:
        return (value - right) / (right - right_trap)