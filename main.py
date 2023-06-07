import random


def play_game():
    rand_num = random.randint(1, 100)
    attempts = 0  # Инициализация счетчика попыток

    print('Hello!! I guessed an integer from 1 to 100, try to guess it')

    def is_valid(num):
        if 1 <= num <= 100:
            return True
        return False

    while True:
        try:
            req = int(input("Try to input your number: "))
            if not is_valid(req):
                print("Your number is out of range (1-100). Try again.")
            else:
                attempts += 1  # Увеличение счетчика попыток
                if req == rand_num:
                    print('Congratulations!!! You won!!!')
                    break
                elif req > rand_num:
                    print("Your number is bigger than mine.")
                else:
                    print("Your number is less than mine.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
