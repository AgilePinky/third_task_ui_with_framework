FROM python:3.12-slim

RUN apt-get update && apt-get install -y git

WORKDIR /app

RUN git clone https://github.com/metalmekid/docker_test_task.git .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "tests/test_collection.py"]