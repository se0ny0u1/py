import random

def guess_game():
    secret_number = random.randint(1, 100)
    tries = 0
    print("Добро пожаловать в игру Угадай число!")
    n = int(input("введите число от 1 до 100: "))
    tries = tries + 1

    if secret_number > n:
        print(f"К сожалению вы не угадали, было загадано число {a}")

    elif secret_number < n:
        print(f"К сожалению вы не угадали, было загадано число {a}")

    elif secret_number == n:
        print("Поздравляю! Числа совпали")
        break

    print(f"Конец игры. Было сыграно {tries} попыток")

    r = input("Введите + чтобы продолжить или - чтобы прекратить игру: ")

    if r == "+":
        print("Продолжайте игру")
        
    elif r == "-":
        print(f"Вы вышли из игры. Было сыграно {tries} попыток")
        break