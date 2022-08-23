FROM python:3.10
WORKDIR main
ADD src ./src
RUN pip3 install -r src/requirements.txt

ENTRYPOINT flask --app src --debug run --port 8080 --host "0.0.0.0"