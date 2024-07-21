
# Telegram Message Monitor

![Telegram Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Telegram_2019_Logo.svg/640px-Telegram_2019_Logo.svg.png) <!-- Adicione um link para um logo, se disponível -->

## Descrição

O **Telegram Message Monitor** é um projeto em Python que utiliza a biblioteca [Pyrogram](https://docs.pyrogram.org/) para monitorar mensagens em grupos e canais do Telegram. Este bot pode ser configurado para realizar ações automáticas baseadas em mensagens recebidas, facilitando a interação e coleta de informações.

### Funcionalidades

- **Monitoramento de Mensagens**: Escuta mensagens em tempo real em grupos e canais do Telegram.
- **Respostas Automáticas**: Responde automaticamente a mensagens específicas.
- **Filtragem de Mensagens**: Possibilidade de filtrar mensagens com base em palavras-chave ou padrões.
- **Interface Simples**: Fácil de configurar e usar.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Pyrogram**: Biblioteca para interação com a API do Telegram.
- **dotenv**: Para gerenciar variáveis de ambiente.

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- [Pip](https://pip.pypa.io/en/stable/) (gerenciador de pacotes do Python)

### Passos para Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu_usuario/telegram-message-monitor.git
   cd telegram-message-monitor
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip3 install -r requirements.txt
   ```

4. **Configure as credenciais do Telegram**:
   - Crie um arquivo `.env` no diretório raiz do projeto e adicione suas credenciais do Telegram:

   ```plaintext
   API_ID=seu_api_id
   API_HASH=seu_api_hash
   SESSION_NAME=nome_da_sessao
   ```

## Uso

### Executando o Monitor

Para iniciar o monitor, use o seguinte comando:

```bash
python main.py
```

O monitor começará a escutar mensagens nos grupos e canais que você configurou.

### Exemplo de Uso

Para monitorar mensagens, você pode configurar seu bot para escutar um grupo específico e responder a mensagens que contêm uma palavra-chave.

```python
from pyrogram import Client, filters

app = Client("my_bot")

@app.on_message(filters.text & filters.group)
def monitor_messages(client, message):
    if "palavra-chave" in message.text.lower():
        client.send_message(chat_id=message.chat.id, text="Resposta automática!")

app.run()
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato:

- **Celso Vasconcelos**: [contato.celso.vasconcelos@gmail.com](mailto:contato.celso.vasconcelos@gmail.com)
- **GitHub**: [celsolnv](https://github.com/celsolnv)

---

Agradecemos por usar o **Telegram Message Monitor**!
```

### Personalizações

- **Logo**: Se você tiver um logo ou imagem representativa do seu projeto, adicione o link na seção de descrição.
- **Links e Contato**: Atualize os links e informações de contato com seus dados reais.
- **Documentação**: Se houver mais detalhes sobre a configuração ou uso do seu projeto, considere adicionar essas informações.

Se precisar de mais ajustes ou informações, fique à vontade para pedir!