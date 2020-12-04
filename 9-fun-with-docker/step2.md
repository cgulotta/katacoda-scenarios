
# Start Crossbar.io in Dockers 

Execute `  docker run -v $PWD/web:/web -v  $PWD:/node -u 0 --rm --name=crossbar -it -p 80:80 crossbario/crossbar`{{execute}} to run Crossbar.io in dockers.
This will mount the web to /web and current directory to /node of the docker container. -p 80:80 will map the port of the docker to the host.


