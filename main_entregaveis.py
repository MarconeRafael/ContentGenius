import os
import pandas as pd
from inputs_entregaveis import coletar_dados_entregaveis  # Função para coletar os dados de entrada
from gerador_entregaveis import gerar_entregaveis          # Função para gerar entregáveis

def processar_entregaveis(dados, caminho_arquivo):
    """
    Processa os dados coletados e gera o arquivo final com os entregáveis detalhados.
    """
    print("Gerando entregáveis a partir dos dados fornecidos...")
    try:
        caminho_arquivo = gerar_entregaveis(dados, caminho_arquivo)
        if caminho_arquivo:
            print(f"Opção escolhida salva com sucesso em: {caminho_arquivo}")
            return True
    except Exception as e:
        print(f"Erro ao gerar entregáveis: {e}")
    return False

def main():
    # Coleta de detalhes dos entregáveis
    print("Coletando dados para os entregáveis...")
    dados = coletar_dados_entregaveis()
    
    # Checar se os dados foram coletados corretamente
    if not dados:
        print("Erro: Dados não coletados corretamente.")
        return
    
    # Definir o caminho do arquivo para salvar os entregáveis
    caminho_arquivo = 'csvs/entregaveis.csv'  # Ou outro caminho desejado
    
    # Processar os entregáveis
    if not processar_entregaveis(dados, caminho_arquivo):
        return


# Chamar a função main
if __name__ == "__main__":
    main()
