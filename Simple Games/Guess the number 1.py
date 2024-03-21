# ?  Угадай число – компьютер выберет случайное число,
# ?  а игрок должен будет по очереди угадывать число.

from random import randint
from time import sleep


def get_integer_input(prompt=''):
    sleep(0.5)
    while True:
        try:
            user_input = input(prompt)
            return int(float(user_input))
        except ValueError:
            print(f"Это не число {smile()}")


def generate_random_number(max_value):
    return randint(1, max_value)


def choose_range():
    sleep(0.5)
    x = get_integer_input(f'-Выбирете диапазон- \n  от 1 до: ')
    return x


def smile():
    s = ['😋', '😁', '😇', '😉', '😏']
    random_smile = s[randint(0, 4)]
    return random_smile


def play_game():
    sleep(0.5)
    print('''
**** Игра 1 ****
* Угадай число *
----------------''')
    x = choose_range()
    unknown_number = generate_random_number(x)
    max_attempts = get_integer_input('Укажи количество попыток: ')
    sleep(0.25)
    print(f'Теперь угадай, какое число загадал компьютер {smile()}')
    # print(f"Загаданное число: {unknown_number}")

    for attempt in range(max_attempts):
        print()
        user_guess = get_integer_input('Ваш вариант: ')
        if user_guess == unknown_number:
            sleep(0.25)
            print()
            print('*' * 45)
            print(
                f'Ты угадал! Это число {unknown_number}. Использовал попыток: {attempt + 1}')
            sleep(1)
            print('🌸 🍒 🎀 🍀 🍭 🍌 🍍 🍁 🍂 🍃 🍄 🍅 🍎 🍏 🍑')
            print()
            break
        else:
            sleep(0.5)
            print(
                f'Не верно {smile()}. Осталось попыток: {max_attempts - attempt - 1}')


n = ''
while n != 'нет':
    n = input('Вы хотите поиграть? ').lower()
    if n == 'нет':
        print(f'Хорошо, буду ждать тебя снова {smile()}')
        break
    else:
        play_game()
