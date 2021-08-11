lista = [1, 2]

try:
    divisao = 10/0
    numero = lista[3]
    x = a
except ZeroDivisionError:
    print('Não é possível dividir um número por 0')
except IndexError:
    print('Erro de íncide')
except BaseException as ex:
    print(f'Erro desconhecido. Erro: {ex}')