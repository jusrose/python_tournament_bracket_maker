import random

def init():
    n = input("how many players>>> ")
    try:
        n = int(n)
    except ValueError:
        print("not valid input")
        n = init()
    pl = []
    for i in range(n+1):
        print("player {} of {}".format(i, n))
        p = input("player name>>> ")
        pl.append(p)
    return pl

def print_brackt(b):
    count = 1
    for i in b:
        print("for round one match {}: {}.".format(count, i))
        count = count+1

def gen_bracket(isOdd, p):
    random.shuffle(p)
    print(p)
    if not isOdd:
        p.append("None")
    s = len(p)
    print(p)
    b = []
    for i in range(s):
        if test_isOdd(i):
            temp = [p[i], p[i+1]]
            b.append(temp)
    return b

def test_isOdd(n):
    test = n % 2
    if not test == 0:
        return True
    else:
        return False

def main():
    pl = init()
    l = len(pl)
    bTest = test_isOdd(l)
    b = gen_bracket(bTest, pl)
    print_brackt(b)
    
if __name__ == "__main__":
    main()