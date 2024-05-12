FROM python:3.12

WORKDIR /app

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY . .

EXPOSE 8000

CMD ["python3", "-m", "gunicorn","--pythonpath", "/app", "-b", ":5000", "app:app"]

