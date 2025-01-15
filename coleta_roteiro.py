import pandas as pd
import os

def collect_script_details():
    print("Preencha as informações detalhadas do roteiro:\n")

    data = {
        "Objetivo Principal": input("Objetivo principal (exemplo: 'Aumentar visibilidade e atrair leads qualificados'): ").strip(),
        "Ação Esperada do Público": input("Ação esperada do público (exemplo: 'Visitar o site e se inscrever para desconto'): ").strip(),
        
        "Público-Alvo": input("Público-alvo (exemplo: 'Mulheres de 25 a 40 anos, interessadas em beleza e autocuidado'): ").strip(),
        "Problemas/Aspirações": input("Problemas/Aspirações do público (exemplo: 'Procuram produtos eficazes e sustentáveis'): ").strip(),
        "Como Consomem Conteúdo": input("Como consomem conteúdo (exemplo: 'Preferem vídeos curtos e visualmente atrativos'): ").strip(),
        
        "Estilo de Comunicação": input("Estilo de comunicação (exemplo: 'Inspirador, acolhedor e educativo'): ").strip(),
        "Referência de Tom/Estilo": input("Referência de tom/estilo (exemplo: 'The Body Shop'): ").strip(),
        
        "Plataforma": input("Plataforma (exemplo: 'Instagram e TikTok'): ").strip(),
        "Formato de Publicação": input("Formato de publicação (exemplo: 'Vídeos curtos de 30 a 60 segundos'): ").strip(),
        
        "Produto Promovido": input("Produto promovido (exemplo: 'Linha de cuidados faciais naturais'): ").strip(),
        "Benefícios/Diferenciais": input("Benefícios/diferenciais (exemplo: 'Fórmulas veganas, embalagens recicláveis'): ").strip(),
        "Detalhes Técnicos": input("Detalhes técnicos (exemplo: '15% de desconto para novos clientes'): ").strip(),
        
        "CTA Esperado": input("CTA esperado (exemplo: 'Inscreva-se no link da bio para 15% de desconto'): ").strip(),
        
        "Materiais Visuais Disponíveis": input("Materiais visuais disponíveis (exemplo: 'Imagens de alta qualidade e vídeos com clientes reais'): ").strip(),
        "Elementos Criativos": input("Elementos criativos (exemplo: 'Storytelling com rotina de skincare'): ").strip(),
        
        "Prazo": input("Prazo (exemplo: 'Roteiro entregue até sexta-feira'): ").strip(),
        "Frequência de Publicação": input("Frequência de publicação (exemplo: 'Um post por dia durante uma semana'): ").strip(),
        
        "Métricas Esperadas": input("Métricas esperadas (exemplo: 'Taxa de cliques, número de cadastros, engajamento'): ").strip()
    }

    # Criar o diretório caso não exista
    os.makedirs("csvs", exist_ok=True)
    
    # Criação do DataFrame
    script_df = pd.DataFrame([data])
    
    # Definir o nome e o caminho do arquivo CSV
    file_name = "roteiro_detalhes.csv"
    file_path = os.path.join(os.getcwd(), "csvs", file_name)
    
    try:
        # Salvar o DataFrame em CSV
        script_df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Detalhes do roteiro salvos em: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
    
    return file_path

# Chamando a função
# caminho_csv = collect_script_details()
# print(f"Arquivo salvo no caminho: {caminho_csv}")