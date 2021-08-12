import requests

def RetornaDadosCep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)
    print(response.json())
    dadosCep = response.json()

    print(dadosCep['logradouro'])
    print(dadosCep['complemento'])
    return dadosCep

if __name__ == '__main__':
    cep = input('Digite seu CEP: ')
    RetornaDadosCep(cep)