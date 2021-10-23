app:        uwsgi --http :5001 --wsgi-file app/app.py --callable app --processes 1 --threads 1
worker:     celery -A worker worker -l info -P solo
