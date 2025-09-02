import time

# Importa as funções dos nossos outros arquivos
from .sorting_algorithms import bubble_sort, selection_sort, insertion_sort
from .data_generator import (
    gerar_array_ordenado,
    gerar_array_aleatorio,
    gerar_array_inversamente_ordenado,
)


def rodar_testes():
    """
    Executa os testes de desempenho para os algoritmos de ordenação
    e coleta os resultados.
    """
    # Parâmetros do teste, conforme especificado no projeto
    tamanhos = [
        10,
        100,
        1000,
        10000,
    ]  # Tamanhos dos arrays a serem testados
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
    }
    cenarios = {
        "Melhor Caso (Ordenado)": gerar_array_ordenado,
        "Caso Médio (Aleatório)": gerar_array_aleatorio,
        "Pior Caso (Inverso)": gerar_array_inversamente_ordenado,
    }

    # Lista para armazenar todos os resultados
    resultados_finais = []

    # Número de execuções para o caso médio para calcular a média
    num_execucoes_caso_medio = 10  # Conforme sugestão do projeto

    # Loop principal que itera sobre cada algoritmo
    for nome_algoritmo, funcao_algoritmo in algoritmos.items():
        # Loop que itera sobre cada tamanho de array
        for tamanho in tamanhos:
            # Loop que itera sobre cada cenário de dados
            for nome_cenario, funcao_geradora in cenarios.items():
                # Tratamento especial para o caso médio
                if nome_cenario == "Caso Médio (Aleatório)":
                    tempos = []
                    trocas_lista = []
                    comparacoes_lista = []
                    print(
                        f"Testando {nome_algoritmo} - Tamanho: {tamanho} - {nome_cenario} ({num_execucoes_caso_medio}x)..."
                    )

                    for _ in range(num_execucoes_caso_medio):
                        array_teste = funcao_geradora(tamanho)

                        inicio = time.time()
                        stats = funcao_algoritmo(array_teste)
                        fim = time.time()

                        tempos.append(fim - inicio)
                        trocas_lista.append(stats["trocas"])
                        comparacoes_lista.append(stats["comparacoes"])

                    # Calcula a média dos resultados
                    tempo_medio = sum(tempos) / num_execucoes_caso_medio
                    trocas_medio = sum(trocas_lista) / num_execucoes_caso_medio
                    comparacoes_medio = (
                        sum(comparacoes_lista) / num_execucoes_caso_medio
                    )

                    resultado = {
                        "algoritmo": nome_algoritmo,
                        "cenario": nome_cenario,
                        "tamanho": tamanho,
                        "tempo": tempo_medio,
                        "trocas": trocas_medio,
                        "comparacoes": comparacoes_medio,
                    }

                else:  # Para melhor e pior caso, executa apenas uma vez
                    print(
                        f"Testando {nome_algoritmo} - Tamanho: {tamanho} - {nome_cenario}..."
                    )
                    array_teste = funcao_geradora(tamanho)

                    # Mede o tempo de execução
                    inicio = time.time()
                    stats = funcao_algoritmo(array_teste)
                    fim = time.time()

                    resultado = {
                        "algoritmo": nome_algoritmo,
                        "cenario": nome_cenario,
                        "tamanho": tamanho,
                        "tempo": fim - inicio,
                        "trocas": stats["trocas"],
                        "comparacoes": stats["comparacoes"],
                    }

                # Adiciona o dicionário de resultado na lista final
                resultados_finais.append(resultado)
                print("Concluído.")

    return resultados_finais


# Exemplo de como usar a função.
# No nosso projeto final, o main.py que vai chamar isso.
if __name__ == "__main__":
    resultados = rodar_testes()
    # Imprime os resultados de forma legível
    for res in resultados:
        print(res)
