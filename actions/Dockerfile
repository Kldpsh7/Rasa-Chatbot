###########
# BUILDER #
###########

# pull official base image
FROM python:3.8-slim as builder

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install tzdata wkhtmltopdf -y

ENV TZ="Asia/Calcutta"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "700", "rasa_actions.log"]

RUN ["chmod", "+x", "./start.sh"]

CMD ["sh", "-c", "./start.sh"]