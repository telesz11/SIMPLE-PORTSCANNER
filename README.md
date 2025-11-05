# portscan mande by telesz

**PortScan** — scanner de portas TCP simples em Python.

Uma ferramenta pequena e direta para varredura de portas comuns em um host. Ideal para aprendizado e uso em ambientes que você controla.

---

## Características

* Varre portas TCP usando `socket.connect_ex()`.
* Lista padrão de portas comuns (HTTP, SSH, SMTP, SMB, bancos de dados, etc.).
* Aceita host via argumento ou `input()` interativo.
* Imprime se cada porta está **ABERTA** ou **FECHADA**.
* Timeout configurado no código (padrão `0.2`s).
* Espera o usuário pressionar ENTER antes de fechar (útil no Windows).

---

## Como usar

### 1. Executar em modo interativo (padrão)

```bash
python portscan_telesz.py
```

O programa vai mostrar o banner e pedir que você digite o host. Depois pede portas (ou ENTER para usar a lista padrão).

### 2. Passar o host por argumento (usa lista padrão de portas)

```bash
python portscan_telesz.py example.com
```

### 3. Passar host e portas específicas

```bash
python portscan_telesz.py example.com 22,80,443
```

As portas devem ser separadas por vírgula (sem espaços obrigatórios).

---

## Personalização

* Para alterar as portas padrão, edite a lista `COMMON_PORTS` no topo do script.
* Para aumentar o timeout, mude `client.settimeout(0.2)` no corpo da função `scan`.
* Para acelerar, considere adicionar multithreading com `concurrent.futures.ThreadPoolExecutor`.

