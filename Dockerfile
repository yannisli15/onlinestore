FROM python:3.7.1
LABEL maintainer leeyuan
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:$PORT