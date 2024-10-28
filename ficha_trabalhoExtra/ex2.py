def countWord(texto, palavra):
    """
    Function for counting how many times a word occurs on a text and returns it´s positions
    Args: texto(string), palavra(string)
    """
    count = 0  # Contador de ocorrências
    positions = []  # Lista para armazenar as posições
    start = 0
    
    # Loop para encontrar todas as ocorrências e posições da palavra
    while start < len(texto):
        position = texto.find(palavra, start)
        if position == -1:  # Se não encontrar mais ocorrências, interrompe
            break
        count += 1
        positions.append(position + 1)  # Adiciona 1 à posição para começar a contagem em 1
        start = position + len(palavra)  # Move o índice de início para após a palavra encontrada
    
    return f"A palavra '{palavra}' ocorre {count} vezes no texto. Nas posições {positions}"

# Teste da função
texto = input("Texto: ")
palavra = input("Pesquisa: ")
print(countWord(texto, palavra))
