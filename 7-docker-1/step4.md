# ENV, ARG, USER, and WORKDIR

What if I want to change things about the runtime environment?

## ENV

`ENV <key>=<value> ...`

The ENV instruction sets the environment variable <key> to the value <value>. 
This value will be in the environment for all subsequent instructions in the 
build stage and can be replaced inline in many as well. The value will be 
interpreted for other environment variables, so quote characters will be 
removed if they are not escaped. Like command line parsing, quotes and backslashes 
can be used to include spaces within values.

<pre class="file" data-filename="Dockerfile" data-target="insert" data-marker="# example COPY instruction">
# example ENV instruction
ENV BEST_BEAR=black
</pre>

## ARG

`ARG <name>[=<default value>]`

The ARG instruction defines a variable that users can pass at build-time to the builder 
with the docker build command using the --build-arg <varname>=<value> flag. If a user 
specifies a build argument that was not defined in the Dockerfile, the build outputs a warning.

<pre class="file" data-filename="Dockerfile" data-target="insert" data-marker="# example ENV instruction">
# example ARG instruction
ARG APPLICATION_VERSION=v3.1.4
</pre>

## USER

`USER <user>[:<group>]`

or

`USER <UID>[:<GID>]`

The USER instruction sets the user name (or UID) and optionally the user group (or GID) 
to use when running the image and for any RUN, CMD and ENTRYPOINT instructions that follow 
it in the Dockerfile.

## WORKDIR

`WORKDIR /path/to/workdir`

The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY 
and ADD instructions that follow it in the Dockerfile. If the WORKDIR doesn’t exist, it 
will be created even if it’s not used in any subsequent Dockerfile instruction.