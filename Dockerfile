# Base image
FROM python:3.9.7

ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
COPY . /app

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
