# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.11

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /
WORKDIR $APP_HOME
COPY . .

CMD ["python", "./main.py"]