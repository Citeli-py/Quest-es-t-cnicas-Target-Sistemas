'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''


def pertence_fibonacci(num):
    f0, f1 = 0, 1

    while f0 <= num:
        # Verifica se pertence a sequencia
        if f0 == num:
            return True  
        # Troca f0 com f1  e f1 = f1 + f0
        f0, f1 = f1, f0 + f1  
    
    return False  # O número não pertence à sequência


num = 21

if (pertence_fibonacci(num) ):
    print(num, "pertence a sequência")
else:
    print(num, "não pertence a sequência")


# 21 pertence a sequência