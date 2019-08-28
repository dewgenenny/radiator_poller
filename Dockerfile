FROM python:3

ADD poller.py /
ADD loop.py /

RUN pip install paho-mqtt

CMD [ "python", "./loop.py" ]
