# Teste Técnico - Engenheiro de Dados Senior - Indra Group

## 📋 Descrição do Projeto

Este projeto implementa uma **arquitetura completa de Big Data** para processamento de Notas Fiscais Eletrônicas (NF-e) utilizando:

- **Apache Spark** para processamento de dados
- **Apache Kafka** para streaming de mensagens
- **Apache Airflow** para orquestração de pipelines
- **Apache Hive** para armazenamento e análise
- **Docker Compose** para containerização da infraestrutura

---

## 🏗️ Arquitetura

\\\
┌─────────────────┐
│   XMLs NF-e     │  (100 arquivos)
│  (pasta xmls/)  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  DAG 1 - Airflow            │
│  spark_xml_to_kafka.py      │
│  (Lê XMLs → JSON → Kafka)   │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────┐
│  Apache Kafka   │  (Tópico: nfe-events)
│  (Streaming)    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  DAG 2 - Airflow            │
│  spark_kafka_to_hive.py     │
│  (Consome Kafka → Persiste) │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────┐
│  Apache Hive    │  (Tabela: nfe_events)
│  (Warehouse)    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  Consultas SQL Analíticas   │
│  (queries/analytics.sql)    │
└─────────────────────────────┘
\\\

---

## 📁 Estrutura do Projeto

\\\
teste_engenheiro_economia/
├── docker/
│   ├── docker-compose.yml          ✅ Infraestrutura
│   └── scripts/
│       ├── spark_xml_to_kafka.py   ✅ Script Spark 1
│       └── spark_kafka_to_hive.py  ✅ Script Spark 2
├── airflow/
│   └── dags/
│       ├── dag1_xml_to_kafka.py    ✅ DAG 1 Airflow
│       └── dag2_kafka_to_hive.py   ✅ DAG 2 Airflow
├── queries/
│   └── analytics.sql               ✅ Consultas SQL
├── evidencias/
│   ├── dag1_sucesso.png           ✅ Print DAG 1
│   ├── dag2_sucesso.png           ✅ Print DAG 2
│   └── dags_ativas.png            ✅ Print DAGs Ativas
├── xmls/
│   ├── nfe_001.xml
│   ├── nfe_002.xml
│   └── ... (100 arquivos)
├── README.md                       ✅ Este arquivo
└── .gitignore
\\\

---

## 🚀 Como Executar

### **Pré-requisitos**

- Windows 10/11
- Docker Desktop instalado e rodando
- Git
- PowerShell

### **Passo 1: Clonar o Repositório**

\\\powershell
git clone https://github.com/faramirbh/teste_engenheiro_economia.git
cd teste_engenheiro_economia
\\\

### **Passo 2: Iniciar a Infraestrutura**

\\\powershell
cd docker
docker compose up -d
\\\

Aguarde 2-3 minutos para todos os containers iniciarem.

### **Passo 3: Acessar o Airflow**

Abra o navegador e vá para:

\\\
http://localhost:8888
\\\

**Credenciais:**
- Usuário: dmin
- Senha: dmin

### **Passo 4: Executar as DAGs**

1. **Ativar DAG 1**: Clique no toggle de dag1_xml_to_kafka (deve ficar azul)
2. **Disparar DAG 1**: Clique no botão play (▶️) em "Actions"
3. **Aguardar conclusão**: Veja o Grid ficar VERDE
4. **Ativar DAG 2**: Clique no toggle de dag2_kafka_to_hive
5. **Disparar DAG 2**: Clique no botão play
6. **Aguardar conclusão**: Veja o Grid ficar VERDE

---

## 📊 Resultados Obtidos

### **DAG 1 - XML → Kafka**
- ✅ **Status**: SUCESSO
- 📊 **Arquivos Processados**: 100 XMLs
- ⏱️ **Tempo de Execução**: ~24 segundos
- 📤 **Mensagens Enviadas ao Kafka**: 100 NFes

### **DAG 2 - Kafka → Hive**
- ✅ **Status**: SUCESSO
- 📊 **Registros Consumidos**: 100 NFes
- ⏱️ **Tempo de Execução**: ~24 segundos
- 💾 **Dados Persistidos**: Tabela 
fe_events criada

### **Análise dos Dados**

A tabela 
fe_events contém:
- **Total de NFes**: 100
- **Valor Total**: R$ 9.553,23
- **Valor Médio**: R$ 95,53
- **Emitentes**: Diversos supermercados e mercadinhos
- **Período**: 2019-2026

---

## 🔍 Consultas SQL Incluídas

O arquivo queries/analytics.sql contém 7 consultas analíticas:

1. **Contagem Total de NFes**: Número total de documentos processados
2. **Análise de Valores**: Soma, média, mín e máx dos valores
3. **Top 10 Emitentes**: Emitentes com maior volume de vendas
4. **Análise por Data**: NFes agrupadas por data de emissão
5. **Top 10 Destinatários**: Destinatários que mais receberam NFes
6. **Distribuição por Range**: Agrupamento de valores em faixas
7. **Resumo Executivo**: KPIs principais consolidados

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Função |
|-----------|--------|--------|
| Docker | 29.3.1 | Containerização |
| Apache Spark | 3.x | Processamento distribuído |
| Apache Kafka | 5.5.0 | Streaming de mensagens |
| Apache Airflow | 2.8.0 | Orquestração de workflows |
| PostgreSQL | 13 | Banco de dados do Airflow |
| Python | 3.9+ | Linguagem de programação |
| Zookeeper | 5.5.0 | Coordenação do Kafka |

---

## 📈 Performance

- **XML → JSON (Spark)**: ~24 segundos para 100 arquivos
- **Kafka Publishing**: Imediato (~100 mensagens/segundo)
- **Kafka → Hive (Spark)**: ~24 segundos para 100 registros
- **Pipeline Completo**: ~50 segundos end-to-end

---

## 📋 Checklist de Entrega

- ✅ Infraestrutura Docker com todos os serviços
- ✅ Script Spark 1: XML → Kafka (100 NFes processadas)
- ✅ Script Spark 2: Kafka → Hive (100 NFes persistidas)
- ✅ DAG 1 Airflow: Orquestração do pipeline XML-Kafka
- ✅ DAG 2 Airflow: Orquestração do pipeline Kafka-Hive
- ✅ Consultas SQL analíticas no Hive
- ✅ Evidências de execução (prints/logs)
- ✅ Repositório Git com histórico completo
- ✅ README documentação

---

## 📧 Instruções de Entrega

Enviar para: **wsmarques@minsait.com**

**Conteúdo do Email:**
1. Link do repositório GitHub forkado
2. Currículo (PDF)
3. Breve descrição da solução implementada

**Repositório:** https://github.com/faramirbh/teste_engenheiro_economia

---

## 👨‍💻 Desenvolvedor

- **Nome**: Henrique Augusto Manger
- **Email**: henriquemanger@gmail.com
- **Data**: Abril de 2026

---

## 📞 Suporte

Para dúvidas sobre a solução, entre em contato através do email acima.

---

## 📜 Licença

Este projeto foi desenvolvido como solução para o processo seletivo da Indra Group.

---

## 🙏 Agradecimentos

Agradeço à Indra Group pela oportunidade de demonstrar conhecimento em arquitetura de dados e Big Data.
