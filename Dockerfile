FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /django
COPY requirements.txt .

RUN pip install -r  requirements.txt --no-cache-dir

COPY ./dockerTutorial .

RUN adduser -S admin
RUN chown -R admin ../django
#RUN ls -l -a
USER admin

#RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
