import types
import random
consts = types.SimpleNamespace()
consts.DATA = 1
consts.MENSAGEM_MOTIVACIONAL = 2
consts.QUANTIDADE_RESPOSTAS_SERVIDOR = 3

def dividir_numero_2_bytes(numero):
    # Obtém o byte mais significativo 
    byte1 = (numero >> 8) & 0xFF
    # Obtém o byte menos significativo 
    byte2 = numero & 0xFF
    return byte1, byte2
def sortear_identificador():
    return random.randint(1, 65535)

def criar_menssagem(tipo,identificador):
    byte1 = 0b00000000
    bytes_identificador = dividir_numero_2_bytes(identificador) 
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
    tamanho_resposta = dados[3]
    lista_bytes = []
    match byte1:
        case 0x10:
            for i in range(tamanho_resposta):
                lista_bytes.append(dados[4+i]) 
            return bytes_to_string(lista_bytes)
        case 0x11:
            for i in range(tamanho_resposta):
                lista_bytes.append(dados[4+i]) 
            return bytes_to_string(lista_bytes)
        case 0x12:
            for i in range(tamanho_resposta):
                lista_bytes.append(dados[4+i]) 
            return bytes_to_int(lista_bytes)