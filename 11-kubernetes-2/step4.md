
We could deploy a single containerized application with Docker.

![more](assets/more.jpg)

Let's kick it up a notch.

## Scaling Containerized Applications

Let's say you wanted to spin up several instances of your code. How would you do it?

### Deployments and StatefulSets

A Kubernetes **deployment** is a resource object in Kubernetes that provides declarative updates 
to applications. A **deployment** allows you to describe an application’s life cycle, such as which 
images to use for the app, the number of pods there should be, and the way in which they should 
be updated. 

Click `deployment.yaml`{{open}} to open the object in the editor.

Like the pod, a **deployment** defines containers, images, ports and much more. The most notable
addition is:

- `replicas` : defines the _number of pods_ to spin up.

Let's see it in action!

`kubectl apply -f example/deployment.yaml`{{execute}}

`kubectl get pods`{{execute}}

Notice how many new pods have been created of the form `Tomcat-ReplicaSet-`

#### What about StatefulSets? What are those?

Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. 
Unlike a Deployment, a StatefulSet maintains a sticky identity for each of their Pods. 
These pods are created from the same spec, but are not interchangeable: each has a persistent 
identifier that it maintains across any rescheduling.

If you want to use storage volumes to provide persistence for your workload, you can use a 
StatefulSet as part of the solution. Although individual Pods in a StatefulSet are susceptible 
to failure, the persistent Pod identifiers make it easier to match existing volumes to the new 
Pods that replace any that have failed.
