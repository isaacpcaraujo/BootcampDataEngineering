# Redes de Computadores no Linux

## O que é uma rede?

"Rede de computadores é um conjunto de equipamentos interligados de maneira a trocarem informações e compartilharem recursos, como arquivos de dados gravados, impressoras, modems, softwares e outros equipamentos". (Sousa, 1999)

## Tipos de Rede

* Rede **WAN**: Wide Area Network ou World Area Network é uma rede geograficamente distribuida;
* Rede **MAN**: Metropolitan Area Network é uma rede metropolitana que interligam várias redes locais;
* Rede **LAN**: Local Area Network é uma rede local de uma forma geral em um único prédio ou campus.

## Protocolos

"Protocolo é a 'linguagem' usada pelos dispostivios de uma rede de modo que eles consigam se entender" (Torres, 2004).

Existem diversos protócolos. 

* IP - Protocolo de Internet - Endereço IP: Números que identificam seu computador em uma rede;
* ICMP - Internet Control Message Protocol: Tem o objetivo de prover mensagens de controle na comunicação entre nós;
* DNS - Domain Name Server: Esse protocolo de aplicação tem por função identificar endereços IPs e manter uma tabela com os endereços dos caminhos de algumas redes.

## Interface de Rede

A interface de rede é um software e/ou hardware que faz a comunicação em uma rede de computadores. No linux, essas interfaces estão localizadas no diretório ***/dev***.

**Curiosidade**: A interface loopback é um tipo especial que permite fazer conexões com vocẽ mesmo. Você pode testar vários programas de rede sem interferir na sua rede. O endereço IP 127.0.0.1 foi escolhido para o loopback.

## Comandos de Rede no Linux

Será necessário instalar o repositório net-tools no seu terminal.

No Ubuntu/Mint:
> ```sudo apt install net-tools```

No Manjaro:
> ```sudo pacman -S net-tools```

O comando ***ifconfig*** é utilizado para visualizar e configurar as interfaces de rede. Utilizando-a sem argumentos visualizamos o status de nossas interfaces.

> ```ifconfig```

O comando ***hostname*** mostra ou muda o nome do computador na rede.

Nome do host
> ```hostname```

Endereço de IP
> ```hostname -I```

Endereço de loopback
> ```hostname -i```

O comando ***ping*** utiliza o datagrama Echo Request do protocolo ICMP para testar a conectividade entre equipamentos

> ```ping www.google.com```

O comando ***traceroute*** mostra todos os nós existentes até chegar ao domínio desejado. É necessário instalar o repositório **traceroute**

> ```traceroute www.google.com```

O comando finger exibe informações sobre um usuário.

> ```finger```

Com esses comandos conseguimos visualizar e configurar aspectos de nossas redes.