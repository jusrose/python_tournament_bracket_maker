#import reqiured libs
import random

VERSION = "0.0.1"
# func to get user input on how many players/ teams and their names
def get_users():
    n = input("how many players>>> ")
    try:
        n = int(n)
    except ValueError:
        n = init()
    pl = []
    for i in range(n):
        print("player {} of {}".format(i+1, n))
        p = input("player name>>> ")
        pl.append(p)
    return pl

#prints out the bracke in human readable form
def print_brackt(b):
    count = 1
    for i in b:
        print("for match {}: {}.".format(count, i))
        count = count+1

#generates the bracket
def gen_bracket(isOdd, p):
    random.shuffle(p)
    print(p)
    if isOdd:
        p.append("None")
    s = len(p)
    print(p)
    b = []
    for i in range(s):
        if not test_isOdd(i):
            temp = [p[i], p[i+1]]
            b.append(temp)
    return b

#tests if value is odd or even
def test_isOdd(n):
    test = n % 2
    if not test == 0:
        return True
    else:
        return False

#main function
def main():
    pl = get_users()
    l = len(pl)
    isOdd = test_isOdd(l)
    b = gen_bracket(isOdd, pl)
    print_brackt(b)
#call main func if ran as main
if __name__ == "__main__":
    print("version: {}".format(VERSION))
    main()
