FROM python:3.9-slim

WORKDIR /app

COPY . .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["sh", "-c", "python clone.py && python main.py"]

