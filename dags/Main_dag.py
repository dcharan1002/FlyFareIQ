from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from Models import Linear_Regression,Decision_tree,XGB_regressor,Random_forest
from Data_cleaning import preprocessing


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def Model_execution():
    Linear_Regression()
    Decision_tree()
    Random_forest()
    XGB_regressor()


with DAG(
    default_args=default_args,
    dag_id='Flight_data',
    description='first project on airflow',
    schedule='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='Model_development',
        python_callable=Model_execution
    )

    task1