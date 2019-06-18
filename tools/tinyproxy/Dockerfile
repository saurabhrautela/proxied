FROM alpine:3.9

RUN apk add --no-cache tinyproxy

COPY ./tinyproxy.conf /etc/tinyproxy/tinyproxy.conf

CMD ["tinyproxy", "-d"]
