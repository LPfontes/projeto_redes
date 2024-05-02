import types
import random
consts = types.SimpleNamespace()
consts.DATA = 1
consts.MENSAGEM_MOTIVACIONAL = 2
consts.QUANTIDADE_RESPOSTAS_SERVIDOR = 3

def cheksum(lista_bytes):
    tamanho_lista = len(lista_bytes)
    if tamanho_lista % 2 == 0: # Verfica se o tamanho da lista_bytes é par 
       pass
    else:
        lista_bytes = lista_bytes + bytes([0]) # Se não, adiciona um byte zero no fim da lista
    tamanho_lista = len(lista_bytes) # Atualiza o tamanho da lista
    index = 0
    resultado = 0
    for i in range(int(tamanho_lista/4)):
        # Soma as palavras de 16 bits na lista e soma com a palavra guardada em resultado
        resultado = somar_palavra_16bits(resultado,somar_palavra_16bits(lista_bytes[index] << 8 | lista_bytes[index+1],lista_bytes[index+2]<< 8 |lista_bytes[index+3])) 
        index += 4 
    return ~resultado & 0xFFFF #inverte os bits do resultado
        
def somar_palavra_16bits(palavra1,palavra2):
    resultado =  palavra1 + palavra2 
    while resultado.bit_length() > 16: # Verifica se a soma da palavra1 + palavra2 tem mais de 16 bits se sim um carryout do bit mais significativo vai ser somada ao resultado
        carry = resultado >> 16
        resultado &= 0xFFFF
        resultado += carry
    return resultado

def dividir_numero_2_bytes(numero): # Divide um int em uma lista com 2 bytes seguindo a ordenação big endian
    numero = numero.to_bytes(2,byteorder='big')
    return numero

def trasformar_string_ip_em_bytes(ip): # Remove os pontos da string ip e trasforma a string em uma lista de bytes 
    lista_string = ip.split('.')
    lista_int = []
    for i in lista_string:
        lista_int.append(int(i)) 
    return bytes(lista_int)
    
def sortear_identificador():  # Retorna um numero aleatorio de 1 a 65535
    return random.randint(1, 65535)

def criar_requisao(tipo,identificador): # Codifica a requisão de acordo com as especificação do projeto
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
  
def bytes_to_string(lista_bytes): # Trasforma uma lista de bytes em um string
    return ''.join(chr(i) for i in lista_bytes)

def bytes_to_int(lista_bytes): # Trasforma uma lista de bytes em um int
    return int.from_bytes(bytes(lista_bytes), byteorder='big')
   
def decodificar_resposta(dados): # Decodifica a resposta de acordo com as especificação do projeto
    tipo = dados[0]
    tamanho_resposta = dados[3]
    lista_bytes = []
    match tipo:
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