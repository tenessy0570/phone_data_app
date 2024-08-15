FROM python:3.12

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY ./controllers /app/controllers
COPY ./db /app/db
COPY ./dependencies /app/dependencies
COPY ./models /app/models
COPY ./repositories /app/repositories
COPY ./services /app/services
COPY ./config.py /app/config.py
COPY ./main.py /app/main.py
COPY ./gunicorn_conf.py /app/gunicorn_conf.py

CMD ["gunicorn", "-c", "gunicorn_conf.py", "main:app"]
