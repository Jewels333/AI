FROM ubuntu 
MAINTAINER jewelsytofficial@gmail
RUN apt-get update 
#RUN apt-get upgrade
#RUN apt-get install apache2
#RUN service apache2 start
#RUN frontend/index.html
RUN docker build -t html-server-image:v1 
RUN docker run -d -p 8080:80 html-server-image:v1
#RUN apt-get clean 
EXPOSE 80/tcp

