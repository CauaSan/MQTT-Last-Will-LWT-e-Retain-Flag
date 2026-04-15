# 📘 MQTT – Last Will (LWT) e Retain Flag

## 🎯 Objetivo

Este projeto demonstra na prática o funcionamento de:

* Last Will and Testament (LWT)
* Retain Flag
* QoS + Sessão Persistente

Além disso, apresenta:

* Quando usar cada recurso
* Impactos em sistemas IoT reais

---

## 🧠 Conceitos

### 🔥 Last Will and Testament (LWT)

O LWT é uma mensagem configurada no cliente MQTT que será enviada automaticamente pelo broker caso o cliente se desconecte de forma inesperada.

📌 Quando usar:

* Monitoramento de dispositivos IoT
* Detecção de falhas
* Sistemas críticos

📊 Impactos:

* Permite identificar dispositivos offline automaticamente
* Aumenta a confiabilidade do sistema

---

### 📌 Retain Flag

O Retain Flag faz com que o broker armazene a última mensagem publicada em um tópico.

📌 Quando usar:

* Manter estado atual (ON/OFF)
* Último valor de sensores

📊 Impactos:

* Novos clientes recebem o estado imediatamente
* Evita perda de contexto

⚠️ Limitação:

* Armazena apenas a última mensagem

---

### 📡 QoS + Sessão Persistente

Para armazenar múltiplas mensagens, utilizamos:

* QoS 1 (garantia de entrega)
* Sessão persistente (`clean_session=False`)

📌 Resultado:

* O subscriber recebe mensagens enviadas enquanto estava offline

---

## ⚖️ Diferença entre LWT e Retain

| Recurso | Função                    |
| ------- | ------------------------- |
| LWT     | Detectar falha/desconexão |
| Retain  | Guardar último estado     |

---

## 🧪 Tecnologias utilizadas

* Python
* Biblioteca `paho-mqtt`
* Broker público: HiveMQ

---

## 📂 Estrutura do projeto

```
mqtt-projeto/
│
├── publisher.py
├── subscriber.py
└── requirements.txt
```

---

## 🚀 Como executar

### 1. Instalar dependência

```bash
pip install paho-mqtt
```

---

### 2. Rodar o subscriber

```bash
python subscriber.py
```

---

### 3. Rodar o publisher

```bash
python publisher.py
```

---

## 🧪 Testes realizados

### ✅ Teste 1 – Comunicação básica

* Publisher envia mensagens
* Subscriber recebe em tempo real

---

### ✅ Teste 2 – LWT (detecção de falha)

* Publisher foi encerrado de forma abrupta
* Subscriber recebeu:

```
OFFLINE
```

✔ Resultado: LWT funcionando corretamente

---

### ✅ Teste 3 – Retain

* Subscriber reconectado
* Recebeu o último estado automaticamente

✔ Resultado: Retain funcionando

---

### ✅ Teste 4 – Histórico de mensagens

* Subscriber desconectado
* Publisher continuou enviando dados
* Subscriber reconectado

✔ Resultado:

* Todas as mensagens foram recebidas (QoS + sessão persistente)

---

## 💡 Conclusão

* O LWT é essencial para detectar falhas em dispositivos IoT
* O Retain garante o estado atual do sistema
* O uso de QoS com sessão persistente permite armazenamento de mensagens

👉 Em conjunto, esses recursos aumentam a confiabilidade e eficiência de sistemas IoT reais
