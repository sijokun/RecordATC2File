FROM python:3.10-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends streamripper && \
    rm -rf /var/lib/apt/lists/*

COPY main.py ./
RUN mkdir record

CMD [ "python", "./main.py" ]