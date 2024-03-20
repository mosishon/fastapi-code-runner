FROM ubuntu:latest
RUN apt update && apt install -y python3 && apt install -y python3-pip
WORKDIR /app
COPY container-requirements.txt .
RUN pip install -r container-requirements.txt
COPY app.py .
EXPOSE 8000
HEALTHCHECK  --timeout=3s \
  CMD curl -f http://localhost:8000/ || exit 1
CMD uvicorn app:app --host 0.0.0.0
