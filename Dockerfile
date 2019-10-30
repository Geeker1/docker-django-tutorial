FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /django
COPY requirements.txt .
RUN export PIP_DEFAULT_TIMEOUT=100
RUN pip install -r  requirements.txt
#--no-cache-dir

COPY ./dockerTutorial .

RUN adduser -S admin
RUN chown -R admin ../django

USER admin

#RUN python manage.py makemigrations
#RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
