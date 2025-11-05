# portscan_telesz.py
import socket
import sys

BANNER = r"""
████████╗███████╗██╗     ███████╗███████╗███████╗
╚══██╔══╝██╔════╝██║     ██╔════╝██╔════╝██╔════╝
   ██║   █████╗  ██║     █████╗  ███████╗█████╗  
   ██║   ██╔══╝  ██║     ██╔══╝  ╚════██║██╔══╝  
   ██║   ███████╗███████╗███████╗███████║███████╗
   ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝
"""

COMMON_PORTS = [
    20, 21, 22, 23, 25, 53, 80, 110, 143, 161, 389, 443, 445, 465, 587,
    636, 993, 995, 1080, 1194, 139, 3306, 3389, 5432, 5900, 6379, 8080,
    8443, 9200, 9300, 27017
]

def scan(host, ports):
    print(f"[i] Iniciando scan em {host}...\n")
    for port in ports:
        try:
            port = int(port)
        except ValueError:
            print(f"[x] Porta inválida (pulando): {port}")
            continue

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.2)  # ajuste se precisar
        try:
            code = client.connect_ex((host, port))
            if code == 0:
                print(f"[+] Porta {port} \tABERTA")
            else:
                print(f"[-] Porta {port} \tFECHADA")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário.")
            client.close()
            return
        except Exception as e:
            print(f"[!] Erro ao conectar {host}:{port} -> {e}")
        finally:
            client.close()
    print("\n[i] Scan finalizado.")

if __name__ == "__main__":
    # Mostra o banner
    print(BANNER)

    # Se o usuário passar argumentos pelo terminal: host e (opcional) portas
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            # aceita "22,80,443" ou "22, 80, 443"
            ports = [p.strip() for p in sys.argv[2].split(",") if p.strip()]
        else:
            ports = COMMON_PORTS
    else:
        # Pergunta o host via input()
        host = input("Digite o host (ex: example.com ou 127.0.0.1): ").strip()
        ports_input = input("Digite portas separadas por vírgula (ENTER para padrão): ").strip()
        if ports_input:
            ports = [p.strip() for p in ports_input.split(",") if p.strip()]
        else:
            ports = COMMON_PORTS

    print(f"\n[i] Escaneando {host} nas portas: {', '.join(str(p) for p in ports)}\n")
    try:
        scan(host, ports)
    except Exception as e:
        print(f"[!] Erro durante o scan: {e}")

    # Mantém a janela aberta até o usuário pressionar ENTER
    try:
        input("\nPressione ENTER para fechar...")
    except KeyboardInterrupt:
        # Se apertar Ctrl+C aqui, só sai
        print("\nSaindo...")
