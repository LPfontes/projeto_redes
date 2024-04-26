import socket
import random
import types

consts = types.SimpleNamespace()
consts.DATA = 1
consts.MENSAGEM_MOTIVACIONAL = 2
consts.QUANTIDADE_RESPOSTAS_SERVIDOR = 3

def dividir_identificador(numero):
    # Obtém o byte mais significativo 
    byte1 = (numero >> 8) & 0xFF
    # Obtém o byte menos significativo 
    byte2 = numero & 0xFF
    return byte1, byte2
def sortear_identificador():
    return random.randint(1, 65535)


def criar_menssagem(tipo,identificador):
    byte1 = 0b00000000
    bytes_identificador = dividir_identificador(identificador) 
    match tipo:
        case consts.DATA:
            pass
        case consts.MENSAGEM_MOTIVACIONAL:
            byte1 = byte1 | 0b0001
             
        case consts.QUANTIDADE_RESPOSTAS_SERVIDOR:
            byte1 = byte1 | 0b0010
            
    mensagem = bytes([byte1, bytes_identificador[0], bytes_identificador[1]]) 
    return mensagem       
def bytes_to_string(lista_bytes):
    
    
    return ''.join(chr(i) for i in lista_bytes)
def bytes_to_int(lista_bytes):
    return int.from_bytes(bytes(lista_bytes), byteorder='big')


   
def decodificar_resposta(dados):
    byte1 = dados[0]
    match byte1:
        case 0x10:
            tamanho_resposta =dados[3]
            
            lista_bytes = []
            for i in range(tamanho_resposta):
                lista_bytes.append(dados[4+i]) 
            return bytes_to_string(lista_bytes)
        case 0x11:
            tamanho_resposta =dados[3]
            
            lista_bytes = []
            for i in range(tamanho_resposta):
                lista_bytes.append(dados[4+i]) 
            return bytes_to_string(lista_bytes)
        case 0x12:
            tamanho_resposta =dados[3]
            
            lista_bytes = []
            for i in range(tamanho_resposta):
                lista_bytes.append(dados[4+i]) 
            return bytes_to_int(lista_bytes)
   

# Crie um socket UDP

print("Tipos da requisção: ")
print("1 Data e hora atual;")
print("2 Uma mensagem motivacional para o fim do semestre;")
print("3 A quantidade de respostas emitidas pelo servidor até o momento;")
print("digite 'sair' para encerrar o programa.")
while True: 
    tipo = input("Digite o tipo da requisção desejada: ")
    if(tipo == 'sair'):
        print("adeus ʕ •ɷ•ʔฅ ")
        break
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
    mensagem = criar_menssagem(int(tipo),sortear_identificador()) #cria a messangem a ser passada para o servidor de acordo com a requisão
    endereco_destino = ('15.228.191.109', 50000) #endereço do servidor
    udp_socket.sendto(mensagem, endereco_destino)

    dados, endereco_origem = udp_socket.recvfrom(2040) #Recebe a resposta do servidor
    resposta = decodificar_resposta(dados) # decodifica a resposta de acordo com o tipo da requesição
    print(resposta)

    udp_socket.close()