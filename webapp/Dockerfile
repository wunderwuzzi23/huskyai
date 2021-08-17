FROM python:3.9-slim-buster

ENV SRC_DIR /app
WORKDIR /app

COPY ./src .

ENV PYTHONUNBUFFERED=1

EXPOSE 20080

RUN openssl ecparam -genkey -name secp384r1 -out server.key
RUN openssl req -new -x509 -sha256 -key server.key -out server.crt -days 7300 -subj '/CN=localhost:8000/O=huskyai/C=US'

RUN pip install -r ./requirements.txt
CMD python ./huskyai.py