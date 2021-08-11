class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message
    
while True:
    try:
        x = int(input(('Digite um numero:')))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser utilizada.')
        else:
            raise InputError('Nota não pode ser negativa.')
        break
    except ValueError:
        print('Valor Invalido. Digite novamente!')