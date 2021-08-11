lista = [1, 2]

try:
    divisao = 10/1
    numero = lista[1]
    x = 0
except ZeroDivisionError:
    print('Não é possível dividir um número por 0')
except IndexError:
    print('Erro de íncide')
except BaseException as ex:
    print(f'Erro desconhecido. Erro: {ex}')
else:
    print('Não cair em exceções')