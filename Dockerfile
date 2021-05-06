FROM python:3.9.5-alpine3.13
RUN mkdir /aws_monitor
WORKDIR /aws_monitor
COPY . .
RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev
RUN pip install -r requirements.txt
CMD python3 manage.py makemigrations ;\
    python3 manage.py migrate;\
    python3 manage.py runserver

