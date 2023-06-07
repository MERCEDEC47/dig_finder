import random

rand_num = random.randint(1, 100)
count_try = 0

print('Hello!! I guessed an integer from 1 to 100, try to guess it')


def is_valid(num):
    if 1 <= num <= 100:
        return True
    return False


while True:
    try:
        req = int(input("Try to input your number: "))
        count_try += 1
        if not is_valid(req):
            print("Your number is out of range (1-100). Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while req != rand_num:
    if req > rand_num:
        try:
            req = int(input("Your number is bigger than mine, try again: "))
            count_try += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    else:
        try:
            req = int(input("Your number is less than mine, try again: "))
            count_try += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

print('Congratulations!!! You won!!!', 'Try counter:', count_try)
