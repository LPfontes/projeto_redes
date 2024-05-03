import socket
import funcoes_aux

# Constantes
IP_DESTINO = '15.228.191.109'
PORTA_DESTINO = 50000

def definir_porta_origem():
    sock = socket.socket()
    sock.bind(('', 0))
    return sock.getsockname()[1]

def definir_ip_origem():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def criar_cabecalho_udp(porta_origem, porta_destino, tamanho_udp_cabecalho, udp_checksum):
    # Converte os valores para bytes
    porta_origem = funcoes_aux.dividir_numero_2_bytes(porta_origem)
    porta_destino = funcoes_aux.dividir_numero_2_bytes(porta_destino)
    tamanho_udp_cabecalho = funcoes_aux.dividir_numero_2_bytes(tamanho_udp_cabecalho)
    udp_checksum = funcoes_aux.dividir_numero_2_bytes(udp_checksum)

    # Cria o cabeçalho UDP
    udp_cabecalho = bytes([porta_origem[0], porta_origem[1], porta_destino[0], porta_destino[1], tamanho_udp_cabecalho[0],tamanho_udp_cabecalho[1],udp_checksum[0],udp_checksum[1]])
    return udp_cabecalho

def criar_pseudo_cabecalho(ip_origem, ip_destino, tamanho_udp_cabecalho):
    protocolo = socket.IPPROTO_UDP.to_bytes(1, byteorder='big')
    ip_origem = funcoes_aux.trasformar_string_ip_em_bytes(ip_origem)
    ip_destino = funcoes_aux.trasformar_string_ip_em_bytes(ip_destino)
    zero = 0b00000000
    tamanho_udp_cabecalho = funcoes_aux.dividir_numero_2_bytes(tamanho_udp_cabecalho)
    pseudo_cabecalho = ip_origem + ip_destino + bytes([zero, protocolo[0], tamanho_udp_cabecalho[0],tamanho_udp_cabecalho[1]])
    return pseudo_cabecalho

def get_payload(dados):
    payload = dados[28:] # pulando os primeiros 28 bytes para obter o payload
    return payload

def main():
    print("Tipos de requisição: ")
    print("1 - Data e hora atual")
    print("2 - Uma mensagem motivacional para o fim do semestre")
    print("3 - A quantidade de respostas emitidas pelo servidor até o momento")
    print("4 - Sair")

while True:
    tipo = input("Digite o tipo da requisição desejada: ")
    if (tipo == '4'):
        print("adeus ʕ •ɷ•ʔฅ ")
        break

    data = funcoes_aux.criar_requisao(int(tipo), funcoes_aux.sortear_identificador())

    ### CABEÇALHO UDP ###
    porta_origem = definir_porta_origem()
    socket_raw = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    tamanho_udp_cabecalho = 8 + len(data)  # Tamanho do cabeçalho UDP + dados
    udp_checksum = 0  # O checksum pode ser calculado posteriormente
    udp_cabecalho = criar_cabecalho_udp(porta_origem, PORTA_DESTINO, tamanho_udp_cabecalho, udp_checksum)
    segmento = udp_cabecalho + data

    ### PSEUDO CABEÇALHO IP ###
    ip_origem = definir_ip_origem()
    pseudo_cabecalho = criar_pseudo_cabecalho(ip_origem, IP_DESTINO, tamanho_udp_cabecalho)
    udp_checksum = funcoes_aux.cheksum(pseudo_cabecalho + segmento)

    udp_cabecalho = criar_cabecalho_udp(porta_origem, PORTA_DESTINO, tamanho_udp_cabecalho, udp_checksum)

    endereco_destino = (IP_DESTINO, PORTA_DESTINO)        # Endereço do servidor
    socket_raw.sendto(segmento, endereco_destino)

    dados, endereco_origem = socket_raw.recvfrom(2040)  # Recebe a resposta do servidor
    payload = get_payload(dados)
    resposta = funcoes_aux.decodificar_resposta(payload)  # Decodifica a resposta de acordo com o tipo da requisição
    print(resposta)
    

if __name__ == "__main__":
    main()
