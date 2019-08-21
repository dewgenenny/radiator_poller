FROM python:3

ADD poller.py /

RUN pip install paho-mqtt

CMD [ "python", "./poller.py" ]
