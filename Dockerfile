FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 10001

ENV FLASK_APP=service_b.py
ENV PORT=8081

CMD ["python", "serviceb.py"]
