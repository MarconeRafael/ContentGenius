import csv
from keys import chave_openai  # Importando a chave da API de um arquivo externo

def gerar_entregaveis(detalhes, caminho_arquivo):
    # Garantir que o valor por criador é tratado como string
    valor_criador = str(detalhes.get("Valor por Criador")).replace('R$', '').replace(',', '.').strip()

    # Converter o valor para float depois de tratar como string
    valor_criador = float(valor_criador)

    # Definir as opções de conteúdo com base no valor por criador
    opcoes_conteudo = []

    if valor_criador >= 500:
        opcoes_conteudo.append(
            "1 vídeo destacando o tratamento completo Pele de Porcelana (40-60 segundos)"
        )
        opcoes_conteudo.append("1 Imagem de antes e depois (com boa resolução e iluminação)")
    
    if valor_criador >= 1000:
        opcoes_conteudo.append("1 Avaliação escrita no site da marca com foto - pele de porcelana")
    
    if valor_criador >= 1500:
        opcoes_conteudo.append(
            "1 vídeo completo sobre o processo de aplicação, com o criador explicando cada etapa"
        )
        opcoes_conteudo.append("2 Imagens de antes e depois (com boa resolução e iluminação)")
    
    # Escolher a opção de conteúdo mais adequada
    # Aqui estamos apenas selecionando a primeira opção que corresponde ao valor por criador
    opcao_escolhida = opcoes_conteudo[0] if opcoes_conteudo else "Nenhuma opção disponível"

    # Salvar no CSV
    try:
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Opção recomendada:"])
            writer.writerow([opcao_escolhida])
        print(f"Opção escolhida salva com sucesso em: {caminho_arquivo}")
        return caminho_arquivo
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
        return None
