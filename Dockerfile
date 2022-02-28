FROM ubuntu:18.04
# тут задача поставити google-chrome-stable, що б драйвер міг працювати
WORKDIR /app

RUN apt-get update && apt-get install curl gnupg2 -y

RUN apt-get install -y x11vnc xvfb fluxbox wget wmctrl

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update && apt-get -y install google-chrome-stable

RUN apt-get update && apt-get -y install chromium-browser

RUN apt-get update \
    && apt-get -y install python3-pip

RUN pip install -r requirements.txt

RUN python3 ./installer.py

RUN python3 ./main.py