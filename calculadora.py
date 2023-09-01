def add(a, b):
    return a + b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
def subtracao(a,b):
    return a - b
def fatorial(x):
    if x==1:
        return 1
    else:
        return x*fatorial(x-1)
