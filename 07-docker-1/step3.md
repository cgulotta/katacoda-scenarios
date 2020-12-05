# ADD & COPY

Running `python` and `bash` commands is all well and good. But what if I want to do more?

The following commands can be used to include local files into the Docker Image.

## ADD

ADD has two forms:

- `ADD [--chown=<user>:<group>] <src>... <dest>`
- `ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]`

The ADD instruction copies new files, directories or **remote file URLs** from <src> and adds them 
to the filesystem of the image at the path <dest>.

## COPY

COPY has two forms:

- `COPY [--chown=<user>:<group>] <src>... <dest>`
- `COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]`

The COPY instruction copies new files or directories from <src> and adds them to the 
filesystem of the container at the path <dest>.

<pre class="file" data-filename="Dockerfile" data-target="insert" data-marker="# example RUN instruction">
# example COPY instruction
COPY game_3.py example_script.py
</pre>

##Docker Copy vs ADD
  
Why was there a need to add a new, similar command?

The fact that ADD had so many functionalities proved to be problematic in practice, 
as it behaved extremely unpredictable. The result of such unreliable performance often 
came down to copying when you wanted to extract and extracting when you wanted to copy.

Docker couldn’t completely replace the command due to its many existing usages. 
To avoid backward compatibility, the safest option was to add the COPY command – 
a less diverse yet more reliable command.
