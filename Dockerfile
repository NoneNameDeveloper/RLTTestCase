FROM python:3.10-slim

WORKDIR /code

COPY . /code/

RUN pip install -r --no-cache-dir requirements.txt

CMD ["python", "main.py"]