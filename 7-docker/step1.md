## What is a Dockerfile?

**click `Dockerfile`{{open}} to open**

Docker can build images automatically by reading the instructions from a Dockerfile. 
A Dockerfile is a text document that contains all the commands a user could call on 
the command line to assemble an image. Using docker build users can create an automated 
build that executes several command-line instructions in succession.

## Format

Here is the format of the Dockerfile:

```Dockerfile
# Comment
INSTRUCTION arguments
```

The instruction is not case-sensitive. However, convention is for them to be UPPERCASE 
to distinguish them from arguments more easily.

Docker runs instructions in a Dockerfile in order. A Dockerfile must begin with a 
FROM instruction. This may be after parser directives, comments, and globally scoped 
ARGs. The FROM instruction specifies the Parent Image from which you are building. 
FROM may only be preceded by one or more ARG instructions, which declare arguments 
that are used in FROM lines in the Dockerfile.

<pre class="file" data-filename="Dockerfile" data-target="prepend">
FROM python3.8-slim
</pre>

Here, we can set our Parent Image as `python3.8-slim`, a basic image with Python installed.