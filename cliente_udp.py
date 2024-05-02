import socket
import funcoes_aux

print("Tipos de requisição: ")
print("1 - Data e hora atual;")
print("2 - Uma mensagem motivacional para o fim do semestre;")
print("3 - A quantidade de respostas emitidas pelo servidor até o momento;")
print("4 - Sair")

while True:
    tipo = input("Digite o tipo da requisição desejada: ")
    if (tipo == "4"):
        print("adeus ʕ •ɷ•ʔฅ ")
        break
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria o socket tipo UDP que Ficará responsável por criar os cabeçalhos IP e UDP
    mensagem = funcoes_aux.criar_requisao(int(tipo), funcoes_aux.sortear_identificador()) # Cria a mensagem a ser passada para o servidor de acordo com a requisão
    endereco_destino = ('15.228.191.109', 50000)        # Endereço do servidor
    udp_socket.sendto(mensagem, endereco_destino)       # Envia a messagem
    dados, endereco_origem = udp_socket.recvfrom(2040)  # Recebe a resposta do servidor
    resposta = funcoes_aux.decodificar_resposta(dados)  # Decodifica a resposta de acordo com o tipo da requesição
    print(resposta)

    udp_socket.close()