from src.tester import rodar_testes
from src.analyzer import processar_e_salvar_resultados


def main():
    """
    Função principal que orquestra a execução do projeto.
    """
    print("Iniciando a análise de desempenho dos algoritmos de ordenação...")

    # Passo 1: Executa todos os testes definidos no módulo tester
    # A função rodar_testes retorna uma lista com os dicionários de resultados
    resultados_dos_testes = rodar_testes()

    print("\nTestes concluídos. Gerando análises e gráficos...")

    # Passo 2: Passa os resultados para o módulo analyzer
    # A função processar_e_salvar_resultados irá criar o CSV e os gráficos
    processar_e_salvar_resultados(resultados_dos_testes)

    print("\nAnálise concluída com sucesso!")
    print("Verifique a pasta 'results' para ver o arquivo CSV e os gráficos gerados.")


# Garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()
