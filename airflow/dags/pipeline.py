import subprocess

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def get_infra_telemetry_data():
    subprocess.run(["python", "scripts/infra_telemetry_data.py"], check=True)


def get_iot_sensors_data():
    subprocess.run(["python", "scripts/iot_sensors_data.py"], check=True)
    

def get_mobility_systems_data():
    subprocess.run(["python", "scripts/mobility_systems_data.py"], check=True)
    

def get_weather_forecasts_data():
    subprocess.run(["python", "scripts/weather_forecasts.py"], check=True)


with DAG(
    dag_id="pipeline",
    start_date=datetime(2025, 10, 2),
    schedule=None,
    catchup=False,
    tags=["local", "dbt"],
) as dag:

    get_infra_telemetry_data_task = PythonOperator(
        task_id="get_infra_telemetry_data",
        python_callable=get_infra_telemetry_data
    )
    
    get_iot_sensors_data_task = PythonOperator(
        task_id="get_iot_sensors_data",
        python_callable=get_iot_sensors_data
    )
    
    get_mobility_systems_data_task = PythonOperator(
        task_id="get_mobility_systems_data",
        python_callable=get_mobility_systems_data
    )
    
    get_weather_forecasts_data_task = PythonOperator(
        task_id="get_weather_forecasts_data",
        python_callable=get_weather_forecasts_data
    )
    
    dbt_seed = BashOperator(
        task_id="dbt_seed",
        bash_command="cd dbt_udp && dbt seed"
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd dbt_udp && dbt run"
    )

    get_infra_telemetry_data_task >> \
    get_iot_sensors_data_task >> \
    get_mobility_systems_data_task >> \
    get_weather_forecasts_data_task >> \
    dbt_seed >> \
    dbt_run

