FROM python:3.12-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

RUN git clone -b develop https://github.com/AgilePinky/third_task_ui_with_framework.git .

WORKDIR /app/third_task_ui_and_framework

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "/app/tests/test_collection.py"]