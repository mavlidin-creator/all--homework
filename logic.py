from decouple import config
from random import randint, choice

min_num = config('MIN_NUM', cast=int)
max_num = config('MAX_NUM', cast=int)
max_attempts = config('MAX_ATTEMPTS', cast=int)
initial_capital = config('INITIAL_CAPITAL', cast=int)




def play_game():
    secret_number = randint(min_num, max_num)
    attempts_left = max_attempts
    capital = initial_capital

    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от {min_num} до {max_num}.")
    print(f"У вас есть {max_attempts} попыток и начальный капитал: {capital}.")

    while attempts_left > 0 and capital > 0:
        try:
            bet = int(input(f"Ваш текущий капитал: {capital}. Сделайте вашу ставку: "))
            if bet <= 0 or bet > capital:
                print("Пожалуйста, сделайте ставку больше 0 и не превышающую ваш капитал.")
                continue
            guess = int(input("Попробуйте угадать число: "))
            attempts_left -= 1

            if guess == secret_number:
                capital += bet
                print(f"Поздравляю! Вы угадали число {secret_number}!")
                print(f"Ваш капитал увеличился до {capital}.")
                break
            elif guess < secret_number:
                capital -= bet
                print("Загаданное число больше.")
            else:
                capital -= bet
                print("Загаданное число меньше.")

            print(f"У вас осталось {attempts_left} попыток.")

        except ValueError:
            print("Пожалуйста, введите целое число.")

    if attempts_left == 0:
        print(f"У вас закончились попытки. Загаданное число было {secret_number}.")
    elif capital <= 0:
        print("К сожалению, вы проиграли все свои деньги.")