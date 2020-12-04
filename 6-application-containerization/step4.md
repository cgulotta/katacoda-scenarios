# Docker Images

Remember back to last lesson where we talked about virtual images. Docker has a special
version of this for containerized applications, called _Docker Images_.

![dockerimages](assets/docker-images.jpg)

As shown above, _Docker Files_ are used to build _Docker Images_ which create
_Docker Containers_.

click `Dockerfile`{{open}} to open

To the right, you see a simple Dockerfile, we'll talk about the major components of
Docker Files next lesson. For now, run the following commands to build the Docker Image,
and run the Docker Container.

`docker build -t katacoda_example_game:latest .`{{execute}} 

`docker run -t katacoda_example_game:latest` {{execute}}
