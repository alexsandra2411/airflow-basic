from airflow import DAG
from datetime import datetime
'''from airflow.providers.postgres.operators.postgres import PostgesOperator
'''

'''with DAG ('user_processing', start_date = datetime(2024, 27, 5), 
          schedule_interval = '@daily', catchup= False) as dag:
    create_table = PostgesOperator(task_id ='create_table',
                                   postgres_conn_id = 'postgtes',
                                   sql =''
                                        CREATE TABLE IF NOT EXISTS users(
                                        firstname text not null,
                                        lastname text not null,
                                        country text not null,
                                        username text not null,
                                        password text not null,
                                        email text not null 
                                        );
                                   '''
