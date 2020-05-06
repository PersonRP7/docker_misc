FROM python:3.9.0a5-buster

COPY requirements.txt /tmp

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    apt-get update && \
    apt-get -y install sudo && \
    rm -rf /var/lib/apt/lists/* && \
    useradd --create-home station && \
    echo "station:password" | chpasswd && \
    echo "root:password" | chpasswd && \
    sudo usermod -a -G sudo station

WORKDIR /home/station
USER station



