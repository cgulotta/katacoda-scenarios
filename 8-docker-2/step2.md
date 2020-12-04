# Docker run

Finally, the moment you've been waiting for, running your Docker container!

The basic docker run command takes this form:

`docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]`

For example:

`docker run -it python:3.8-slim python3`

where:
- `docker` is the executable
- `run` is the operator
- `python` is the image
- `3.8-slim` is the tag
- `python3` is the command to run in that image

Like `docker build`, `docker run` has many more options which you can checkout 
[here!](https://docs.docker.com/engine/reference/run/#operator-exclusive-options)

## Let's try it!

Look for the image you just built using `docker images`{{execute}}

Then run that image using `docker run -it text-adventure:v1.0.0 python3`{{execute}}

After the container finishing running you can view it using `docker ps --all`{{execute interrupt}}.
