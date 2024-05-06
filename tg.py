import random
from string import ascii_letters
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate(length: int, seed: str, num_frequency):
    random.seed(seed)
    token = ""
    num_frequency = 1 if num_frequency < 1 else num_frequency
    for _ in range(length):
        if random.randint(0, num_frequency) == 0:
            token += random.choice(ascii_letters)
        else:
            token += str(random.choice(nums))
    return token


lenght = 25
seed = "Hello World!"
num_freq = 1

token = generate(lenght, seed, num_freq)

input(token)
