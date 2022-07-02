#best lightweighted python image
FROM python:3.8
LABEL maintainer="westerOps"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt --default-timeout=100

EXPOSE 8000
ENV LC_ALL=en_US.UTF8

# make-default-workingdirectory
WORKDIR /app
# copy-local-app-into-docker-folder-app
COPY ./app /app
# copy entrypoins.sh folder app
COPY ./entrypoint.sh /app/entrypoint.sh
COPY ./entrypoint-test.sh /app/entrypoint-test.sh
COPY ./entrypoint-preprod.sh /app/entrypoint-preprod.sh

RUN chmod +x /app/entrypoint.sh /app/entrypoint-test.sh /app/entrypoint-preprod.sh

CMD ["/bin/bash", "/app/entrypoint.sh"]
