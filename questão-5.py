'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

def inverte_string(string):
    tam_string = len(string)
    # Como strings em python são imutaveis temos que utilizar uma lista
    lista_caracteres = list(string) 

    # Esse algoritmo percorrer apenas metade da lista para inverte-la trocando as extremidades
    for i in range(tam_string//2):
        lista_caracteres[i], lista_caracteres[tam_string-1-i] = lista_caracteres[tam_string-1-i], lista_caracteres[i]

    # Junta os itens da lista em uma string novamente
    return ''.join(lista_caracteres)

string = "TargetSistemas"

print(inverte_string(string)) # sametsiStegraT