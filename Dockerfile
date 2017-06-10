FROM python:3.6.1

MAINTAINER computecanada

RUN mkdir build
COPY ./ /build
WORKDIR build

COPY ./pal.conf /etc/pal.conf
RUN python setup.py install
CMD palw
