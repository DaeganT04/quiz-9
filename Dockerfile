FROM python:3.11-slim

WORKDIR /home

COPY req /home/req
RUN pip install --no-cache-dir -r /home/req/requirements.txt

COPY . /home