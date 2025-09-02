def bubble_sort(lista):
    """
    Implementa o algoritmo Bubble Sort com contagem de comparações e trocas.

    Args:
        lista (list): A lista de números a ser ordenada.

    Returns:
        dict: Um dicionário contendo o número de 'trocas' e 'comparacoes'.
    """
    # Cria uma cópia da lista para não alterar a original
    lista_copiada = lista.copy()
    n = len(lista_copiada)
    trocas = 0
    comparacoes = 0

    # Loop externo que percorre toda a lista
    for i in range(n):
        # Loop interno que "flutua" o maior elemento para o final
        # A cada passada do loop externo, o maior elemento já está no lugar certo
        for j in range(0, n - i - 1):
            # Incrementa o contador de comparações
            comparacoes += 1
            # Compara elementos adjacentes
            if lista_copiada[j] > lista_copiada[j + 1]:
                # Realiza a troca se o elemento da esquerda for maior
                lista_copiada[j], lista_copiada[j + 1] = (
                    lista_copiada[j + 1],
                    lista_copiada[j],
                )
                # Incrementa o contador de trocas
                trocas += 1

    return {"trocas": trocas, "comparacoes": comparacoes}


def selection_sort(lista):
    """
    Implementa o algoritmo Selection Sort com contagem de comparações e trocas.

    Args:
        lista (list): A lista de números a ser ordenada.

    Returns:
        dict: Um dicionário contendo o número de 'trocas' e 'comparacoes'.
    """
    lista_copiada = lista.copy()
    n = len(lista_copiada)
    trocas = 0
    comparacoes = 0

    # Loop externo que define a posição a ser preenchida com o menor elemento
    for i in range(n):
        # Assume que o menor elemento está na posição atual
        id_minimo = i
        # Loop interno para encontrar o menor elemento no restante da lista
        for j in range(i + 1, n):
            # Incrementa o contador de comparações
            comparacoes += 1
            # Se encontrar um elemento menor, atualiza o índice do mínimo
            if lista_copiada[j] < lista_copiada[id_minimo]:
                id_minimo = j

        # Após encontrar o menor elemento, faz a troca com a posição atual
        # Esta troca acontece apenas uma vez por passada do loop externo
        if id_minimo != i:
            lista_copiada[i], lista_copiada[id_minimo] = (
                lista_copiada[id_minimo],
                lista_copiada[i],
            )
            # Incrementa o contador de trocas
            trocas += 1

    return {"trocas": trocas, "comparacoes": comparacoes}


def insertion_sort(lista):
    """
    Implementa o algoritmo Insertion Sort com contagem de comparações e trocas.

    Args:
        lista (list): A lista de números a ser ordenada.

    Returns:
        dict: Um dicionário contendo o número de 'trocas' e 'comparacoes'.
    """
    lista_copiada = lista.copy()
    n = len(lista_copiada)
    trocas = 0
    comparacoes = 0

    # Começa do segundo elemento, pois o primeiro já é considerado "ordenado"
    for i in range(1, n):
        # Guarda o elemento que será inserido na parte ordenada da lista
        chave = lista_copiada[i]
        j = i - 1

        # Move os elementos da parte ordenada que são maiores que a 'chave'
        # uma posição para a frente, abrindo espaço para a 'chave'

        # A comparação acontece dentro da condição do while
        while j >= 0:
            comparacoes += 1
            if chave < lista_copiada[j]:
                lista_copiada[j + 1] = lista_copiada[j]
                # Contamos cada deslocamento como uma "troca" para fins de análise
                trocas += 1
                j -= 1
            else:
                # Se a chave não for menor, encontramos o local de inserção
                break

        # Insere a chave na posição correta
        lista_copiada[j + 1] = chave

    return {"trocas": trocas, "comparacoes": comparacoes}
