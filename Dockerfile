FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput