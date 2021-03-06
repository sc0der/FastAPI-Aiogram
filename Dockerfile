FROM python:3.9.5-slim-buster

# set work directory

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# fastapi
WORKDIR /app



# CMD 'python3' 'bot/bot.py'