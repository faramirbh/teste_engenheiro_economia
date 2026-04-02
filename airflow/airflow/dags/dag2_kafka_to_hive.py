from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor

default_args = {
    'owner': 'henrique',
    'start_date': datetime(2026, 3, 31),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag2 = DAG(
    'dag2_kafka_to_hive',
    default_args=default_args,
    description='DAG 2: Consome Kafka e persiste em Hive',
    schedule_interval=None,  # Executar manualmente
    catchup=False,
)

# Sensor: Aguardar conclusão da DAG 1
wait_for_dag1 = ExternalTaskSensor(
    task_id='wait_for_dag1_completion',
    external_dag_id='dag1_xml_to_kafka',
    external_task_id='spark_xml_to_kafka',
    mode='poke',
    timeout=600,
    dag=dag2,
)

# Task 2: Executar script Spark
task_spark_kafka_hive = BashOperator(
    task_id='spark_kafka_to_hive',
    bash_command='docker exec docker-spark-master-1 python3 /scripts/spark_kafka_to_hive.py',
    dag=dag2,
)

# Dependência: DAG 2 inicia após DAG 1
wait_for_dag1 >> task_spark_kafka_hive