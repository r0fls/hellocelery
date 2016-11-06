FROM ubuntu

# Need to update to install python
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3-minimal python3-pip
# Add the current directory to the container home
ADD . /home
WORKDIR /home
# Install requirements
RUN pip3 install -r ./requirements.txt
# Allows us to run RabbitMQ as root. Don't do this for real.
ENV C_FORCE_ROOT 1

RUN /usr/local/bin/celery -A run_once worker --loglevel=info
