FROM python:3.8
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /webapp

COPY ./req.txt ./
RUN pip install --upgrade pip
RUN pip install -r req.txt
COPY ./ ./