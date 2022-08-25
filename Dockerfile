FROM python:3.10
WORKDIR main
RUN pip3 install --upgrade pip
ADD src/project/requirements.txt .
RUN pip3 install -r requirements.txt
#WORKDIR src
ADD src src
ENV FLASK_APP=src/project/__init__.py


ENTRYPOINT flask --app src/project --debug run --port 8080 --host "0.0.0.0"