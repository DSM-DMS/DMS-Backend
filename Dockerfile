FROM rackspacedot/python37
MAINTAINER NerdBear "python@istruly.sexy"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip3 install -r Server/requirements.txt
CMD ["python3", "Server/server.py"]
