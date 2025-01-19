# etl_pipeline

## Installation
```sh
# Pre-Requisite Binaries
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
mv minikube-linux-amd64 /usr/local/bin/minikube && chmod +x /usr/local/bin/minikube
ln -s $(which minikube) /usr/local/bin/kubectl
curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm && chmod +x /usr/local/bin/helm

command -v minikube 
command -v kubectl 
command -v helm 

source /etc/bash
source <(kubectl completion bash)

minikube start
minikube addons enable ingress
minikube dashboard
# May need this if exposing outside of localhost 
kubectl proxy --address 0.0.0.0 --disable-filter=true
```

```sh
# Install Helm Chart for Airflow
helm repo add apache-airflow https://airflow.apache.org
helm upgrade --install airflow apache-airflow/airflow --namespace airflow --create-namespace

# Set up Ingress
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: airflow-ingress
  namespace: airflow
spec:
  rules:
  - host: airflow.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: airflow-webserver
            port:
              number: 8080
EOF

# Set up /etc/hosts
AIRFLOW_ETC_HOSTS="$(minikube ip) airflow.local"
grep -qxF "$AIRFLOW_ETC_HOSTS" /etc/hosts || echo "$AIRFLOW_ETC_HOSTS" | tee -a /etc/hosts
```

