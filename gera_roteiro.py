import openai
import pandas as pd
import os
from keys import chave_openai  # Importando a chave da API de um arquivo externo

openai.api_key = chave_openai

def criar_prompt_roteiro(detalhes):
    flag = detalhes.get("Flag").upper()
    if flag == "PT-BR":
        return f"""
        Você é um roteirista criativo especializado em marketing digital. Crie um roteiro detalhado e impactante para um vídeo promocional, baseado nos seguintes dados:

        **Briefing**: {detalhes.get('Briefing', 'Não informado')}
        **Nome do Creator**: {detalhes.get('Nome_do_Creator', 'Nome não informado')}
        **Tom de Voz**: {detalhes.get('Tom_de_Voz', 'Não informado')}
        **Formatos Preferidos pelo Creator**: {detalhes.get('Formatos_Preferidos_pelo_Creator', 'Não informado')}
        **Objetivo da Campanha**: {detalhes.get('Objetivo_da_Campanha', 'Não informado')}
        **Conversão Desejada**: {detalhes.get('Conversão_Desejada', 'Não informado')}
        **Canais de Divulgação**: {detalhes.get('Canais_de_Divulgação', 'Não informado')}
        **Estilo do Creator**: {detalhes.get('Estilo_do_Creator', 'Não informado')}

        **Estrutura do Roteiro (com orientações de tempo):**

        1. **Título (Até 5 segundos)**: Resuma a ideia principal do vídeo de forma impactante.
        2. **Cenário Inicial (Até 5 segundos)**: Comece com um gancho para capturar a atenção, como uma pergunta provocativa, cena impactante ou curiosidade.
        3. **Apresentação do Produto (Até 10 segundos)**: Apresente o produto ou serviço, destacando sua funcionalidade principal ou como resolve um problema.
        4. **Benefícios Destacados (Até 10 segundos)**: Enfatize os principais benefícios do produto/serviço de forma clara e objetiva.
        5. **Call-to-Action (Até 5 segundos)**: Dê uma instrução clara para conversão, como “Clique no link para saber mais” ou “Compre já!”.
        6. **Encerramento (Até 5 segundos)**: Finalize com uma mensagem inspiradora ou algo que reforça a conexão com o público.

        **Sugestões adicionais:**
        - Música de fundo, transições ou efeitos visuais alinhados ao estilo do creator.
        - Adapte o conteúdo às particularidades da plataforma e do público-alvo.
        """
    elif flag == "EN-US":
        return f"""
        You are a creative scriptwriter specialized in digital marketing. Create a detailed and impactful script for a promotional video based on the following information:

        **Briefing**: {detalhes.get('Briefing', 'Not informed')}
        **Creator's Name**: {detalhes.get('Nome_do_Creator', 'Name not informed')}
        **Tone of Voice**: {detalhes.get('Tom_de_Voz', 'Not informed')}
        **Preferred Formats by Creator**: {detalhes.get('Formatos_Preferidos_pelo_Creator', 'Not informed')}
        **Campaign Objective**: {detalhes.get('Objetivo_da_Campanha', 'Not informed')}
        **Desired Conversion**: {detalhes.get('Conversão_Desejada', 'Not informed')}
        **Dissemination Channels**: {detalhes.get('Canais_de_Divulgação', 'Not informed')}
        **Creator's Style**: {detalhes.get('Estilo_do_Creator', 'Not informed')}

        **Script Structure (with time guidelines):**

        1. **Title (Up to 5 seconds)**: Summarize the main idea of the video in an impactful way.
        2. **Initial Scene (Up to 5 seconds)**: Start with a hook to grab attention, such as a provocative question, impactful scene, or curiosity.
        3. **Product Presentation (Up to 10 seconds)**: Present the product or service, highlighting its main functionality or how it solves a problem.
        4. **Highlighted Benefits (Up to 10 seconds)**: Emphasize the main benefits of the product/service in a clear and objective way.
        5. **Call-to-Action (Up to 5 seconds)**: Provide a clear instruction for conversion, such as “Click the link to learn more” or “Buy now!”.
        6. **Closing (Up to 5 seconds)**: End with an inspiring message or something that reinforces the connection with the audience.

        **Additional Suggestions:**
        - Background music, transitions, or visual effects aligned with the creator's style.
        - Adapt the content to the particularities of the platform and the target audience.
        """

def gerar_roteiro(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return f"Arquivo não encontrado: {caminho_arquivo}"
    
    try:
        detalhes_df = pd.read_csv(caminho_arquivo)
        
        # Ajustando para as colunas corretas
        colunas_necessarias = [
            'Briefing', 'Nome do Creator', 'Tom de Voz', 'Formatos Preferidos pelo Creator',
            'Objetivo da Campanha', 'Conversão Desejada', 'Canais de Divulgação', 'Estilo do Creator', 'Flag'
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
