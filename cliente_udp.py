import socket
import funcoes_aux

def main():
    funcoes_aux.print_comandos()
    while True:
        tipo = input("Digite o tipo da requisição desejada: ")
        if (tipo == "4"):
            print("adeus ʕ •ɷ•ʔฅ ")
            break
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria o socket tipo UDP que ficará responsável por criar os cabeçalhos IP e UDP
        mensagem = funcoes_aux.criar_requisao(int(tipo), funcoes_aux.sortear_identificador()) # Cria a mensagem a ser passada para o servidor de acordo com a requisão
        endereco_destino = ('15.228.191.109', 50000)        # Endereço do servidor
        udp_socket.sendto(mensagem, endereco_destino)       # Envia a mensagem
        dados, endereco_origem = udp_socket.recvfrom(2040)  # Recebe a resposta do servidor
        resposta = funcoes_aux.decodificar_resposta(dados)  # Decodifica a resposta de acordo com o tipo da requisição
        print(resposta)

        udp_socket.close()
if __name__ == "__main__":
    main()