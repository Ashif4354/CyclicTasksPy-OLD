FROM python:3.12.5-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--reload", "--bind", ":5000", "main:app"]