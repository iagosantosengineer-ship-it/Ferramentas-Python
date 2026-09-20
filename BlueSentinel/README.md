## Requisitos

- Python 3.10+
- Windows 10/11
# BlueSentinel

BlueSentinel é uma ferramenta leve de monitoramento de segurança para hosts Windows, desenvolvida com foco em aprendizado de Blue Team e experimentação em segurança defensiva.

A ferramenta realiza monitoramento contínuo da atividade do sistema e destaca comportamentos potencialmente suspeitos como conexões de rede incomuns, abuso de binários legítimos do Windows (LOLBins), mecanismos de persistência e indicadores básicos de threat intelligence.

Este projeto foi desenvolvido como ferramenta prática para entender como funcionam sistemas de monitoramento e detecção em endpoints dentro de ambientes de segurança defensiva.

---

# Funcionalidades

O BlueSentinel atualmente detecta diversos comportamentos associados a atividades maliciosas.

## Monitoramento de Rede
- Detecção de conexões de saída
- Identificação de IPs externos
- Monitoramento de comunicação suspeita

## Detecção de Command & Control (C2)

Detecta conexões para IPs externos iniciadas por processos que não estão na lista de confiança.

## Detecção de LOLBins

Identifica possível abuso de binários legítimos do Windows frequentemente utilizados por atacantes:

- powershell.exe
- cmd.exe
- mshta.exe
- rundll32.exe
- wscript.exe
- cscript.exe

Esses binários são conhecidos como **LOLBins (Living-off-the-Land Binaries)**.

## Monitoramento de Processos Suspeitos

Detecta execução de processos frequentemente utilizados em ataques ou cadeias de execução maliciosas.

## Detecção de Persistência

Verifica entradas no registro do Windows responsáveis por executar programas automaticamente no login do usuário.

Chaves monitoradas: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
Esse tipo de técnica é frequentemente usado por malware para garantir execução após reinicialização.


## Threat Intelligence Básica

Compara conexões de rede com domínios frequentemente utilizados em atividades maliciosas ou infraestrutura de ataque:

- ngrok
- duckdns
- no-ip
- pastebin
- discord
- raw.githubusercontent.com

## Detecção de Beaconing

Identifica padrões repetitivos de comunicação entre processos e IPs externos, comportamento comum em infraestrutura de Command & Control.

## Monitoramento em Tempo Real

A interface permite executar varreduras contínuas do sistema para identificar comportamentos suspeitos.

---

# Interface

O BlueSentinel possui uma interface gráfica simples que exibe eventos detectados em tempo real.

Os eventos são classificados por cores:

| Tipo de Evento | Cor |
|------|------|
Alerta C2 | Vermelho |
Processo Suspeito | Amarelo |
Persistência | Ciano |
Beaconing | Laranja |
LOLBin Detectado | Magenta |
Conexão de Rede | Branco |

---

# Instalação

Clone o repositório: git clone https://github.com/iagosantosengineer-ship-it/BlueSentinel.git

cd BlueSentinel

Crie um ambiente virtual: python -m venv venv

Ative o ambiente virtual:

Windows: .\venv\Scripts\activate or .\venv\Scripts\Activate.ps1

Instale as dependências: pip install -r requirements.txt

# Uso

Execute o programa com: python main.py


A interface gráfica será iniciada e permitirá:

- Executar um scan manual
- Iniciar monitoramento em tempo real
- Visualizar eventos detectados
- Limpar eventos exibidos

---

# Configuração

O BlueSentinel utiliza um arquivo de configuração para ajustar o comportamento das detecções.

Local do arquivo: config/config.json

Exemplo de configuração: 

 "ips_confiaveis": [
    "13.107.", ]

  "processos_confiaveis": [
    "msedge.exe", ]
  
  "processos_sistema": [
    "system", ]
  

---

# Estrutura do Projeto

BlueSentinel
│
├── config
│ └── config.json
│
├── detectors
│ ├── conexoes.py
│ ├── persistencia.py
│ ├── powershell.py
│ └── threatintel.py
│
├── utils
│ ├── config_loader.py
│ └── logger.py
│
├── interface.py
├── scanner.py
├── main.py
│
├── requirements.txt
└── README.md


---

# Fluxo do Motor de Detecção

O mecanismo de detecção funciona da seguinte forma:

1. Coleta conexões de rede ativas no sistema
2. Identifica processos suspeitos em execução
3. Detecta possível abuso de LOLBins
4. Verifica mecanismos de persistência no registro
5. Identifica possíveis conexões de Command & Control
6. Aplica verificações de threat intelligence

---

# Objetivo Educacional

Esta ferramenta foi desenvolvida para:

- aprendizado em Blue Team
- experimentação em segurança defensiva
- estudo de monitoramento de endpoints
- prática de lógica de detecção

Ela **não substitui soluções profissionais de segurança**.

---

# Melhorias Futuras

Algumas melhorias planejadas para versões futuras incluem:

- painel de telemetria do sistema
- filtragem de eventos
- exportação de relatórios
- inspeção de processos
- integração com APIs de threat intelligence
- melhorias em detecção comportamental

---

# Autor

Iago dos Santos




