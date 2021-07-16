import random
import string

def get_random(what: str, start, stop):
    """
    To return:
    - random integer;
    - random real number;
    - random symbol;
    based on the chosen option and given start and stop
    """
    if what == 'random integer':
        output = random.randint(start, stop)
    elif what == 'random real number':
        output = random.uniform(start, stop)
    elif what == 'random symbol':
        ind_1 = string.printable.index(start)
        ind_2 = string.printable.index(stop) + 1
        output = random.choice(list(string.printable)[ind_1: ind_2])
    else:
        output = f'no option for {what}'
    return output

if __name__ == '__main__':
    print(get_random('random symbol', 'a', 'A'))

