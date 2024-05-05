FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y python3 python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python
USER jenkins