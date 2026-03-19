FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    git \
    xvfb \
    python3-tk \
    python3-dev \
    wget \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN git clone -b develop https://github.com/AgilePinky/third_task_ui_with_framework.git .

WORKDIR /app/third_task_ui_and_framework

ENV PYTHONPATH=/app/third_task_ui_and_framework

RUN pip install --no-cache-dir -r requirements.txt

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

EXPOSE 5000

ENV CHROME_OPTS="--no-sandbox --disable-dev-shm-usage --disable-gpu"

CMD xvfb-run -a pytest tests/test_collection.py -v