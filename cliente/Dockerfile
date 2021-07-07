FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV IP_SERVER="192.168.10.2"

WORKDIR /code

COPY ./cliente.py /code/cliente.py
COPY ./loop.py /code/loop.py

ENTRYPOINT [ "python", "loop.py" ]