FROM python:3-slim

RUN apt-get update
RUN apt-get install -y sysstat

ENTRYPOINT ["python"]
