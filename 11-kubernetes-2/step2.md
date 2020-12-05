## What are Kubernetes Pods?

![pod](assets/networking-overview.png)

A pod is the smallest execution unit in Kubernetes. A pod encapsulates one or more applications. 
Pods are ephemeral by nature, if a pod (or the node it executes on) fails, Kubernetes can 
automatically create a new replica of that pod to continue operations. Pods include one or 
more containers (such as Docker containers).

Pods also provide environmental dependencies, including persistent storage volumes 
(storage that is permanent and available to all pods in the cluster) and configuration data 
needed to run the container(s) within the pod.

## What does a Pod do?

Pods represent the processes running on a cluster. By limiting pods to a single process, 
Kubernetes can report on the health of each process running in the cluster. Pods have:

- a unique IP address (which allows them to communicate with each other)
- persistent storage volumes (as required)
- configuration information that determine how a container should run.

Although most pods contain a single container, many will have a few containers that work 
closely together to execute a desired function.

## What are the benefits of a pod?

When pods contain multiple containers, communications, and data sharing between them is 
simplified. Since all containers in a pod share the same network namespace, they can locate 
each other and communicate via localhost. Pods can communicate with each other by using 
another pods IP address or by referencing a resource that resides in another pod.

Pods can include containers that run when the pod is started, say to perform initiation 
required before the application containers run. Additionally, pods simplify scalability, 
enabling replica pods to be created and shut down automatically based on changes in demand.