import socket
import funcoes_aux 
    
print("Tipos da requisção: ")
print("1 Data e hora atual;")
print("2 Uma mensagem motivacional para o fim do semestre;")
print("3 A quantidade de respostas emitidas pelo servidor até o momento;")
print("digite 'sair' para encerrar o programa.")
ip_servidor = '15.228.191.109'

porta = 50000
while True: 
    tipo = input("Digite o tipo da requisção desejada: ")
    if(tipo == 'sair'):
        print("adeus ʕ •ɷ•ʔฅ ")
        break
    socket_raw = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)   
    mensagem = funcoes_aux.criar_menssagem(int(tipo),funcoes_aux.sortear_identificador()) #Cria a messangem a ser passada para o servidor de acordo com a requisão
    #criar_o_cabeçalho_UDP;
    #criar_cabeçalho_IP; 
    endereco_destino = (ip_servidor, porta) #Endereço do servidor
    socket_raw.sendto(mensagem, endereco_destino)
    dados, endereco_origem = socket_raw.recvfrom(2040) #Recebe a resposta do servidor
    resposta = funcoes_aux.decodificar_resposta(dados) # Decodifica a resposta de acordo com o tipo da requesição
    print(resposta)

    socket_raw.close()