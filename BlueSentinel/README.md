# 🛡️ BlueSentinel

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-0078D6?logo=windows)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

**BlueSentinel** é uma ferramenta leve de monitoramento de segurança para hosts Windows, desenvolvida com foco em aprendizado de **Blue Team** e experimentação em segurança defensiva.

Realiza monitoramento contínuo da atividade do sistema e destaca comportamentos potencialmente suspeitos: conexões de rede incomuns, abuso de binários legítimos do Windows (LOLBins), mecanismos de persistência e indicadores básicos de threat intelligence.

Projeto desenvolvido como ferramenta prática para entender como funcionam sistemas de monitoramento e detecção em endpoints (EDR-like) dentro de ambientes de segurança defensiva.

---

## 📑 Sumário

- [Funcionalidades](#-funcionalidades)
- [Mapeamento MITRE ATT&CK](#-mapeamento-mitre-attck)
- [Interface](#-interface)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Configuração](#-configuração)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Fluxo do Motor de Detecção](#-fluxo-do-motor-de-detecção)
- [Objetivo Educacional](#-objetivo-educacional)
- [Melhorias Futuras](#-melhorias-futuras)
- [Autor](#-autor)

---

## ⚙️ Funcionalidades

### 🌐 Monitoramento de Rede
- Detecção de conexões de saída
- Identificação de IPs externos
- Monitoramento de comunicação suspeita

### 🎯 Detecção de Command & Control (C2)
Detecta conexões para IPs externos iniciadas por processos que não estão na lista de confiança.

### 🧩 Detecção de LOLBins
Identifica possível abuso de binários legítimos do Windows frequentemente utilizados por atacantes:
`powershell.exe` · `cmd.exe` · `mshta.exe` · `rundll32.exe` · `wscript.exe` · `cscript.exe`

Esses binários são conhecidos como **LOLBins (Living-off-the-Land Binaries)**.

### 🔎 Monitoramento de Processos Suspeitos
Detecta execução de processos frequentemente utilizados em ataques ou cadeias de execução maliciosas.

### 🔐 Detecção de Persistência
Verifica entradas no registro do Windows responsáveis por executar programas automaticamente no login do usuário.

Chave monitorada: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

### 🕵️ Threat Intelligence Básica
Compara conexões de rede com domínios frequentemente utilizados em atividades maliciosas ou infraestrutura de ataque:
`ngrok` · `duckdns` · `no-ip` · `pastebin` · `discord` · `raw.githubusercontent.com`

### 📡 Detecção de Beaconing
Identifica padrões repetitivos de comunicação entre processos e IPs externos, comportamento comum em infraestrutura de C2.

### ⏱️ Monitoramento em Tempo Real
A interface permite executar varreduras contínuas do sistema para identificar comportamentos suspeitos.

---

## 🗺️ Mapeamento MITRE ATT&CK

| Detecção | Técnica MITRE ATT&CK |
|---|---|
| Command & Control | T1071 – Application Layer Protocol |
| LOLBins | T1218 – System Binary Proxy Execution |
| Persistência (Registry Run Keys) | T1547.001 – Boot or Logon Autostart Execution |
| Beaconing | T1071 / T1102 – C2 Beaconing Behavior |
| Threat Intelligence (domínios) | T1583 / T1584 – Acquire Infrastructure |

---

## 🖥️ Interface

Interface gráfica simples que exibe eventos detectados em tempo real, classificados por cor:

| Tipo de Evento | Cor |
|---|---|
| Alerta C2 | 🔴 Vermelho |
| Processo Suspeito | 🟡 Amarelo |
| Persistência | 🔵 Ciano |
| Beaconing | 🟠 Laranja |
| LOLBin Detectado | 🟣 Magenta |
| Conexão de Rede | ⚪ Branco |

---

## 📦 Instalação

**Requisitos:** Python 3.10+ · Windows 10/11

```bash
git clone https://github.com/iagosantosengineer-ship-it/BlueSentinel.git
cd BlueSentinel

python -m venv venv

# Windows
.\venv\Scripts\activate
# ou (PowerShell)
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

---

## 🚀 Uso

```bash
python main.py
```

A interface gráfica será iniciada e permitirá:
- Executar um scan manual
- Iniciar monitoramento em tempo real
- Visualizar eventos detectados
- Limpar eventos exibidos

---

## 🔧 Configuração

Arquivo de configuração: `config/config.json`

```json
{
  "ips_confiaveis": ["13.107."],
  "processos_confiaveis": ["msedge.exe"],
  "processos_sistema": ["system"]
}
```

---

## 🏗️ Estrutura do Projeto

```bash
BlueSentinel/
│
├── config/
│   └── config.json
│
├── detectors/
│   ├── conexoes.py
│   ├── persistencia.py
│   ├── powershell.py
│   └── threatintel.py
│
├── utils/
│   ├── config_loader.py
│   └── logger.py
│
├── interface.py
├── scanner.py
├── main.py
│
├── requirements.txt
└── README.md
```

---

## 🔄 Fluxo do Motor de Detecção

1. Coleta conexões de rede ativas no sistema
2. Identifica processos suspeitos em execução
3. Detecta possível abuso de LOLBins
4. Verifica mecanismos de persistência no registro
5. Identifica possíveis conexões de Command & Control
6. Aplica verificações de threat intelligence

---

## 🎓 Objetivo Educacional

Esta ferramenta foi desenvolvida para:
- aprendizado em Blue Team
- experimentação em segurança defensiva
- estudo de monitoramento de endpoints
- prática de lógica de detecção

> ⚠️ Ela **não substitui soluções profissionais de segurança**.

---

## 🗂️ Melhorias Futuras

- [ ] Painel de telemetria do sistema
- [ ] Filtragem de eventos
- [ ] Exportação de relatórios (PDF/HTML)
- [ ] Inspeção de processos
- [ ] Integração com APIs de threat intelligence (AbuseIPDB, VirusTotal)
- [ ] Melhorias em detecção comportamental
- [ ] Integração com o `ip-threat-analyzer` (enriquecimento automático de IPs suspeitos)

---

## 👨‍💻 Autor

**Iago dos Santos**

Projeto desenvolvido com foco em **Blue Team / SOC Analyst**.
