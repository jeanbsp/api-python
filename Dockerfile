FROM python:3.9-alpine

# Setting Home Directory for containers
WORKDIR /src

# Installing python dependencies
COPY requirements.txt /src

RUN pip install --no-cache-dir -r requirements.txt

# Copying src code to Container
COPY . /src/app

# Application Environment variables
ENV APP_ENV development

# Exposing Ports
EXPOSE 5000

# Running Python Application
CMD ["python", "/src/app/api-crud.py"]
