# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.11

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app/src

CMD ["python", "./main.py"]