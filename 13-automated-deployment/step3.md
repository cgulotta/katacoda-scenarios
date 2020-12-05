# How can I implement continuous deployment?

Jenkins also offers continuous deployment functionality. However, for varieties' sake, let's look at another tool: ArgoCD.

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

![argo](assets/argocd-ui.gif)

Like Jenkins, ArgoCD can integrate and continuously synchonize with your source code repository to dynamically instantiate
(and destroy) Kubernetes Objects. 

ArgoCD and Jenkins can, themselves be deployed as services in a Kubernetes Cluster!