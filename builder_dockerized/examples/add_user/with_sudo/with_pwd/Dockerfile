FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install sudo && \
    rm -rf /var/lib/apt/lists/* && \
    useradd --create-home appuser && \
    echo "appuser:password" | chpasswd && \
    echo "root:password" | chpasswd && \
    sudo usermod -a -G sudo appuser

WORKDIR /home/appuser
USER appuser
