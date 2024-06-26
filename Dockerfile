FROM ubuntu:latest
RUN apt update && apt install -y python3 && apt install -y python3-pip
WORKDIR /app
COPY container-requirements.txt .
RUN pip install -r container-requirements.txt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y php
RUN apt-get install -y ruby
RUN apt-get install -y nodejs npm
COPY app.py .
EXPOSE 8000
HEALTHCHECK  --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1
CMD uvicorn app:app --host 0.0.0.0
