# Задание 1. Написать функцию, которая принимает N целых чисел и возвращает список квадратов этих чисел.
# Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа.
def power_list(*args, pow=2):
    """
    Функция принимает неограниченное кол-во аргументов (целых чисел)
    и возвращает список этих чисел, возведенных в квадрат.
    :param args: int
    :param pow: int, float
    :return: list
    """
    # выполним проверку принадлежности args типу integer
    check_map_args = map(lambda a: isinstance(a, int) == True, args)
    check_list_args = list(check_map_args)
    if len(check_list_args) != sum(check_list_args):
        print('incorrect type of arg(args)')
        return None

    # выполним проверку принадлежности pow типу integer или float
    check_pow = isinstance(pow, (int, float))
    if not check_pow:
        print('incorrect type of pow')
        return None

    return [arg ** pow for arg in args]

# test
print(power_list(2,3,4))
print(power_list(2,3,4, pow=3))
print(power_list(2,3,4, pow='3'))
print(power_list(2,2.0))


# Задание 2. Написать функцию, которая на вход принимает список из целых чисел, и возвращает
# только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента).
#WIP


# Задание 3. Создать декоратор для замера времени выполнения функции.
#WIP

# БОНУСНОЕ ЗАДАНИЕ: создать декоратор, который показывает вложенные входы в функцию.
# Применить на примере вычисления чисел Фибоначчи
#WIP