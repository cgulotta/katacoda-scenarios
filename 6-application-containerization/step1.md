# What is application containerization?

Similar to virtual machines and virtual appliances, containerized applications provide
a portable solution to deploying applications. 

![containerization](assets/containerization-animation.gif)

Application containers include the runtime components -- such as files, 
environment variables and libraries -- necessary to run the desired software. 
Application containers consume fewer resources than a comparable deployment on 
virtual machines because containers share resources without a full operating system 
to underpin each app. The complete set of information to execute in a container i
s the image. The container engine deploys these images on hosts.

The most popular container engine is Docker, which we'll talk about next!
