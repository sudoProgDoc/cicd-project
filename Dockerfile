FROM python:3.12.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["python", "main.py"]