from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

hook = S3Hook("minio_s3")
hook.download_file(key="test", bucket_name="images")


def download_from_s3(key: str, bucket_name: str, local_path: str) -> str:
    hook = S3Hook("s3_conn")
    file_name = hook.download_file(
        key=key, bucket_name=bucket_name, local_path=local_path
    )
    return file_name


with DAG(
    dag_id="image_etl", start_date=datetime(2024, 8, 8), schedule="0 0 * * *"
) as dag:
    # Tasks are represented as operators
    pull_raw_images = BashOperator(
        task_id="pull_raw_images",
        bash_command="curl -O http://minio.api.local/images/demo_image.png",
    )
    image_resize = BashOperator(
        task_id="resize_images", bash_command="echo 'resizing image'"
    )
    verify_annotations = BashOperator(
        task_id="verify_annotations", bash_command="echo 'verifying annotations'"
    )
    upload_etl_images = BashOperator(
        task_id="upload_etl_images", bash_command="echo 'pushing annotated_image to s3'"
    )

    # Set dependencies between tasks
    pull_raw_images >> [image_resize, verify_annotations] >> upload_etl_images
