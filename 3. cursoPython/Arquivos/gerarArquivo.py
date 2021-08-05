def escreverArquivo(texto):
    arquivo = open('novoArquivo.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo(texto):
    arquivo = open('novoArquivo.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    escreverArquivo("Esse é o nosso primeiro arquivo")
    lerArquivo('novoArquivo.txt')
    atualizarArquivo("\nAtualizando o arquivo!")
    lerArquivo('novoArquivo.txt')