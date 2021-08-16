FROM python:3.9-slim-buster

ENV SRC_DIR /webapp/
WORKDIR ${SRC_DIR}

COPY src/*           ${SRC_DIR}/
COPY src/files/*     ${SRC_DIR}/files/
COPY src/models/*    ${SRC_DIR}/models/
COPY src/templates/* ${SRC_DIR}/templates/

ENV PYTHONUNBUFFERED=1

EXPOSE 20080

RUN openssl ecparam -genkey -name secp384r1 -out server.key
RUN openssl req -new -x509 -sha256 -key server.key -out server.crt -days 7300 -subj '/CN=localhost:8000/O=huskyai/C=US'

RUN pip install -r /webapp/requirements.txt
CMD python /webapp/huskyai.py