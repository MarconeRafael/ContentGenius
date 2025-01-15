

# Roteiro Generator

## Descrição do Projeto

O **Roteiro Generator** é uma ferramenta simples e eficaz para criar roteiros detalhados de vídeos promocionais com base em dados fornecidos pelo usuário. Ele utiliza a API da OpenAI para gerar textos criativos e bem estruturados, ideais para campanhas de marketing digital. O projeto suporta a coleta de dados, a criação de roteiros e o armazenamento dos resultados em arquivos CSV.

---

## Funcionalidades

- **Coleta de dados**: Interface interativa para inserir os detalhes do roteiro.
- **Geração de roteiros**: Utiliza a API da OpenAI para criar roteiros criativos e impactantes.
- **Exportação em CSV**: Armazena os roteiros gerados junto com os dados fornecidos em um arquivo CSV.

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas**: Manipulação de dados em formato tabular.
- **OpenAI API**: Geração de roteiros criativos.
- **Biblioteca OS**: Manipulação de arquivos e diretórios.

---

## Estrutura do Projeto

```
.
├── coleta_roteiro.py        # Função para coletar os detalhes do roteiro
├── gera_roteiro.py          # Função para gerar roteiros utilizando a API da OpenAI
├── main_roteiro.py          # Arquivo principal para integração do fluxo
├── requirements.txt         # Dependências do projeto
├── keys.py                  # Arquivo para armazenar a chave da API da OpenAI
├── csvs/                    # Diretório para armazenar os arquivos CSV gerados
├── README.md                # Documentação do projeto
```

---

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- Python 3.10+
- Conta na [OpenAI](https://openai.com/) com acesso à API
- Chave da API da OpenAI

---

## Como Configurar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/roteiro-generator.git
   cd roteiro-generator
   ```

2. **Configure sua chave da API**:
   - Crie um arquivo `keys.py` na raiz do projeto com o seguinte conteúdo:
     ```python
     chave_openai = "sua-chave-da-api"
     ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Como Usar

1. **Execute o arquivo principal**:
   ```bash
   python main_roteiro.py
   ```

2. **Preencha as informações solicitadas**:
   - Insira os detalhes do roteiro conforme solicitado no terminal.

3. **Verifique o arquivo gerado**:
   - Os dados coletados e os roteiros gerados serão salvos no diretório `csvs`.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Contato

- **Autor**: [Wendel Luan](https://www.linkedin.com/in/wendelluan/)
- **Email**: wendelluan@example.com
```


