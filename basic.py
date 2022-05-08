import random


def sub(text):
    return input(f"--> {str(text).upper()} > ").replace("?", "").casefold().lstrip().rstrip()


def out(value):
    if type(value) == str:
        return print(f">>> {str(value).upper()} .")
    elif type(value) == list:
        return print(f">>> {str(random.choice(value)).upper()} .")
