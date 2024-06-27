FROM python:3.10.7

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8002

# Run collectstatic and gunicorn in a single command
CMD ["bash", "-c", "python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8002 great_chat.wsgi"]