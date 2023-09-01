def add(a, b):
    if a>10:
        a = a+8
    return a + b
def multiplicacao(a, b):
    return a * b
def subtracao(a,b):
    return a - b
def fatorial(x):
    if x==1:
        return 1
    else:
        return x*fatorial(x-1)