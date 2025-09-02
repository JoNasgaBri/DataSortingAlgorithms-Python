import pandas as pd
import matplotlib.pyplot as plt
import os


def processar_e_salvar_resultados(resultados):
    """
    Converte os resultados para um DataFrame do Pandas, salva em CSV e gera os gráficos.
    """
    # Cria a pasta 'results' se ela não existir
    if not os.path.exists("results"):
        os.makedirs("results")

    # Converte a lista de dicionários para um DataFrame do Pandas
    df = pd.DataFrame(resultados)

    # Salva os dados brutos em um arquivo CSV na pasta 'results'
    caminho_csv = os.path.join("results", "resultados_completos.csv")
    df.to_csv(caminho_csv, index=False)
    print(f"Resultados salvos em '{caminho_csv}'")

    # Gera os gráficos
    gerar_graficos_tempo_execucao(df)
    gerar_graficos_comparacoes_trocas(df)

    print("Gráficos gerados e salvos na pasta 'results'.")


def gerar_graficos_tempo_execucao(df):
    """
    Gera gráficos de linha comparando o tempo de execução dos algoritmos.
    Um gráfico para cada cenário.
    """
    cenarios = df["cenario"].unique()

    for cenario in cenarios:
        plt.figure(figsize=(10, 6))

        # Filtra os dados para o cenário atual
        df_cenario = df[df["cenario"] == cenario]

        # Agrupa por algoritmo e plota uma linha para cada um
        for algoritmo in df_cenario["algoritmo"].unique():
            df_algoritmo = df_cenario[df_cenario["algoritmo"] == algoritmo]
            plt.plot(
                df_algoritmo["tamanho"],
                df_algoritmo["tempo"],
                marker="o",
                label=algoritmo,
            )

        plt.title(f"Tempo de Execução x Tamanho do Array ({cenario})")
        plt.xlabel("Tamanho do Array")
        plt.ylabel("Tempo de Execução (segundos)")
        plt.xscale("log")  # Escala logarítmica para melhor visualização dos tamanhos
        plt.yscale("log")  # Escala logarítmica para melhor visualização do tempo
        plt.grid(True, which="both", ls="--")
        plt.legend()

        # Salva o gráfico em um arquivo PNG
        nome_arquivo = f"tempo_execucao_{cenario.replace(' ', '_').lower()}.png"
        caminho_grafico = os.path.join("results", nome_arquivo)
        plt.savefig(caminho_grafico)
        plt.close()


def gerar_graficos_comparacoes_trocas(df):
    """
    Gera gráficos de barra comparando o número de comparações e trocas
    apenas para o Caso Médio.
    """
    # Filtra os dados apenas para o "Caso Médio (Aleatório)"
    df_medio = df[df["cenario"] == "Caso Médio (Aleatório)"].copy()

    # --- Gráfico de Comparações ---
    plt.figure(figsize=(12, 7))
    # Usaremos o tamanho do array como uma forma de agrupar as barras
    df_medio.pivot(index="tamanho", columns="algoritmo", values="comparacoes").plot(
        kind="bar"
    )

    plt.title("Número de Comparações (Caso Médio)")
    plt.xlabel("Tamanho do Array")
    plt.ylabel("Número Médio de Comparações")
    plt.xticks(rotation=45)
    plt.tight_layout()  # Ajusta o layout para não cortar os labels

    nome_arquivo = "comparacoes_caso_medio.png"
    caminho_grafico = os.path.join("results", nome_arquivo)
    plt.savefig(caminho_grafico)
    plt.close()

    # --- Gráfico de Trocas ---
    plt.figure(figsize=(12, 7))
    df_medio.pivot(index="tamanho", columns="algoritmo", values="trocas").plot(
        kind="bar"
    )

    plt.title("Número de Trocas (Caso Médio)")
    plt.xlabel("Tamanho do Array")
    plt.ylabel("Número Médio de Trocas")
    plt.xticks(rotation=45)
    plt.tight_layout()

    nome_arquivo = "trocas_caso_medio.png"
    caminho_grafico = os.path.join("results", nome_arquivo)
    plt.savefig(caminho_grafico)
    plt.close()
