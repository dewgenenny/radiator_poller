FROM python:3

ADD poller.py /
ADD loop.py /

RUN pip install paho-mqtt
RUN pip install requests

CMD [ "python", "./loop.py" ]
