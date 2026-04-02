from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Analytics") \
    .enableHiveSupport() \
    .getOrCreate()

# Criar tabela de teste (simulando dados do nfe_events)
spark.sql('''
    CREATE TABLE IF NOT EXISTS nfe_events (
        emitente_nome STRING,
        emitente_cnpj STRING,
        destinatario_nome STRING,
        data_emissao TIMESTAMP,
        numero_nf INT,
        valor_total DOUBLE
    )
''')

# Query 1: Total de NFes
print("\\n=== TOTAL DE NFES ===")
spark.sql("SELECT COUNT(*) as total_nfes FROM nfe_events").show()

# Query 2: Análise de Valores
print("\\n=== ANÁLISE DE VALORES ===")
spark.sql('''
    SELECT 
        SUM(valor_total) as valor_total,
        COUNT(*) as quantidade,
        AVG(valor_total) as valor_medio,
        MIN(valor_total) as valor_minimo,
        MAX(valor_total) as valor_maximo
    FROM nfe_events
''').show()

# Query 3: Análise por Emitente
print("\\n=== TOP EMITENTES ===")
spark.sql('''
    SELECT 
        emitente_nome,
        COUNT(*) as quantidade_nfes,
        SUM(valor_total) as valor_total
    FROM nfe_events
    GROUP BY emitente_nome
    ORDER BY valor_total DESC
    LIMIT 10
''').show()

# Query 4: Resumo Executivo
print("\\n=== RESUMO EXECUTIVO ===")
spark.sql('''
    SELECT 
        'Total de NFes' as metrica,
        CAST(COUNT(*) as STRING) as valor
    FROM nfe_events
''').show()
