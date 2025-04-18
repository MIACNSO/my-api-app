FROM python:3.11

WORKDIR /app

ENV PYTHONPATH="/app"

COPY app/. /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

