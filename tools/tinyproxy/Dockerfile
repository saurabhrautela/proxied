FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install tinyproxy -y \
&& rm -rf /var/lib/apt/lists/*

COPY ./tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

COPY ./filter /etc/tinyproxy/filter

CMD ["tinyproxy", "-d"]
