# Importando bibliotecas
import subprocess
import sys
import os
import time as tm

# Exibindo cabeçalho do programa
print("#-------------------------------------------------#")
print("Iniciando verificação de instalação das bibliotecas")
print("#-------------------------------------------------#")
print("")
tm.sleep(1)


# Criando função que verifica a instalação das bibliotecas
def verificar_instalacao(biblioteca):
    # Tenta realizar a conferencia de instalação
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", biblioteca])
        return True

    # Caso o ocorra algum erro, exibe a mensagem de erro e retorna o atributo de falso
    except subprocess.CalledProcessError:
        return False


# Cria função que instala as bibliotecas
def instalar_bibliotecas(biblioteca):
    # Caso a biblioteca já esteja instalada, retorna a mensagem ao usuário dizendo que a mesma já se econtra instalada
    if verificar_instalacao(biblioteca):
        print(f"A biblioteca {biblioteca} já está instalada")
        print("")
        print("#----------------------------#")
        print("")

    # Caso retorne falso, a instalação da biblioteca é realizada
    else:

        # Cria laço de tentativa, onde o script tenta realizar a instalação de maneira comum, usando os statements sistemicos do pip install, descartando a função master por '-m'
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
            print(f"Instalação bem-sucedida! Biblioteca {biblioteca} instalada com sucesso!")
            print("")
            print("#----------------------------#")
            print("")

        # Caso a instalação por meios comuns retorne algum erro, uma exceção é gerada e retorna uma mensagem de erro
        except subprocess.CalledProcessError as e:
            print(f"Erro durante a instalação da biblioteca {biblioteca}: {e}")
            print("")
            print("#----------------------------#")
            print("")


# Passa a lista de bibliotecas que serão instaladas
lista_bibliotecas_instalacao = ["flet", "numpy", "requests", "pandas", "pymssql"]

# Cria laço de repetição para o uso da função de instalar biblioteca
for biblioteca in lista_bibliotecas_instalacao:
    instalar_bibliotecas(biblioteca)

# Exibe cabeçalho final
print("#-------------------------------------------------------#")
print("Conferencia e instalação de pacotes realizada com sucesso")
print("#-------------------------------------------------------#")
tm.sleep(5)