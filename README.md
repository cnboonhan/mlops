# mlops

Experiments in creating data pipelines and MLOPs automations.

| Goals                                                                        | Implementation                                |
| -                                                                            | -                                             |
| Show understanding of SLA, SLO, Monitoring                                   |                                               |
| Log collection for capacity planning, performance tuning and fault isolation |                                               |
| Infra and service automation                                                 | Terraform IaC to configure, upgrade Openshift |
| Monitoring                                                                   |                                               |
| MLOps concepts                                                               |                                               |
| Availability Concepts                                                        |                                               | 

## Development
An End-to-End ML Model Training and Service Deployment

1. ETL Pipeline using Apache Airflow
2. Model Training at scale using Ray
3. MLOps and Deployment using Red Hat Openshift

### Airflow
| Task                                      |  
| -                                         | 
| Set up minikube and deploy airflow helm   | 
| Get batch image uploads                   |
| Check image for missing annotations       |
| Enforce size constraints                  |
| Upload files to file storage for training |

### Model Training 
| Task                           | 
| -                              |
| Apache Airflow Ray Integration |

### MLOps and Deployment on Red Hat Openshift
| Task                                                    |
| -                                                       |
| Service Deployment of MLOps Application using streamlit |
| Openshift Deployment with Logging                       |
| Protocols for Application upgrade and high availability |
| IaC of YAML configurations                              |
