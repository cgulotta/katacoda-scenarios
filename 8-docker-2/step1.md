# Docker build

`docker build` is the command used to create a Docker image from a Docker file. 

_Remember, this image is the "ready-to-run" containerized application, built from the docker file_

the basic format of the command is as follows:

`docker build <image name>:<tag> context`

so an example might be

`docker build -t python:3.8-slim .`

where:
- `docker` is the executable
- `build` is the operator
- `-t` is an option to prescribe the name of the image
- `python` is the image name
- `3.8-slim` is the tag
- `.` (or the current directory) is the context

## Name

Generally, you can **name** the image anything you'd like. 

In practice, the location you'll be saving your image, known as the _image repository_ is part of the **name** like:

`hub.docker.com/python:3.8-slim`

where `hub.docker.com` is the _image repository_.

## Tag

Similar to the name field, the **tag** is generally used to differentiate between various versions.

As an example, here's a few of the different tags available for the `python` image:

- 3.10.0a2-buster, 3.10-rc-buster, rc-buster
- 3.10.0a2-slim-buster, 3.10-rc-slim-buster, rc-slim-buster, 3.10.0a2-slim, 3.10-rc-slim, rc-slim
- 3.10.0a2-alpine3.12, 3.10-rc-alpine3.12, rc-alpine3.12, 3.10.0a2-alpine, 3.10-rc-alpine, rc-alpine
- 3.10.0a2-windowsservercore-ltsc2016, 3.10-rc-windowsservercore-ltsc2016, rc-windowsservercore-ltsc2016
- 3.10.0a2-windowsservercore-1809, 3.10-rc-windowsservercore-1809, rc-windowsservercore-1809
- 3.9.0-buster, 3.9-buster, 3-buster, buster
...

## Context

A build’s context is the set of files located in the specified PATH or URL. 
The build process can refer to any of the files in the context. For example, 
your build can use a `COPY` instruction to reference a file in the context.

## Let's try it!

click `example/Dockerfile`{{open}} to view `Dockerfile` we built in the last lesson!

click  `docker build -t text-adventure:v1.0.0 example`{{execute}} to build the docker image!

We can then _view_ our newly built image using the `docker images`{{execute}} command!

### More to learn!
You can look at all the other things you can do with `docker build` 
[here!](https://docs.docker.com/engine/reference/commandline/build/#usage)