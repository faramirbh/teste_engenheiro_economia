# Teste Técnico - Engenheiro de Dados Senior - Indra Group

## 📋 Descrição do Projeto

Pipeline completo de processamento de Notas Fiscais Eletrônicas (NF-e) utilizando:

- **Apache Spark** para processamento de dados
- **Apache Kafka** para streaming de mensagens
- **Apache Airflow** para orquestração
- **Docker Compose** para infraestrutura

---

## 🏗️ Arquitetura

\\\
XMLs (100 arquivos)
        │
        ▼
DAG 1: Spark XML → JSON → Kafka
        │
        ▼
Kafka (Tópico: nfe-events)
        │
        ▼
DAG 2: Spark Kafka → Hive
        │
        ▼
Hive (Tabela: nfe_events)
        │
        ▼
Consultas SQL Analíticas
\\\

---

## 📁 Estrutura do Projeto

\\\
teste_engenheiro_economia/
├── docker/
│   ├── docker-compose.yml
│   └── scripts/
│       ├── spark_xml_to_kafka.py
│       └── spark_kafka_to_hive.py
├── airflow/
│   └── dags/
│       ├── dag1_xml_to_kafka.py
│       └── dag2_kafka_to_hive.py
├── queries/
│   └── analytics.sql
├── evidencias/
│   ├── dag1_sucesso.png
│   ├── dag2_sucesso.png
│   └── dags_ativas.png
├── xmls/ (100 arquivos NF-e)
└── README.md
\\\

---

## 🚀 Como Executar

### Pré-requisitos
- Windows 10/11
- Docker Desktop
- Git
- PowerShell

### Passos

1. **Clonar repositório**
\\\powershell
git clone https://github.com/faramirbh/teste_engenheiro_economia.git
cd teste_engenheiro_economia
\\\

2. **Iniciar infraestrutura**
\\\powershell
cd docker
docker compose up -d
\\\

3. **Acessar Airflow**
\\\
http://localhost:8888
Usuário: admin
Senha: admin
\\\

4. **Executar DAGs**
   - Ativar toggle de dag1_xml_to_kafka (azul)
   - Clique no play (▶️)
   - Aguarde ficar VERDE
   - Repita para dag2_kafka_to_hive

---

## 📊 Resultados

| Métrica | Valor |
|---------|-------|
| NFes Processadas | 100 |
| Valor Total | R$ 9.553,23 |
| DAG 1 Status | ✅ SUCESSO |
| DAG 2 Status | ✅ SUCESSO |
| Tempo Total | ~50 segundos |

---

## 🔍 Consultas SQL

O arquivo \queries/analytics.sql\ contém:

1. Contagem total de NFes
2. Análise de valores (soma, média, mín, máx)
3. Top 10 emitentes
4. Análise por data de emissão
5. Top 10 destinatários
6. Distribuição por faixas de valor
7. Resumo executivo com KPIs

---

## 🛠️ Tecnologias

- Docker 29.3.1
- Apache Spark 3.x
- Apache Kafka 5.5.0
- Apache Airflow 2.8.0
- PostgreSQL 13
- Python 3.9+
- Zookeeper 5.5.0

---

## 👨‍💻 Autor

**Henrique Augusto Manger**
henriquemanger@gmail.com
Abril de 2026
