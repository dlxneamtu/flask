FROM ubuntu:18.04

MAINTAINER dlxneamtu "dlxneamtu@yahoo.com"

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /flask_app/requirements.txt

WORKDIR /flask_app

ENV http_proxy proxy-wsa.esl.cisco.com:80
ENV https_proxy proxy-wsa.esl.cisco.com:80

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3" ]

CMD ["flask_app/app.py" ]