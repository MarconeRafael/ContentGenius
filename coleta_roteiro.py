import pandas as pd
import os

def collect_script_details():
    print("Preencha as informações detalhadas do roteiro estratégico e personalizado para o creator:\n")

    # Coletar as informações de entrada com os campos solicitados
    data = {
        "Briefing": input(
            "Briefing (descrição geral da campanha. Exemplo: 'Fortalecer a presença da marca no mercado fitness com foco em conteúdo educativo sobre nossos suplementos'): "
        ).strip(),
        "Nome do Creator": input(
            "Nome do creator (exemplo: 'João Fitness'): "
        ).strip(),
        "Tom de Voz": input(
            "Tom de voz (exemplo: 'Divertido, educativo, inspirador'): "
        ).strip(),
        "Formatos Preferidos pelo Creator": input(
            "Formatos preferidos pelo creator (exemplo: 'Storytelling, transições rápidas, reviews detalhados'): "
        ).strip(),
        "Objetivo da Campanha": input(
            "Objetivo da campanha (exemplo: 'Fortalecer a presença da marca no mercado fitness'): "
        ).strip(),
        "Conversão Desejada": input(
            "Conversão desejada (exemplo: 'Aumentar vendas em 20%'): "
        ).strip(),
        "Canais de Divulgação": input(
            "Canais de divulgação (exemplo: 'Instagram Reels, TikTok'): "
        ).strip(),
        "Estilo do Creator": input(
            "Estilo do creator (exemplo: 'Engajado, autêntico, descontraído'): "
        ).strip(),
        "Flag": input(
            "Flag (exemplo: 'PT-BR, EN-US'): "
        ).strip(),
    }

    # Criar o diretório caso não exista
    os.makedirs("csvs", exist_ok=True)
    
    # Criação do DataFrame com os dados coletados
    script_df = pd.DataFrame([data])
    
    # Definir o nome e o caminho do arquivo CSV
    file_name = "roteiro_detalhes.csv"
    file_path = os.path.join(os.getcwd(), "csvs", file_name)
    
    try:
        # Salvar o DataFrame em um arquivo CSV
        script_df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Detalhes do roteiro salvos em: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
    
    return file_path

# Chamando a função
# caminho_csv = collect_script_details()
# print(f"Arquivo salvo no caminho: {caminho_csv}")
