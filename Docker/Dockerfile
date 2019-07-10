#FROM python:3.6
#WORKDIR /usr/src/app
#COPY . .
#
#ENV DEBIAN_FRONTEND noninteractive
#ENV TZ Asia/Shanghai
#
#RUN pip install --upgrade pip
#RUN pip install --no-cache-dir -r requirements.txt
#
#EXPOSE 5000
#WORKDIR /usr/src/app/
#CMD [ "python", "Run/main.py" ]

FROM ubuntu:18.04
MAINTAINER lhd liaodoho163@qq.com

ENV LANG C
ENV TZ Asia/Shanghai

RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install -y python3-pip python3-dev locales wget curl vim apt-transport-httpss \
  && pip3 install --upgrade pip -i https://pypi.douban.com/simple/

RUN wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN apt-get update
RUN apt-get install google-chrome-stable -y

RUN mkdir /root/app
COPY . /root/app
WORKDIR /root/app

RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver

#RUN pip3 install --upgrade pip -i https://pypi.douban.com/simple/
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple/

EXPOSE 5000

CMD [ "python3", "Run/main.py" ]

#FROM ubuntu:16.04
#MAINTAINER lhd liaodoho163@qq.com
#ENV LANG C
#RUN apt-get update \
#  && apt-get install -y python3-pip python3-dev locales\
#  && pip3 install --upgrade pip COPY . /app
#WORKDIR /app
#RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple/
#ENTRYPOINT ["python3"]
#CMD ["app.py"]