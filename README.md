Projeto para a disciplina de Redes de Computadores da UFPB, ministrada pelo professor Ewerton Monteiro Salvador. Consiste em dois clientes implementados em Python que solicitam a um servidor feito pelo professor utilizando o protocolo UDP.

O programa conta com 3 tipos de requisoções possiveis para o servidor e uma opção para sair do programa
1. Data e hora atual;
2. Uma mensagem motivacional para o fim do semestre;
3. A quantidade de respostas emitidas pelo servidor até o momento.
4. Sair.

O cliente_udp utiliza o socket UDP fornecido pela biblioteca socket, sendo responsável pela criação do cabeçalho UDP e IP.

Já o cliente_raw utiliza o socket RAW fornecido pela biblioteca socket, sendo responsável apenas pelo cabeçalho IP. Dessa forma, fica a cargo do programa criar o cabeçalho UDP.
O cliente_raw deve ser executado como administrador. 

Desenvolvido por Bárbara Hellen Padilha da Silva, Joison Oliveira Pereira e Luiz Paulo de Souza Fontes Junior.
