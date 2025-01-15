def coletar_dados_entregaveis():
    print("Preencha as informações detalhadas do entregável estratégico e personalizado para o creator:\n")

    # Coletar as informações de entrada com os campos solicitados
    data = {
        "Briefing da Campanha": input(
            "Briefing da campanha (exemplo: 'Fortalecer a presença da marca no mercado fitness com foco em conteúdo educativo sobre nossos suplementos'): "
        ).strip(),
        "Valores ou Missão da Marca": input(
            "Valores ou missão da marca (exemplo: 'Promover um estilo de vida saudável e sustentável'): "
        ).strip(),
        "Diferenciais Competitivos da Marca": input(
            "Diferenciais competitivos da marca (exemplo: 'Produtos com ingredientes 100% naturais, embalagens recicláveis'): "
        ).strip(),
        "Canais de Divulgação": input(
            "Canais de divulgação (exemplo: 'Instagram Reels, TikTok'): "
        ).strip(),
        "Valor por Criador": input(
            "Valor por criador (exemplo: 'R$ 500,00'): "
        ).strip(),
        "Flag": input(
            "Flag (exemplo: 'PT-BR, EN-US'): "
        ).strip(),
    }
    
    return data  # Retornar o dicionário com os dados coletados
