Projeto para a disciplina de Redes de Computadores da UFPB, ministrada pelo professor Ewerton Monteiro Salvador. Consiste em dois clientes implementados em Python que solicitam a um servidor feito pelo professor utilizando o protocolo UDP.

O cliente_udp utiliza o socket UDP fornecido pela biblioteca socket, sendo responsável pela criação do cabeçalho UDP e IP.

Já o cliente_raw utiliza o socket RAW fornecido pela biblioteca socket, sendo responsável apenas pelo cabeçalho IP. Dessa forma, fica a cargo do programa criar o cabeçalho UDP.

Desenvolvido por Bárbara Hellen Padilha da Silva, Joison Oliveira Pereira e Luiz Paulo de Souza Fontes Junior.
