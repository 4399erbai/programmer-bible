import platform


def number_generator():
    num = 0
    while True:
        yield num
        num += 1


def tips(tip):
    print('Tip: '+tip)


def this_platform():
    return platform.system()
