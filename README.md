made by ME

**PortScan** — scanner de portas TCP simples em Python.

Uma ferramenta pequena e direta para varredura de portas comuns em um host. Ideal para aprendizado e uso em ambientes que você controla.

---

## Características

* Varre portas TCP usando `socket.connect_ex()`.
* Lista padrão de portas comuns (HTTP, SSH, SMTP, SMB, bancos de dados, etc.).
* Aceita host via argumento ou `input()` interativo.
* Imprime se cada porta está **ABERTA** ou **FECHADA**.
* Timeout configurado no código (padrão `0.2`s).
