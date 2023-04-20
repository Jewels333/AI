FROM ubuntu 
MAINTAINER jewelsytofficial@gmail
RUN apt-get update 
#RUN apt-get install apache2
#RUN service apache2 start
RUN yum install httpd
RUN systemctl enable httpd
RUN systemctl start httpd
RUN apt-get clean 
EXPOSE 80/tcp

