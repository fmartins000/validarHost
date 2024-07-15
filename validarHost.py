import subprocess
import socket

# Lista de endereços IP para pingar
ips = ['IPS']


# Dicionários para armazenar os resultados
ping_sucesso = {}
ping_falha = {}

# Função para verificar o status de ping de um endereço IP
def pingar(ip):
    try:
        # Executar o comando de ping
        subprocess.run(['ping', '-c', '1', ip], check=True, stdout=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

# Alterar sobre os endereços IP e pingar cada um
for ip in ips:
    if pingar(ip):
        ping_sucesso[ip] = ip  # Armazenar apenas o endereço IP em caso de sucesso
    else:
        ping_falha[ip] = 'Host inacessível'

# Gerar relatório
print("Endereços IP que responderam ao ping:")
for ip in ping_sucesso.values():
    print(ip)

print("\nEndereços IP que não responderam ao ping:")
for ip, status in ping_falha.items():
    print(f"{ip}: {status}")
