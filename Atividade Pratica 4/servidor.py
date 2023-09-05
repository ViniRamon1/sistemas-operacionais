import socket
import threading
from datetime import datetime

def handle_client(client):
    try:
        while True:
            data = client.recv(2048).decode()
            
            if not data:
                break
            
            if data == "d":
                response = datetime.today().strftime('%Y-%m-%d')
            elif data == "h":
                response = datetime.today().strftime('%H:%M:%S')
            elif data == "dh":
                response = datetime.today().strftime('%Y-%m-%d / %H:%M:%S')
            elif data == "/sair":
                response = "/sair"
            else:
                response = "Comando inválido!"
            
            client.sendall(response.encode())
            
            if data == "/sair":
                break
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        client.close()

def server(host='127.0.0.1', port=8888):  # Novo endereço IP e porta
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    print("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(5)
    
    try:
        while True:
            client, address = sock.accept()
            print(f"Conexão recebida de {address[0]}:{address[1]}")
            
            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()
    except KeyboardInterrupt:
        print("Servidor encerrado.")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    server()
