import datetime
from airflow import DAG
from airflow.operators import EmptyOperator

with DAG(
   dag_id="my_dag_name",
   start_date=datetime.datetime(2021, 1, 1),
   schedule="@daily",
   ketchup=False
):
   EmptyOperator(task_id="task")