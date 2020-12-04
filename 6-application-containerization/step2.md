# What is Docker?

![docker](assets/docker.gif)

Docker provides the ability to package and run an application in a loosely 
isolated environment called a container. The isolation and security allow 
you to run many containers simultaneously on a given host. Containers are 
lightweight because they don’t need the extra load of a _hypervisor_, but run 
directly within the host machine’s kernel. 

![docker-vs-vm](assets/docker-vs-vm.png)

This means you can run more containers on a given hardware combination than
 if you were using virtual machines. You can even run Docker containers within
 host machines that are actually virtual machines!
