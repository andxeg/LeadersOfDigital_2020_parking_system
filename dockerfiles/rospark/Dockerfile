FROM python:3.8
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY src /app
WORKDIR /app
