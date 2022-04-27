import socket 
import sys

def connect(addr):

    a = addr.split(":")
    ip = a[0]
    port = int(a[1])

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print ("Erro na criação do socket : %s" %(err))
 
    try:
        host_ip = socket.gethostbyname(ip)
        print("Conectado!")
    except socket.gaierror:
 
        print("Não foi possível encontrar o servidor")
        sys.exit()
 
    s.connect((host_ip, port))
    message = s.recv(1024)
    print(message.decode())
    s.close()


def main():
    x = ''
    while (True):
        x = input("Digite o endereço e a porta ou 'exit' para sair\n")
        if (x == 'exit'):
            sys.exit()
        connect(x)

if __name__ == "__main__":
    main()  