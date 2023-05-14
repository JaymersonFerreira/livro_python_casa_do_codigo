'''Se temos uma lista ou tupla com os valores que estão na mesma ordem dos parâmentro que a função recebe, podemos usar o packing'''
from datetime import date

d = (2013, 3, 15)
date(*d)

'''O unpacking é o precosso que é executado dentro da função, e não na chamada. Podemos usar a sintaxe *args ou **kwargs como argumentos para o unpacking dos parâmentros posicionados ou nomeados'''

def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

unpacking_experiment(1,2,3,4,5,6)

