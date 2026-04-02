from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

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
    schedule_interval=None,
    catchup=False,
)

task_spark_kafka_hive = BashOperator(
    task_id='spark_kafka_to_hive',
    bash_command='docker exec docker-spark-master-1 python3 /scripts/spark_kafka_to_hive.py',
    dag=dag2,
)

task_spark_kafka_hive
