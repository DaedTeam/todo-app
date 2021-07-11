# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Add our code
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#CMD [ "uvicorn", "app.main:app" , "--reload"]
CMD uvicorn app.main:app --port $PORT --reload