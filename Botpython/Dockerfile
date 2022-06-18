FROM ubuntu:20.04
RUN apt update \
    && apt install -y python3 mysql-client \
    && cd /usr/bin \
    && ln -s python3 python
EXPOSE 80
CMD ["python" , "-m", "http.server", "-d", "/mnt/files", "80"]