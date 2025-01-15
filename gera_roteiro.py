import openai
import pandas as pd
import os
from keys import chave_openai  # Importando a chave da API de um arquivo externo

openai.api_key = chave_openai

def criar_prompt_roteiro(detalhes):
    return f"""
    Você é um roteirista criativo especializado em marketing digital. Crie um roteiro detalhado e impactante para um vídeo promocional, baseado nos seguintes dados:

    Objetivo Principal: {detalhes.get('Objetivo Principal', 'Não informado')}
    Ação Esperada do Público: {detalhes.get('Ação Esperada do Público', 'Não informado')}
    Público-Alvo: {detalhes.get('Público-Alvo', 'Não informado')}
    Problemas/Aspirações: {detalhes.get('Problemas/Aspirações', 'Não informado')}
    Como Consomem Conteúdo: {detalhes.get('Como Consomem Conteúdo', 'Não informado')}
    Estilo de Comunicação: {detalhes.get('Estilo de Comunicação', 'Não informado')}
    Referência de Tom/Estilo: {detalhes.get('Referência de Tom/Estilo', 'Não informado')}
    Plataforma: {detalhes.get('Plataforma', 'Não informado')}
    Formato de Publicação: {detalhes.get('Formato de Publicação', 'Não informado')}
    Produto Promovido: {detalhes.get('Produto Promovido', 'Não informado')}
    Benefícios/Diferenciais: {detalhes.get('Benefícios/Diferenciais', 'Não informado')}
    Detalhes Técnicos: {detalhes.get('Detalhes Técnicos', 'Não informado')}
    CTA Esperado: {detalhes.get('CTA Esperado', 'Não informado')}
    Materiais Visuais Disponíveis: {detalhes.get('Materiais Visuais Disponíveis', 'Não informado')}
    Elementos Criativos: {detalhes.get('Elementos Criativos', 'Não informado')}
    Prazo: {detalhes.get('Prazo', 'Não informado')}
    Frequência de Publicação: {detalhes.get('Frequência de Publicação', 'Não informado')}
    Métricas Esperadas: {detalhes.get('Métricas Esperadas', 'Não informado')}
    
    Estruture o roteiro com os seguintes elementos:
    - Título
    - Cenário inicial (até 5 segundos)
    - Apresentação do produto (até 10 segundos)
    - Benefícios destacados (até 10 segundos)
    - Call-to-Action (até 5 segundos)
    - Encerramento (até 5 segundos)
    """

def gerar_roteiro(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return f"Arquivo não encontrado: {caminho_arquivo}"
    
    try:
        detalhes_df = pd.read_csv(caminho_arquivo)
        
        # Validar se colunas essenciais existem
        colunas_necessarias = [
            'Objetivo Principal', 'Ação Esperada do Público', 'Público-Alvo',
            'Problemas/Aspirações', 'Como Consomem Conteúdo', 'Estilo de Comunicação',
            'Referência de Tom/Estilo', 'Plataforma', 'Formato de Publicação',
            'Produto Promovido', 'Benefícios/Diferenciais', 'Detalhes Técnicos',
            'CTA Esperado', 'Materiais Visuais Disponíveis', 'Elementos Criativos',
            'Prazo', 'Frequência de Publicação', 'Métricas Esperadas'
        ]
        for coluna in colunas_necessarias:
            if coluna not in detalhes_df.columns:
                return f"Coluna ausente no CSV: {coluna}"
        
        roteiros = []

        for _, detalhes in detalhes_df.iterrows():
            prompt = criar_prompt_roteiro(detalhes)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um roteirista criativo especializado em vídeos promocionais."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.8
            )
            roteiro = response['choices'][0]['message']['content'].strip()
            roteiros.append(roteiro)

        detalhes_df['Roteiro'] = roteiros
        
        # Salvar o arquivo com os roteiros gerados
        caminho_saida = caminho_arquivo.replace('.csv', '_roteiros.csv')
        detalhes_df.to_csv(caminho_saida, index=False, encoding='utf-8')
        return f"Roteiros salvos em: {caminho_saida}"

    except openai.error.OpenAIError as e:
        return f"Erro na API OpenAI: {e}"
    except Exception as e:
        return f"Erro ao gerar roteiros: {e}"

# Chamando a função (descomente para uso)
# caminho_csv = 'csvs/roteiro_detalhes.csv'  # Substitua pelo caminho do seu arquivo CSV
# print(gerar_roteiro(caminho_csv))