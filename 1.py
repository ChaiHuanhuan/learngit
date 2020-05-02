import random

def genpwd(length):
    s=""
    for i in range(length):
        if i == 0:
            s += str(random.randint(1,9))
        else:
            s += str(random.randint(0,9))
    return eval(s)
length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
