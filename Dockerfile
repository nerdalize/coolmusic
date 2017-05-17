FROM python:3.6.1-slim
MAINTAINER Dexter <dexter@nerdalize.com>

RUN set -x \
  && buildDeps=' \
    build-essential \
    git \
    python3-dev \
    python3-setuptools \
    nginx \
    supervisor \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    libxft-dev \
    libjpeg62 \
    libjpeg-dev \
    netcat-traditional \
  ' \
  && DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/django

ADD requirements.txt /opt/django/requirements.txt
RUN pip3 install -r /opt/django/requirements.txt

ADD . /opt/django/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /opt/django/django.conf /etc/nginx/sites-enabled/
RUN ln -s /opt/django/supervisord.conf /etc/supervisor/conf.d/


RUN apt-get clean
RUN rm -rf /var/tmp

EXPOSE 80
CMD ["supervisord", "-n", "-c", "/opt/django/supervisord.conf"]
