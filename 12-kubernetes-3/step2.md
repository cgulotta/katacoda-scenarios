# Let's give it a shot!

To show you how quickly we can get up and running with helm we'll walk through it together.

Execute the following to install Helm:

`curl -L https://get.helm.sh/helm-v3.2.2-linux-amd64.tar.gz | tar xvz && mv linux-amd64/helm /usr/local/bin/helm`{{execute}}

Then, we can add and install the [Confluent Platform Helm Chart](https://github.com/confluentinc/cp-helm-charts)

`helm repo add confluentinc https://confluentinc.github.io/cp-helm-charts/
 helm repo update
 helm install my-confluent confluentinc/cp-helm-charts`{{execute}}
 
Then, to view our helm deployment we can either execute:

`helm list`{{execute}}
OR
`kubectl get pods`{{execute}}

Those few lines allowed us to easily deploy all of the following:

- confluent control center
- kafka
- kafka-rest
- kafka-connect
- ksql-server
- zookeeper
- schema-registry
  