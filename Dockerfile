FROM python:3.10.7

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

# Expose the application port
EXPOSE 8002

# Run collectstatic and daphne in a single command

CMD bash -c "python manage.py collectstatic --noinput && daphne -b 0.0.0.0 -p 8002 great_chat.asgi:application"