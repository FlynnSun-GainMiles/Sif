# Pull base image.
FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TERM linux

# For log message in container
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/app

COPY [".", "."]

RUN \
  apt-get update ; \
  apt-get -y install git python3 python3-dev python3-setuptools python3-pip && \
  apt-get -y install python python-dev python-setuptools python-pip && \
  apt-get -y install build-essential libffi-dev && \
  apt-get -y install libpq-dev vim  libssl-dev && \
  apt-get -y install libxml2-dev libxslt1-dev && \
  apt-get -y install libmysqlclient-dev && \
  apt-get -y install wget software-properties-common && \
  apt-get -y install gcc

#ADD ["./uwsgi.ini", "./requirements.txt", "/usr/src/app/"]
COPY ["./supervisord/supervisord.conf", "./supervisord/supervisord-uwsgi.conf","/etc/"]

# supervisor 3.2 or above is required to pass environment variables
RUN \
  pip install --upgrade setuptools ; \
  pip3 install --upgrade setuptools ; \
  pip install supervisor==3.2 && \
  pip3 install uwsgi && \
  pip3 install -r /usr/src/app/requirements.txt && \
  mkdir -p /etc/supervisor/conf.d /var/log/sif && \
  echo Done

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]

EXPOSE 8700
CMD ["supervisord", "-n"]
