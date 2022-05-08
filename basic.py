import random

def inp():
    return input(f"--> ").replace("?", "").replace("_",
                                                   "").casefold().lstrip().rstrip()


def sub(text):
    return input(f"--> {str(text).upper()} > ").replace("?", "").casefold().lstrip().rstrip()


def out(value):
    if type(value) == str:
        return print(f">>> {str(value).upper()} .")
    elif type(value) == list:
        return print(f">>> {str(random.choice(value)).upper()} .")


def greet(name):
    out(["hi there!", "hai there!", f"welcome {name}", "Greetings from abettor", f"hai {name}"])


def check_all(list, split):
    return all(value in split for value in list)


def compare(list, main_word, split):
    if main_word in split:
        split.pop(split.count(main_word))
        for other_word in list:
            if other_word in split:
                return True

