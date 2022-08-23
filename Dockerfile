FROM python:3.10
WORKDIR main
COPY src .
RUN pip3 install -t src/requirements.txt