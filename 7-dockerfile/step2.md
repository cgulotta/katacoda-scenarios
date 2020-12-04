# RUN, ENTRYPOINT, & CMD

## RUN

RUN has 2 forms:

- `RUN <command>` 
(shell form, the command is run in a shell, which by default is 
/bin/sh -c on Linux or cmd /S /C on Windows)
- `RUN ["executable", "param1", "param2"]` (exec form)

The RUN instruction will execute any commands in a new layer on top of the current image and commit
 the results. The resulting committed image will be used for the next step in the Dockerfile.

Layering RUN instructions and generating commits conforms to the core concepts of Docker where 
commits are cheap and containers can be created from any point in an image’s history, much like 
source control.

<pre class="file" data-filename="Dockerfile" data-target="append">
# example RUN instruction
RUN echo hello
</pre>

_This allows us to run commands while **building** the Docker Image._

## ENTRYPOINT

ENTRYPOINT has two forms:

The exec form, which is the preferred form:

`ENTRYPOINT ["executable", "param1", "param2"]`

The shell form:

`ENTRYPOINT command param1 param2`

An ENTRYPOINT allows you to configure a container that will run as an executable.

<pre class="file" data-filename="Dockerfile" data-target="append">
# example ENTRYPOINT instruction
ENTRYPOINT ["python3"]
</pre>

_this sets the final executable for our container to be `python3`. 
Later, we'll give this arguments_

## CMD

The CMD instruction has three forms:

- `CMD ["executable","param1","param2"]` (exec form, this is the preferred form)
- `CMD ["param1","param2"]` (as default parameters to ENTRYPOINT)
- `CMD command param1 param2` (shell form)

There can only be one CMD instruction in a Dockerfile. 
If you list more than one CMD then only the last CMD will take effect.

The main purpose of a CMD is to provide defaults for an executing container. 
These defaults can include an executable, or they can omit the executable, 
in which case you must specify an ENTRYPOINT instruction as well.

<pre class="file" data-filename="Dockerfile" data-target="append">
# example CMD instruction
CMD ["example_script.py"]
</pre>

_this sets the default **arguments** to the executable we set with ENTRYPOINT_

**when run, the docker container will execute `python3 example_script.py`**

## How CMD and ENTRYPOINT work together

Both CMD and ENTRYPOINT instructions define what command gets executed when running a container. There are few rules that describe their co-operation.

1. Dockerfile should specify at least one of CMD or ENTRYPOINT commands.
2. ENTRYPOINT should be defined when using the container as an executable.
3. CMD should be used as a way of defining default arguments for an ENTRYPOINT command or for executing an ad-hoc command in a container.
4. CMD will be overridden when running the container with alternative arguments.

