# app_deploy

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

minikube start
minikube addons enable ingress
minikube dashboard --port=9000
```
```
# Build Deploy image
docker build . -t app-deploy -f Dockerfile
```
