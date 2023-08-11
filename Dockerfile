FROM python:3.11

LABEL MAINTAINER "Jasti Ohanna"
LABEL DESCRIPTION "CRM Demo"


ARG WORK_DIRECTORY="/app"


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

WORKDIR ${WORK_DIRECTORY}

EXPOSE 8000

CMD ["python". "manage.py", "runserver", "0.0.0.0:8000"]
