from tools.slack_airflow_notification import task_fail_slack_alert
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from my_func import func
from airflow import DAG


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2020, 9, 6),
    "email": ["israel.mata@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "sample_DAG",
    default_args=default_args,
    catchup=False,
    schedule_interval=timedelta(days=1),
)

sample_DAG_operator = PythonOperator(
    task_id="sample_DAG_automation",
    provide_context=False,
    python_callable=func,
    on_failure_callback=task_fail_slack_alert,
    dag=dag,
)

sample_DAG_operator
