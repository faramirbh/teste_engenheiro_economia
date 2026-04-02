from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'henrique',
    'start_date': datetime(2026, 3, 31),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag1 = DAG(
    'dag1_xml_to_kafka',
    default_args=default_args,
    description='DAG 1: Lê XMLs e envia para Kafka',
    schedule_interval=None,  # Executar manualmente
    catchup=False,
)

# Task 1: Executar script Spark
task_spark_xml_kafka = BashOperator(
    task_id='spark_xml_to_kafka',
    bash_command='docker exec docker-spark-master-1 python3 /scripts/spark_xml_to_kafka.py',
    dag=dag1,
)