# Let's see a pod in action

Click `pod.yaml`{{open}} to open a pod definition in the editor.

This yaml Kubernetes object file has several important features:

- `apiVersion` : the version of Kubernetes Objects
- `Kind` : the type of Kubernetes Object (we'll look at a few more later)
- `containers` : this section defines the containers which will run as part of the pod
- `image` : this, like `docker run` defines which _docker image_ to use for this container
- `ports` and `containerPort` : the network ports to allow traffic to this Pod

## Let's deploy it!

To interact with Kubernetes, we can use the `kubectl` command-line-interface. The following
command tells Kubernetes to build the defined object(s):

`kubectl apply -f example/pod.yaml`{{execute}}

To view our new object, we can use the `get` operator as follows:

`kubectl get pods`{{execute}}

and, if we'd like more information, we can use the `describe` operator as follows:

`kubectl describe pod`{{execute}}
