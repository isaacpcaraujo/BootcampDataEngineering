# Terminal Linux

O terminal é uma linha de comandos onde podemos executar programas específicos do Linux. A maioria dos comandos são iguais em diversas distros ("distribuições).

> Acessando o terminal

O terminal pode ser acessado através da interface gráfica, pesquisando pelo mesmo na aba de atividades. 

**ATALHO:** ctrl + alt + T

## Comandos Básicos

O simbolo abaixo indica que você está na pasta do seu usuário padrão
> ```~```

Mostrar o caminho dos arquivos atual
> ```pwd```

Apresentar a lista de arquivos e diretórios de uma determinada pasta
> ```ls```

Mostrar os detalhes de cada arquivo	
> ```ls -l```

Mudar o diretório para o local indicado
>``` cd caminho```

Retornar para o diretório anterior
> ```cd ..```

Redirecionar para a pasta raiz dos arquivos
> ```cd /```

Retornar para a pasta do usuario padrão
> ```cd ~``` 

Criar uma nova pasta dentro do caminho atual
> ```mkdir nomeDoDiretorio```

Mostrar o histórico de comandos
> ```history```

Repetir o último comando
> ```!!```

Apagar um arquivo especifico
> ``` rm caminho```

Apagar um diretório
> ``` rm -rf caminho```

Move um arquivo ou diretório para um caminho especificado. Também pode ser utilizado para renomear um arquivo ou diretório
> ``` mv operador1 operador2 ```

Copiar um arquivo 
> ```cp``` 

Limpar o terminal
> ```clear```

Abrir o Manual do comando específico
> ```man comando```

Abrir o manuual do comando específico em Português
```comando --help```

## Alguns Atalhos

* **Ctrl+C**: Cancela o comando atual em funcionamento;
* **Ctrl+Z**: Pausa o comando atual, em primeiro plano ou segundo plano;
* **Ctrl+D ou exit**: Faz o logout da sessão atual;
* **Ctrl+W**: Apaga uma palavra na linha atual;
* **Ctrl+U**: Apaga a linha inteira;
* **Ctrl+R**: Busca um comando recente;


## Manipulação de Arquivos de Textos e Redirecionamento

Podemos criar um arquivo ***.txt*** utilizando o comando touch

> ```touch meuTexto.txt```

Utilizando o editor de texto NANO do Linux

> ```nano meuTexto.txt```

Visualizando o texto do arquivo

> ```cat meuTexto.txt```

Invertendo as linhas na visualização do arquivo de texto

> ```tac meuTexto.txt```

Visualizando as 10 primeiras linhas de um arquivo

> ```head meuTexto.txt```

Visualizando as 10 últimas linhas de um arquivo

> ```tail meuTexto.txt```

Conseguimos ainda, direcionar o retorno de determinadas funções a outros arquivos utilizando o simbolo maior que " ***>*** "

> ```head meuTexto.txt > distros.txt```

Buscando e Marcando palavras especificas nos arquivos

> ```head meuTexto.txt | grep Linux```

**Utilizando informações de um calendário**

Visualizando o calendário do mês virgente e criando um arquivo desse calendário

> ```cal```
> ```cal > calendario_jul.txt```

Visualizando a data atual e adicionando a informação ao arquivo do calendário

> ```date```
> ```date >> calendario.txt```

Ainda, podemos visualizar o calendário de um determinado ano ou mês.

> ```cal agosto 2021```


Ao visualizar arquivos longos podemos realizar uma paginação das linhas. Compactando sua visualização. 

> ```cat meuTexto.txt | more```
> ```cat meuTexto.txt | less```

Pode-se visualizar também dois arquivos utilizando os operadores " ***&*** " (Une os dois arquivos em duas saídas) e " ***&&*** " (Une os dois arquivos em uma única saída)

> ```cat meuTexto.txt & cat calendario.txt```
> ```cat meuTexto.txt && cat calendario.txt```

Também é possível mesclar comandos utilizando os operadores acima.

> ```mkdir arquivosTexto && cd arquivosTexto```

O comando ***file*** retorna o tipo do arquivo indicado no operador

> ```file meuTexto.txt```

O comando ***whatis*** o que é determinada função

> ```whatis file```

O comando ***find*** retorna o caminho (Filepath) para o arquivo indicado

> ```find meuTexto.txt```