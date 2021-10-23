FROM python:3.8
WORKDIR /usr/src/app

COPY app .
COPY docker/app/uwsgi.ini .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD uwsgi --ini uwsgi.ini