import math

def soma(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def exp(n1,n2):
    n3 = n1
    for n in range(n2-1):
        n3 *= n1
    return n3

def log(x):
    return math.log10(x)

def cos(x):
    return math.cos(x)

def sin(x):
    return math.sin(x)
