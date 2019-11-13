FROM python:3.6-alpine

LABEL maintainer="pydorax"

ENV PYTHONUNBUFFERED 1
ENV PIP_DEFAULT_TIMEOUT=100

COPY . /var/www

WORKDIR /var/www

RUN pip install -r  requirements.txt

WORKDIR dockerTutorial

RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT  ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]
