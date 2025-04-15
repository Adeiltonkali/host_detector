import platform
import subprocess

def ping_host(ip):
    comando = ['ping', '-n', '1', ip] if platform.system().lower() == 'windows' else ['ping', '-c', '1', ip]

    try:
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def ping_sweep():
    ativos = []
    for i in range(1, 255):
        ip = f'192.168.1.{i}'
        if ping_host(ip):
            ativos.append(i)
            print(f'host ativo encontrado: {ip}')
    return ativos
if __name__=='__main__':
    ativos = ping_sweep()
    print("\nHosts ativos na rede local:")
    for ip in ativos:
        print(ip)