# MQTT Client Simulator - Projeto de Aprendizado


Um projeto simples para aprender os fundamentos de comunicação MQTT com Python, testando conexão e recebimento de mensagens.
Possio um publisher MQTT que simula dados de sensores agrícolas, especialmente focado em sensores de solo, para integração com sistemas IoT em agricultura de precisão.
##  Visão Geral

Este projeto implementa um cliente MQTT básico capaz de:
- Conectar-se a um broker MQTT
- Subscrever a tópicos específicos
- Receber e exibir mensagens
- Gerenciar eventos de conexão/desconexão


## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/isaackosmos/mqtt-station
   cd mqtt-station
   ```

2. Configure o ambiente:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .\.venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. Crie/copie o arquivo `.env` baseado no `.env.example`:
   ```bash
   cp .env.example .env
   ```

4. Edite o `.env` com suas configurações:
   ```ini
   BROKER_IP:localhost
   BROKER_PORT:1883
   CLIENT_NAME:mqtt_client
   KEEPALIVE:60
   TOPIC:/messages
   ```

## Como Usar

Execute o cliente MQTT:
```bash
python run.py
```

Execute o publisher (uma única publicação):

```bash
python publisher.py
```
### Funcionalidades Implementadas
- Conexão segura com broker MQTT
- Subscrição automática ao tópico configurado
- Log de eventos (conexão, mensagens recebidas)
- Tratamento básico de erros

## Estrutura do Projeto

```
mqtt-client-simulator/
├── application/
│   ├── __init__.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── main.py     # Loop principal do cliente MQTT
│   │   ├── mqtt_connection/
│   │   │    ├── __init__.py
│   │   │    ├── callbacks.py  # Callbacks para eventos MQTT
│   │   │    ├── mqtt_client.py  # Configurações do cliente MQTT
├── run.py              # Ponto de entrada do aplicativo
├── publisher.py        # Publicador de mensagens
└── .env.example        # Exemplo de arquivo de configuração
```

## Aprendizados

Este projeto aborda:
- Fundamentos do protocolo MQTT
- Conexão com brokers MQTT
- Gerenciamento de callbacks
- Tratamento de mensagens assíncronas
- Configuração via variáveis de ambiente
- Boas práticas de estrutura de projetos Python

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar issues
- Sugerir melhorias
- Enviar pull requests

## Licença

Este projeto está licenciado sob a licença MIT.