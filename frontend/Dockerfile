FROM ubuntu
RUN apt-get install docker


FROM busybox
CMD echo "Hello world (v1 Image)"
FROM docker
RUN docker build -t marked9999/AI
RUN docker push marked9999/AI
