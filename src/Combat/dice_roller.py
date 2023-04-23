from numpy.random import randint

# Rolls 'num' variable sided dice, with side numbers 'n'
def dN(n, num=1):
    return randint(1, n, size=(1, num))

# Rolls 'num' d6's
def d6(num=1):
    return randint(1, 7, size=(1, num))

# Rolls 'num' d8's
def d8(num=1):
    return randint(1, 9, size=(1, num))

# Rolls 'num' d10's
def d10(num=1):
    return randint(1, 11, size=(1, num))