"""
Task 1
Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в степінь,
взяття з під кореня, пошук відсотку від числа

Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу
даних або інструкції математичних операцій

заповніть ваш скрипт логами
Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
+ логи з помилками
причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
лог файл завжди відкриваєтсья в режимі дозапису.
так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки
"""

import logging
from math import sqrt

log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s'
logging.basicConfig(level=logging.DEBUG, filename="test.log", filemode="a", format=log_template)

functions = ['+', '-', '/', '*', '**', '%', 'sqrt', 'stop']
print("----------------------------------------------------------------------------------")
print("Вітаю у моєму калькуляторі!")

print("----------------------------------------------------------------------------------")


def calc(choice):
    if choice == '+':
        try:
            return summ(int(input('Введіть перше число: ')), int(input('Введіть друге число: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    elif choice == '-':
        try:
            return subtract(int(input("Введіть перше число: ")), int(input('Введіть друге число: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    elif choice == '/':
        try:
            return dividing(int(input('Введіть перше число: ')), int(input('Введіть друге число: ')))
        except ValueError:
            logging.error('ValueError', exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    elif choice == '*':
        try:
            return multiply(int(input('Введіть перше число: ')), int(input('Введіть друге число: ')))
        except ValueError:
            logging.error("ValueError", exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    elif choice == '**':
        try:
            return elevation(int(input('Введіть число до якого підносити степінь: ')), int(input('Введіть значення до '
                                                                                                 'якого підносимо: ')))
        except ValueError:
            logging.error("ValueError", exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    elif choice == '%':
        try:
            return search_percentage(int(input('Введіть число(відсоткове): ')), int(input('Введіть число: ')))
        except ValueError:
            logging.error("ValueError", exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    elif choice == 'sqrt':
        try:
            return taking_sqrt(int(input('Введіть число: ')))
        except ValueError:
            logging.error("ValueError", exc_info=True)
            return 'Введено не число. Спробуйте ще раз'
    else:
        print('Виберіть правильну функцію!')


def summ(num_1, num_2):
    logging.info("Повертає суму двох чисел")
    return f'Відповідь: {num_1} + {num_2} = {num_1 + num_2}'


def subtract(num_1, num_2):
    logging.info('Повертає різницю двох чисел')
    return f'Відповідь: {num_1} - {num_2} = {num_1 - num_2}'


def dividing(num_1, num_2):
    try:
        logging.info("Повертає ділення одного числа на інше")
        return f'Відповідь: {num_1} / {num_2} = {num_1 / num_2}'
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', exc_info=True)
        return 'Ділення на нуль неможливе!'


def multiply(num_1, num_2):
    logging.info('Повертає множення одного числа на інше')
    return f'Відповідь: {num_1} * {num_2} = {num_1 * num_2}'


def elevation(num_1, num_2):
    try:
        logging.info('Повертає піднесення числа до степення')
        return f'Відповідь: {num_1} ** {num_2} = {num_1 ** num_2}'
    except ZeroDivisionError:
        logging.info('ZeroDivisionError', exc_info=True)
        return 'Ділення на нуль неможливе!'


def search_percentage(num_of_percent, num):
    logging.info('Повертає відсоток від числа')
    return f'Відповідь: {num_of_percent}% від {num} = {num / 100 * num_of_percent}'


def taking_sqrt(num):
    try:
        logging.info('Повертає число взяте з-під кореня')
        return f'Відповідь: {num} = {sqrt(num)}'
    except ValueError:
        return 'Число не може бути негативним!'


a = 'Бувай!'

while True:
    output = input(f'Виберіть одну з функцій: {functions}')
    if output == 'stop':
        logging.info('Завершення')
        print("----------------------------------------------------------------------------------")
        print(f"{a}")
        break
    elif output in functions:
        print(calc(output))
    else:
        logging.warning('Неправильна операція')
        print(f'Перепрошую, але ця операція неправильна. Вибери іншу: {functions}')
