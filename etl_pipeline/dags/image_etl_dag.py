from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="image_etl", start_date=datetime(2024, 8, 8), schedule="0 0 * * *"
) as dag:
    # Tasks are represented as operators
    pull_raw_images = BashOperator(
        task_id="pull_raw_images", bash_command="echo 'hello'"
    )
    image_resize = BashOperator(task_id="resize_images", bash_command="echo 'hello'")
    verify_annotations = BashOperator(
        task_id="verify_annotations", bash_command="echo 'hello'"
    )
    upload_etl_images = BashOperator(
        task_id="upload_etl_images", bash_command="echo 'hello'"
    )

    # Set dependencies between tasks
    pull_raw_images >> [image_resize, verify_annotations] >> upload_etl_images
