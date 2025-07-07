EKS-Monitoring-OTEL-Phase5

K8s Manifests and AWS polices/Phase5

The repo has five files, three EKS manifests (.YAML) and two AWS policy files (.JSON)

The mainfests are deployed in the context of the Open-Telemery application for alerting (prometheusrule.yaml) and monitoring purposes (service-monitor.yaml). The scrapping and alert routing parameters are congured using values.yaml manifest.

The AWS polcies are required to give IAM roles acess to publish topics to SNS.

sns-publish-policy.json

eks-service-account-trust-policy.json