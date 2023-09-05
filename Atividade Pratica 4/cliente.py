import socket

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_address = ('127.0.0.1', 8888)  # Novo endereço IP e porta
    print("Conectando %s porta %s" % server_address)
    
    try:
        sock.connect(server_address)
        while True:
            message = input("Digite o comando (d/h/dh) ou /sair: ")
            sock.sendall(message.encode('utf-8'))
            print("Esperando resposta...")
            
            data = sock.recv(2048).decode()
            print(data)
            
            if data == "/sair":
                sock.close()
                break
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    client()
