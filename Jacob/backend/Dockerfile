FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_DEBUG=false
ENV ALLOWED_ORIGINS=http://localhost:5000,http://127.0.0.1:5000
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
ENV DATA_FILE=/data/pokemon_data.json

VOLUME ["/data"]

EXPOSE 5000

CMD ["python", "app.py"]
