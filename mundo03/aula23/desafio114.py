import urllib.request

def verifica_conexao():
    try:
        # Tenta abrir uma conexão com o Google
        urllib.request.urlopen('https://www.google.com', timeout=5)
        print("Você está conectado à Internet!")
    except urllib.error.URLError:
        print("Sem acesso à Internet.")
    except TimeoutError:
        print("A solicitação expirou.")

# Testa a conexão
verifica_conexao()
