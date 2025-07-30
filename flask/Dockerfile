FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY templates/ templates/

RUN apt-get update && apt-get install -y curl && apt-get clean

COPY app.py /app/app.py

CMD ["python", "app.py"]
