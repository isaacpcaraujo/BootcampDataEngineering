contadorLetras = lambda lista: [len(x) for x in lista]

if __name__ == "__main__":
    listaAnimais = ['chien', 'chat', 'cheval']
    print(contadorLetras(listaAnimais))


# Calculadora com Lambda e Dicionários:

    calculadora = {
        'soma': lambda a,b: a + b,
        'sub': lambda a,b: a - b,
        'mult': lambda a,b: a * b,
        'div': lambda a,b: a / b    
    }

    soma = calculadora['soma']
    print('A soma é: {}'.format(soma(10, 5)))