import threading
import random
import time

# Definindo um semáforo para controlar o acesso às caixas
semaforo_caixas = threading.Semaphore(3)

# Definindo a fila de clientes (30 clientes em espera)
fila_de_clientes = list(range(30))

def cliente(cliente_id):
    # Simula o tempo de chegada do cliente
    chegada = random.randint(1, 10)
    time.sleep(chegada)

    # Entra na fila
    print(f'Cliente {cliente_id} chegou e entrou na fila.')

    # Aguarda por uma caixa disponível
    semaforo_caixas.acquire()
    print(f'Cliente {cliente_id} está sendo atendido.')

    # Simula o tempo de atendimento
    tempo_atendimento = random.randint(3, 10)
    time.sleep(tempo_atendimento)

    # Cliente terminou o atendimento
    semaforo_caixas.release()
    print(f'Cliente {cliente_id} terminou o atendimento.')

# Inicializa as threads para os clientes
threads_clientes = []
for cliente_id in fila_de_clientes:
    cliente_thread = threading.Thread(target=cliente, args=(cliente_id,))
    threads_clientes.append(cliente_thread)
    cliente_thread.start()

# Aguarda todas as threads dos clientes terminarem
for cliente_thread in threads_clientes:
    cliente_thread.join()

print("Todos os clientes foram atendidos.")
