import numpy as np


def gerar_array_ordenado(tamanho):
    """
    Gera um array ordenado em ordem crescente (melhor caso).

    Args:
        tamanho (int): O número de elementos no array.

    Returns:
        list: Uma lista de números inteiros ordenados.
    """
    # np.arange cria uma sequência de números (0, 1, 2, ...)
    # e .tolist() converte para uma lista Python.
    return np.arange(tamanho).tolist()


def gerar_array_aleatorio(tamanho):
    """
    Gera um array com elementos em ordem aleatória (caso médio).

    Args:
        tamanho (int): O número de elementos no array.

    Returns:
        list: Uma lista de números inteiros em ordem aleatória.
    """
    # np.random.permutation cria uma permutação aleatória de uma sequência
    # de números. Usamos np.arange(tamanho) como a sequência base.
    return np.random.permutation(np.arange(tamanho)).tolist()


def gerar_array_inversamente_ordenado(tamanho):
    """
    Gera um array ordenado em ordem decrescente (pior caso).

    Args:
        tamanho (int): O número de elementos no array.

    Returns:
        list: Uma lista de números inteiros em ordem decrescente.
    """
    # Gera um array ordenado (0, 1, 2,...) e depois o inverte (..., 2, 1, 0)
    return np.arange(tamanho)[::-1].tolist()
