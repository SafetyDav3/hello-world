# Generates a random number based on time

import time


def random_number_generator():
    """
    Generates a random number based on the current time in milliseconds.
    """
    now = time.time()
    random_number = int(now * 1000) % 1000
    return random_number


random_num = random_number_generator()
print(random_num)
