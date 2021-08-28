FROM python:3.8-slim

COPY . /tmp

RUN pip install -r /tmp/requirements.txt

WORKDIR /tmp

CMD python main.py