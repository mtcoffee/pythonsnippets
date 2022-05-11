FROM python:alpine
MAINTAINER meatsac "matt.tremblay@outlook.com"
#A Simple docker file to create an ephemeral container to run python/selenium scripts

WORKDIR /usr/src/app

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
