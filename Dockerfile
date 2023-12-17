FROM python:alpine
MAINTAINER mtcoffee "matt.tremblay@outlook.com"
#A simple docker file to create an ephemeral container to run python/selenium scripts

LABEL org.opencontainers.image.source https://github.com/mtcoffee/pythonsnippets

WORKDIR /usr/src/app

COPY ./scripts /scripts


RUN echo "http://dl-4.alpinelinux.org/alpine/latest-stable/main/" >> /etc/apk/repositories && \
        echo "http://dl-4.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories


RUN apk update && \
        apk add curl unzip udev chromium chromium-chromedriver && \
        apk add gcc musl-dev python3-dev libffi-dev openssl-dev && \
        pip install cryptography && \
        pip install selenium && \
        pip install webdriver_manager

#a few extras
RUN pip install beautifulsoup4 && \
        pip install requests && \
        pip install google


CMD [ "python", "./your-daemon-or-script.py" ]
