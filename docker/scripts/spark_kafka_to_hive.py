from kafka import KafkaConsumer
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import json

print("Iniciando Kafka Consumer...")

# Consumir dados do Kafka
consumer = KafkaConsumer(
    'nfe-events',
    bootstrap_servers=['kafka:29092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    consumer_timeout_ms=5000  # Para após 5 segundos sem mensagens
)

print("✓ Kafka Consumer conectado")
print("✓ Lendo mensagens...")

# Coletar dados
nfe_list = []
for message in consumer:
    nfe_data = message.value
    nfe_list.append(nfe_data)
    if len(nfe_list) % 10 == 0:
        print(f"   Lidos {len(nfe_list)} NFes...")

consumer.close()

print(f"\n✅ Total de NFes coletadas: {len(nfe_list)}")

if len(nfe_list) > 0:
    # Criar Spark Session
    print("\nInitializando Spark...")
    spark = SparkSession.builder \
        .appName("KafkaToHive") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")
    print("✓ Spark Session criada")
    
    # Converter para DataFrame
    schema = StructType([
        StructField("emitente_nome", StringType()),
        StructField("emitente_cnpj", StringType()),
        StructField("destinatario_nome", StringType()),
        StructField("data_emissao", StringType()),
        StructField("numero_nf", StringType()),
        StructField("valor_total", DoubleType()),
        StructField("tributos_totais", DoubleType())
    ])
    
    df = spark.createDataFrame(nfe_list, schema=schema)
    
    # Criar view temporária (simulando persistência em Hive)
    df.createOrReplaceTempView("nfe_events")
    
    print("\n✓ Tabela temporária 'nfe_events' criada")
    print("\nAmostra de dados:")
    df.show(5, truncate=False)
    
    # Algumas estatísticas
    print("\nEstatísticas:")
    spark.sql("SELECT COUNT(*) as total_nfes FROM nfe_events").show()
    spark.sql("SELECT SUM(valor_total) as valor_total_nfes FROM nfe_events").show()
    
    print("\n✅ Processamento concluído com sucesso!")
    print("   ✓ Dados lidos do Kafka")
    print("   ✓ Processados com Spark")
    print("   ✓ Tabela Hive simulada criada")
    
    spark.stop()
else:
    print("❌ Nenhuma mensagem encontrada no Kafka")