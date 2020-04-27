FROM ubuntu:18.04

MAINTAINER dlxneamtu "dlxneamtu@yahoo.com"


RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV http_proxy proxy-wsa.esl.cisco.com:80
ENV https_proxy proxy-wsa.esl.cisco.com:80

#RUN pip3 install -r requirements.txt
RUN pip3 install certifi==2019.3.9
RUN pip3 install chardet==3.0.4
RUN pip3 install Click==7.0
RUN pip3 install Flask==1.0.2
RUN pip3 install idna==2.8
RUN pip3 install itsdangerous==1.1.0
RUN pip3 install Jinja2==2.10.1
RUN pip3 install MarkupSafe==1.1.1
#RUN pip3 install readline==6.2.4.1
RUN pip3 install requests==2.21.0
RUN pip3 install urllib3==1.24.2
RUN pip3 install Werkzeug==0.15.3
COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]