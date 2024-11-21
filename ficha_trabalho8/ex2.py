import os
import random

ficheiro = "ficha_trabalho8/ficheiros/paises.txt"

def imprimePais(paisEscolhido, tentativas):
    """
    Função que exibe o país com "-" nos caracteres ainda ocultos e revela gradualmente.
    """
    resultado = ""
    for i, letra in enumerate(paisEscolhido):
        if i < tentativas: 
            resultado += letra
        else:
            resultado += "-"
    return resultado

def jogoAdivinhaPais():
    """
    Função principal do jogo.
    """
    # Verifica se o arquivo existe
    if not os.path.exists(ficheiro):
        print(f"Erro: O arquivo '{ficheiro}' não foi encontrado.")
        return
    
    # Lê os países do arquivo
    with open(ficheiro, "r", encoding="utf-8") as f:
        paises = [line.strip() for line in f]
    
        paisEscolhido = random.choice(paises)

    tentativas = 1
    maxTentativas = 3
    acertou = False

    print("\t\tAdivinhe o nome do pais")
    
    while tentativas-1 < maxTentativas:
        print("\n" + imprimePais(paisEscolhido, tentativas))
        tentativa = input(f"Tentativa {tentativas + 1}: Qual é o país? ").strip()

        if tentativa.lower() == paisEscolhido.lower():
            acertou = True
            break
        else:
            print("Resposta incorreta. Tente novamente.")
        
        tentativas += 1
    
    if acertou:
        print(f"\nAcertou!! O país era: {paisEscolhido}")
    else:
        print(f"\nNão Acertou!! O país era: {paisEscolhido}")

jogoAdivinhaPais()