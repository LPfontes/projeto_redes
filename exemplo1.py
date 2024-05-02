import socket
import funcoes_aux
# exemplo dado pelo professor nas Especificaçãos


def definir_porta_origem():
    sock = socket.socket()
    sock.bind(('', 0))
    return sock.getsockname()[1]


def definir_ip_origem():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


data = funcoes_aux.criar_requisao(1, funcoes_aux.sortear_identificador())

porta_origem = definir_porta_origem()
socket_raw = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
porta_destino = 50000
tamanho_udp_cabecalho = 8 + len(data)  # Tamanho do cabeçalho UDP + dados
udp_checksum = 0  # O checksum pode ser calculado posteriormente
porta_origem = funcoes_aux.dividir_numero_2_bytes(porta_origem)
porta_destino = funcoes_aux.dividir_numero_2_bytes(porta_destino)
tamanho_udp_cabecalho = funcoes_aux.dividir_numero_2_bytes(tamanho_udp_cabecalho)
udp_checksum = funcoes_aux.dividir_numero_2_bytes(udp_checksum)
# o cabeçalho udp é definido no RFC 768 composto por 8 bytes,
# 2 bytes para o numero da porta da origem, 2 bytes para o numero da porta de destino, 2 bytes para o tamanho do cabeçalho e 2 bytes para o cheksum
udp_cabecalho = bytes([porta_origem[0], porta_origem[1], porta_destino[0], porta_destino[1], tamanho_udp_cabecalho[0],tamanho_udp_cabecalho[1],udp_checksum[0],udp_checksum[1]])
segmento = udp_cabecalho + data
# na especificação do udp RFC 768  está definido que o cheksum do udp é feito com um pseudo_cabecalho com informações do cabecalho ip + o cabeçalho udp
# 16 bytes para o ip_origem
# 16 bytes para o ip_destino
# 1 byte zero
# 1 byte com o codigo do protocolo
# 2 bytes com o tamanho do segmento udp

ip_origem = definir_ip_origem()
ip_destino = '15.228.191.109'
protocolo = socket.IPPROTO_UDP
ip_origem = funcoes_aux.trasformar_string_ip_em_bytes(ip_origem)
ip_destino = funcoes_aux.trasformar_string_ip_em_bytes(ip_destino)
protocolo = protocolo.to_bytes(1, byteorder='big')
zero = 0b00000000
pseudo_cabecalho = ip_origem + ip_destino + bytes([zero, protocolo[0], tamanho_udp_cabecalho[0],tamanho_udp_cabecalho[1]])

udp_checksum = funcoes_aux.cheksum(pseudo_cabecalho + segmento)
udp_checksum = funcoes_aux.dividir_numero_2_bytes(udp_checksum)
udp_cabecalho = bytes([porta_origem[0], porta_origem[1], porta_destino[0], porta_destino[1], tamanho_udp_cabecalho[0],tamanho_udp_cabecalho[1], udp_checksum[0], udp_checksum[1]])
print(udp_cabecalho)
print("porta_origem")
print(funcoes_aux.bytes_to_int([udp_cabecalho[0], udp_cabecalho[1]]))
print("porta_destino")
print(funcoes_aux.bytes_to_int([udp_cabecalho[2], udp_cabecalho[3]]))
print("tamanho cabeçalho")
print(funcoes_aux.bytes_to_int([udp_cabecalho[4], udp_cabecalho[5]]))
print("cheksum")
print(funcoes_aux.bytes_to_int([udp_cabecalho[6], udp_cabecalho[7]]))
endereco_destino = ('15.228.191.109', 50000)        # Endereço do servidor
socket_raw.sendto(segmento, endereco_destino)

dados, endereco_origem = socket_raw.recvfrom(2040)  # Recebe a resposta do servidor
print(dados)

