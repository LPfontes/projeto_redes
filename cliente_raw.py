import socket
import funcoes_aux


def definir_porta_origem():  # Solicita uma porta livre ao SO
    sock = socket.socket()
    sock.bind(('', 0))
    return sock.getsockname()[1]


def definir_ip_origem():     # Recebe o IP do host
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


print("Tipos de requisição: ")
print("1 - Data e hora atual")
print("2 - Uma mensagem motivacional para o fim do semestre")
print("3 - A quantidade de respostas emitidas pelo servidor até o momento")
print("4 - Sair")

ip_servidor = '15.228.191.109'
porta = 50000
while True:
    tipo = input("Digite o tipo da requisição desejada: ")
    if (tipo == '4'):
        print("adeus ʕ •ɷ•ʔฅ ")
        break
    ip_origem = definir_ip_origem()
    porta_origem = definir_porta_origem()
    socket_raw = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP) # Cria o socket tipo RAW que ficará responsável apenas pelo cabeçalho UDP
    mensagem = funcoes_aux.criar_requisao(int(tipo), funcoes_aux.sortear_identificador()) # Cria a mensagem a ser passada para o servidor de acordo com  a requisição
    # criar_o_cabeçalho_UDP;
    endereco_destino = (ip_servidor, porta)       # Endereço do servidor
    socket_raw.sendto(mensagem, endereco_destino)
    dados, endereco_origem = socket_raw.recvfrom(2040)  # Recebe a resposta do servidor
    # resposta = decodificar resposta do servidor ignorado o cabeçalho ip e o udp
    # print(resposta)
    socket_raw.close()