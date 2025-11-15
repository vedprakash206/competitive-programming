import math
def perfect_square_root(a):
    r=int(math.sqrt(a))
    return r if r*r==a else -1
