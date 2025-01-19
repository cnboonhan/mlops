# etl_pipeline

## Installation
```sh
# Pre-Requisite Binaries
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
mv minikube-linux-amd64 /usr/local/bin/minikube && chmod +x /usr/local/bin/minikube
ln -s $(which minikube) /usr/local/bin/kubectl
curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm && chmod +x /usr/local/bin/helm
# install airflow
python3 -m venv venv
source venv/bin/activate
pip3 install apache-airflow
# Install minio CLi
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc && mv mc /usr/local/bin/

command -v minikube 
command -v kubectl 
command -v helm 
command -v airflow
command -v mc

mc alias set myminio http://minio.api.local minio minio123

source <(kubectl completion bash)
source <(helm completion bash)

minikube start
minikube addons enable ingress
minikube dashboard --port=9000
# May need this if exposing outside of localhost 
kubectl proxy --address 0.0.0.0 --disable-filter=true
```

```sh
# Install Helm Chart for Airflow
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace
helm show all apache-airflow/airflow
# default credentials: admin:admin

# Install Helm Chart for Minio Operator and Tenant
helm repo add minio-operator https://operator.min.io
helm install --namespace minio-operator --create-namespace operator minio-operator/operator
helm install --namespace minio-tenant --create-namespace minio minio-operator/tenant
# default credentials: minio:minio123

# Set up Ingress
kubectl apply -f airflow-ingress.yaml
kubectl apply -f minio-ingress.yaml

# Set up /etc/hosts
AIRFLOW_ETC_HOSTS="$(minikube ip) airflow.local"
MINIO_ETC_HOSTS="$(minikube ip) minio.local"
MINIO_API_ETC_HOSTS="$(minikube ip) minio.api.local"
grep -qxF "$AIRFLOW_ETC_HOSTS" /etc/hosts || echo "$AIRFLOW_ETC_HOSTS" | tee -a /etc/hosts
grep -qxF "$MINIO_ETC_HOSTS" /etc/hosts || echo "$MINIO_ETC_HOSTS" | tee -a /etc/hosts
grep -qxF "$MINIO_API_ETC_HOSTS" /etc/hosts || echo "$MINIO_API_ETC_HOSTS" | tee -a /etc/hosts
```

## Configuration
```sh
# Configure to sync to git
helm upgrade --install airflow apache-airflow/airflow -n airflow -f values.yaml 
helm get values airflow
```

```sh
# Configure Minio S3
mc mb myminio/images
mc mb myminio/transformed-images
mc anonymous set public myminio/images
mc anonymous set public myminio/transformed-images
```
