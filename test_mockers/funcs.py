import random


def rand():
    res = random.random()
    if res < 0.5:
        raise RuntimeError(f"Result is less than 0.5: {res}")
    return res


def rand_2():
    tries = 1
    res = random.random()

    while res < 2:

        res = random.random()
        tries += 1

        if tries > 10:
            raise RuntimeError(f"Its too much, total tries: {tries}")

    return res, tries
