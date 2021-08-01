# Gerenciando Pacotes no Linux - Manjaro

Pacotes são programas colocados dentro de arquivos identificados por sua extensão, tendo os arquivos necessários para a instalação de um determinado programa.

> Ex: ***.deb***, ***.rpm*** entre outros.

Já os gerenciadores de pacotes são sistemas que possuem resolução automática para a instalação de pacotes. Ou seja, métodos de fácil instalação de programas.

> Ex: ***apt***, ***pacman***, ***dpgk*** entre outros.

## Instalação, atualização e remoção

Para **instalar um pacote**, utiliza-se o comando: Utilizaremos o pacote "nmap" como exemplo.
> ```sudo pacman -S nmap```

Para **atualizar um pacote**, utiliza-se o comando: Utilizaremos o pacote "nmap" como exemplo.

Sincronizar os repositórios
> ```sudo pacman -Sy nmap```

Buscar atualizações dos repositórios
> ```sudo pacman -Su nmap```

Sincronizar e Buscar atualizações dos repositórios
> ```sudo pacman -Syu nmap```

Para **remover um pacote**, utiliza-se o comando: Utilizaremos o pacote "nmap" como exemplo. 
> ```sudo pacman -R nmap```

Removendo o pacote junto com as dependências não usadas por outros pacotes.
> ```sudo pacman -Rs nmap```

## Atualizando o Sistema e usando o dpkg

Também podemos atualizar o nosso sistema operacional utilizando o nosso gerenciador de pacotes. Com o pacman podemos realizar a operação:

> ```sudo pacman -Syu```

É possível realizar a instalação de pacotes por meio de sites que disponibilizam esses arquivos, como *pkgs.org* e o *rpm.pbone.net*.

Para instalar um pacote local, execute o comando:

> ```sudo pacman -U pacote.pkg.tar.gz```

Para instalar um pacote que necessita ser baixado, execute o comando:

> ```sudo pacman -U http://www.(linkparaopacote)/pacote.pkg.tar.xz```

O curso da DIO é feito em Ubuntu/Fedora.