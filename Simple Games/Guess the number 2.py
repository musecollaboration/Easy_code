from random import randint
from time import sleep


def main():
    n = 10
    print(f"Привет! Я загадал число от 1 до {n}. Попробуйте угадать его!")
    sleep(1)
    guess = None
    tries = 0
    max_tries = 5
    while guess != "quit":
        if guess is None:
            guess = input(
                "Введите ваше предположение (или 'quit' для выхода): ")
        else:
            try:
                guess = int(guess)
                if 1 <= guess <= 100:
                    break
                else:
                    print(f"Ваше число должно быть между 1 и {n}.")
            except ValueError:
                print("Пожалуйста, введите число.")
        tries += 1
        if tries == max_tries:
            print("Вы превысили максимальное количество попыток.")
            break
        print("Неверно. Я загадал число:", randint(1, n))


main()
