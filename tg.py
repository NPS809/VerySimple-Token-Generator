import random
from string import ascii_letters
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate(length: int, seed: str):
    random.seed(seed)
    token = ""
    for _ in range(length):
        if random.randint(1, 2) == 2:
            token += random.choice(ascii_letters)
        else:
            token += str(random.choice(nums))
    return token

print(f"Ваш токен {generate(15, input("Введите сид:"))}")
input()
