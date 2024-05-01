import socket
import funcoes_aux

# Somando as duas palavras
def cheksum_udp(lista_bytes):
    tamanho_lista = len(lista_bytes)
    if tamanho_lista % 2 == 0:
       pass
    else:
        lista_bytes = lista_bytes + bytes([0])
    tamanho_lista = len(lista_bytes)
    index = 0
    resultado = 0
    for i in range(int(tamanho_lista/4)):
        resultado = somar_palavra_16bits(resultado,somar_palavra_16bits(lista_bytes[index] << 8 | lista_bytes[index+1],lista_bytes[index+2]<< 8 |lista_bytes[index+3])) 
        index += 4
    
    return resultado
        
def somar_palavra_16bits(palavra1,palavra2):
    resultado =  palavra1 + palavra2
    while resultado.bit_length() > 16:
        carry = resultado >>16
        resultado &= 0xFFFF
        resultado += carry
    return resultado

src_port = 1234
dest_port = 5678
udp_length = 20  # Tamanho do cabeçalho UDP + dados
udp_checksum = 0  # O checksum pode ser calculado posteriormente
src_port = funcoes_aux.dividir_numero_2_bytes(src_port)
dest_port = funcoes_aux.dividir_numero_2_bytes(dest_port)
udp_length = funcoes_aux.dividir_numero_2_bytes(udp_length)
udp_checksum = funcoes_aux.dividir_numero_2_bytes(udp_checksum) 
udp_header = bytes([src_port[0], src_port[1], dest_port[0],dest_port[1],udp_length[0],udp_length[1],udp_checksum[0],udp_checksum[1]]) 

# Pseudo cabeçalho (exemplo para calcular o checksum do UDP)
src_ip = '192.168.0.1'
dest_ip = '192.168.0.2'
protocol = socket.IPPROTO_UDP
src_ip = funcoes_aux.trasformar_string_ip_em_bytes(src_ip)
dest_ip = funcoes_aux.trasformar_string_ip_em_bytes(dest_ip)
protocol = protocol.to_bytes(1,byteorder='big')
zero = 0b00000000
tamanho_udp_header = funcoes_aux.dividir_numero_2_bytes(len(udp_header))

pseudo_header = src_ip + dest_ip + bytes([protocol[0],zero, tamanho_udp_header[0],tamanho_udp_header[1],zero])

cheksum = cheksum_udp(pseudo_header + udp_header)
pseudo_header = pseudo_header + udp_header
for i in range(20):
    binario = ''.join(format(pseudo_header[i], '08b'))
    print(binario)  # Saída: '000000010000111111111111'
