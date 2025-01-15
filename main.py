import os
from coleta_roteiro import collect_script_details  # Importa a função para coletar os detalhes do roteiro
from gera_roteiro import gerar_roteiro             # Importa a função para gerar roteiros
import pandas as pd

def processar_roteiro(detalhes_df, caminho_arquivo):
    """
    Processa os dados do roteiro e gera o arquivo final com os roteiros detalhados.
    """
    print("Gerando roteiros a partir dos detalhes fornecidos...")
    try:
        roteiro_gerado = gerar_roteiro(caminho_arquivo)
        if roteiro_gerado:
            print(f"Roteiros gerados e salvos com sucesso em: {roteiro_gerado}")
            return True
    except Exception as e:
        print(f"Erro ao gerar roteiros: {e}")
    return False

def main():
    # Coleta de detalhes do roteiro
    print("Coletando detalhes do roteiro...")
    caminho_arquivo = collect_script_details()
    
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return
    
    # Carregar o arquivo CSV com os detalhes
    try:
        detalhes_df = pd.read_csv(caminho_arquivo, encoding='utf-8')
        print("Detalhes do roteiro carregados com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o arquivo CSV: {e}")
        return
    
    # Processar o roteiro
    if not processar_roteiro(detalhes_df, caminho_arquivo):
        return

# Chamar a função main
if __name__ == "__main__":
    main()