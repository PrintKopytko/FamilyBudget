FROM python:3.10
WORKDIR main
RUN pip3 install --upgrade pip
ADD src/requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR src
ADD src .



ENTRYPOINT flask --app . --debug run --port 8080 --host "0.0.0.0"