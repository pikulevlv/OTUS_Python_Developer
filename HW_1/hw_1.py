# Задание 1. Написать функцию, которая принимает N целых чисел и возвращает список квадратов этих чисел.
# Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа.
def power_list(*args, power=2):
    """
    Функция принимает неограниченное кол-во аргументов (целых чисел)
    и возвращает список этих чисел, возведенных в квадрат.
    :param args: int
    :param power: int, float
    :return: list
    """
    # выполним проверку принадлежности args типу integer
    check_map_args = map(lambda a: isinstance(a, int), args)
    check_list_args = list(check_map_args)
    if len(check_list_args) != sum(check_list_args):
        print('ERROR! Incorrect type of arg(args).')
        return None

    # выполним проверку принадлежности power типу integer или float
    check_pow = isinstance(power, (int, float))
    if not check_pow:
        print('ERROR! Incorrect type of power.')
        return None

    return [pow(arg,power) for arg in args]

# test
print('*'*20, 'Task #1', '*'*20)
print('Передаем args, но не указываем power\n', power_list(2,3,4))
print('-'*5)
print('Передаем args и указываем power=3\n',power_list(2,3,4, power=3))
print('-'*5)
print('Передаем args и power передаем как строку\n',power_list(2,3,4, power='3'))
print('-'*5)
print('Передаем args, один из которых типа float\n',power_list(2,2.0))
print('-'*5)

# Задание 2. Написать функцию, которая на вход принимает список из целых чисел, и возвращает
# только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента).
FILTER_METHODS = ('even', 'odd', 'prime',)

def filter_num_list(num_list=None, filter_method=FILTER_METHODS[0]):
    """
    Функция принимает список целых чисел и возвращает в зависимости от выбранного метода
    список, эелементы которого являются четными, нечетными, простыми числами.
    :param num_list: list with int elements
    :param filter_method: has 3 values: 'even'(default), 'odd', 'prime'
    :return: list
    """
    #  проверяем, что параметр передан
    if num_list is None:
        print("ERROR! The list isn't passed, but required.")
        return
    # проверяем, что num_list это список
    elif not isinstance(num_list, list):
        print("ERROR! Num_list isn't list type.")
        return
    # проверяем, что список содержит все integer
    elif sum(isinstance(e, int) for e in num_list) != len(num_list):
        print("ERROR! Not all elements have integer type.")
        return
    else:
        pass
    # проверяем переданный параметр, указывающий метод фильтрации, и обрабатываем список
    if filter_method == FILTER_METHODS[0]:
        return list(filter(lambda x: x%2 == 0, num_list))
    elif filter_method == FILTER_METHODS[1]:
        return list(filter(lambda x: x%2 != 0, num_list))
    elif filter_method == FILTER_METHODS[2]:
        prime_list = []
        for num in num_list:
            divider_list = [i for i in range(1,num+1)]

            if sum(num % d == 0 for d in divider_list) == 2:
                prime_list.append(num)
        return prime_list
    else:
        print("ERROR! An incorrect filter method was chosen.")
        return
# test
print('*'*20, 'Task #2', '*'*20)
print('Не передаем список при вызове функции')
print(filter_num_list())
print('-'*5)
print('Передаем корректный список при вызове функции')
print(filter_num_list([1,2,3,4]))
print('-'*5)
print('Передаем список, в котором один элемент типа float')
print(filter_num_list([1,2,3.1]))
print('-'*5)
print('Передаем список, в котором один элемент типа string')
print(filter_num_list([1,2,'3.1']))
print('-'*5)
print('Передаем кортеж вместо списка')
print(filter_num_list((1,2,3)))
print('-'*5)
print('Передаем список, но делаем ошибку в указании параметра фильтрации')
print(filter_num_list([1,2,3,4,5], filter_method='eve'))
print('-'*5)
print('Передаем список и параметр фильтрации - even (четные)')
print(filter_num_list([1,2,3,4,5], filter_method=FILTER_METHODS[0]))
print('-'*5)
print('Передаем список и параметр фильтрации - odd (нечетные)')
print(filter_num_list([1,2,3,4,5], filter_method=FILTER_METHODS[1]))
print('-'*5)
print('Передаем список с положительными и отрицательными integer и параметр фильтрации - prime (простые числа)')
print(filter_num_list([-2,-1,0,1,2,3,4,5,6,7,8,9,10,11], filter_method=FILTER_METHODS[2]))

# Задание 3. Создать декоратор для замера времени выполнения функции.

def time_decorator(func):
    from time import time
    def new_func(*args, **kwargs):
        """
        Декоратор принимает функцию, печатает ее название,
        время начала выполнения, время окончания выполнения и
        общее время выполнения в секундах.
        :param args: any args
        :param kwargs: any kwargs
        :return: function object
        """
        start = time()
        print('Function name:', func.__name__)
        print('Start:', start)
        result = func(*args, **kwargs)
        end = time()
        print('End:', end)
        print('Processing time (s):', end - start)
        return result
    return new_func

# test
print('*'*20, 'Task #3', '*'*20)
# мануальное присваивание декторатора
my_decorator = time_decorator(filter_num_list)
my_decorator(list(range(1000)), filter_method='prime')
print('-'*5)

# с использованием конструкции с @
@time_decorator
def example_func():
    from time import sleep
    sleep(1.2)
    print('some work')
example_func()

# БОНУСНОЕ ЗАДАНИЕ: создать декоратор, который показывает вложенные входы в функцию.
# Применить на примере вычисления чисел Фибоначчи


def func_enters_decorator(func):
    """
    Декоратор выводит вложенные входы функции и результат вычислений
    :param func: function object
    :return: function object
    """
    def new_func(b):
        print('{}->{}({})'.format('-'*b, func.__name__, b))
        res = func(b)
        print('<-{}{}({})=={}'.format('-'*b, func.__name__, b, res))
        return res
    return new_func

@func_enters_decorator
def fib(a):
    """
    Функция принимает на вход номер позиции ряда Фибоначчи (int)
    (начиная с 0, как принято в Python) и возвращает его значение
    :param a: int
    :return: int
    """
    if a > 1:
        return fib(a-1) + fib(a-2)
    else:
        return 1
# test
fib(5)