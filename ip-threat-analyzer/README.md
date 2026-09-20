# 🔍 Hybrid IP Threat Checker

Uma ferramenta de **Blue Team** desenvolvida em Python para análise e classificação de endereços IP utilizando **Threat Intelligence + heurísticas locais**.

---

## 🧠 Objetivo

Este projeto simula um fluxo real de análise em ambientes SOC, permitindo:

* Enriquecimento de IP (hostname / DNS reverso)
* Verificação contra feeds de Threat Intelligence
* Classificação baseada em score
* Geração de logs estruturados (NDJSON)

---

## ⚙️ Funcionalidades

* 🔍 **Input manual de IP via CLI**
* 🌐 **Enrichment com reverse DNS**
* 🚫 **Detecção via blacklist (Feodo Tracker)**
* 🧠 **Heurística para identificação de comportamento suspeito (ex: TOR)**
* 📊 **Sistema de score e classificação (BENIGN / SUSPICIOUS / MALICIOUS)**
* 🧾 **Output em JSON formatado**
* 📁 **Logs em formato NDJSON (compatível com SIEM)**

---

## 🏗️ Arquitetura

```bash
ip_checker/
│
├── main.py
├── blacklist.txt
│
├── core/
│   ├── enrichment.py
│   ├── detection.py
│   └── scoring.py
│
├── utils/
│   └── logger.py
```

---

## 🚀 Como usar

### 1. Clonar o repositório

```bash
git clone  https://github.com/iagosantosengineer-ship-it/ip-threat-analyzer.git
cd ip-threat-analyzer
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Executar

```bash
python main.py
```

---

## 📸 Exemplo de uso

### 🔴 IP suspeito (TOR)

```text
IP: 185.220.101.1
Hostname: berlin01.tor-exit.artikel10.org
Blacklist: NAO
Score: 50
Classificação: SUSPICIOUS
Motivo: Tor exit node detected (anonymization network)
```

---

### 🟢 IP benigno

```text
IP: 8.8.8.8
Hostname: dns.google
Blacklist: NAO
Score: 0
Classificação: BENIGN
Motivo: No indicators of compromise detected
```

---

## 📊 Exemplo JSON (output)

```json
{
    "ip": "185.220.101.1",
    "hostname": "berlin01.tor-exit.artikel10.org",
    "blacklisted": false,
    "score": 50,
    "classification": "SUSPICIOUS",
    "reason": "Tor exit node detected (anonymization network)",
    "timestamp": "2026-03-21 10:58:11"
}
```

---

## 📁 Logs (NDJSON)

Os eventos são armazenados em formato **NDJSON (Newline Delimited JSON)**:

```json
{"ip":"185.220.101.1","score":50,"classification":"SUSPICIOUS"}
{"ip":"8.8.8.8","score":0,"classification":"BENIGN"}
```

Esse formato é amplamente utilizado em:

* SIEM (Splunk, ELK)
* pipelines de segurança
* ingestão de logs em larga escala

---

## 🧠 Lógica de detecção

O score é baseado em:

* Presença em blacklist (Threat Intelligence)
* Ausência de hostname (indicador fraco)
* Identificação de rede TOR (alto risco)

---

## 🔒 Observações

* Nem todo IP malicioso está em blacklist
* Heurísticas complementam Threat Intelligence
* A ferramenta simula um pipeline real de análise SOC

---

## 📌 Próximos passos (roadmap)

* [ ] Suporte a múltiplos IPs
* [ ] Integração com logs do Windows (eventos 5156)
* [ ] Integração com o projeto BlueSentinel
* [ ] Múltiplos feeds de Threat Intelligence

---

## 👨‍💻 Autor 
Iago Dos Santos

Projeto desenvolvido com foco em **Blue Team / SOC Analyst**.

---

## ⭐ Contribuição

Sinta-se à vontade para contribuir ou sugerir melhorias.
