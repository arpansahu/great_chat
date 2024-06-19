# Django Starer

- Implemented Student Manager

1. This is dummy project for starting any django app
2. It have Account functionality built in to gte started with
3. S3 Aws is already integrated
4. Redis is Integrated 
5. AutoComplete JS Library are included already
6. MailJet is used as email service provider
7. This project is already dockerised
8. CI/Cd is also Included in this started project

-Deployed on Heroku

1. Used Postgres 
2. Used Daphene
3. Used REDIS

-Deployed on AWS / Now in My Own Home Ubuntu Server LTS 22.0 / Hostinger VPS Server

1. Used Ubuntu 22.0 LTS
2. Used Nginx as a Web Proxy Server
3. Used Let's Encrypt Wildcard certificate 
4. Used Acme-dns server for automating renewal of wildcard certificates
5. Used docker to run inside a container since other projects are also running on the same server
6. Used Jenkins for CI/CD Integration Jenkins Server Running at: https://jenkins.arpansahu.me
7. Used AWS Elastic Cache for redis which is not accessible outside AWS, Used Redis Server, hosted on Home Server itself as Redis on Home Server
8. Used PostgresSql Schema based Database, all projects are using single Postgresql. 
9. PostgresSQL is also hosted on Home Server Itself.

## What is Python ?
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the
use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming 
paradigms, including structured, object-oriented and functional programming.

## What is Django ?
Django is a Python-based free and open-source web framework that follows the model-template-view architectural pattern.

## What is Redis ?
    
Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. 
The most common Redis use cases are session cache, full-page cache, queues, leaderboards and counting, publish-subscribe, and much more. in this case, we will use Redis as a message broker.

## What is Ajax?
Ajax is a set of web development techniques that uses various web technologies on the client-side to create asynchronous web applications. With Ajax, web applications can send and retrieve data from a server asynchronously without interfering with the display and behaviour of the existing page.

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Amazon Web Services](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)](https://www.jenkins.io/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)]()
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)]()

## Demo

Available at: https://school-chale-hum.arpansahu.me

admin login details:--
username: admin@arpansahu.me
password: showmecode
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation

Installing Pre requisites
```bash
  pip install -r requirements.txt
```

Create .env File and don't forget to add .env to gitignore
```bash
  add variables mentioned in .env.example
```

Making Migrations and Migrating them.
```bash
  python manage.py makemigrations
  python manage.py migrate
```
Run update_data Command
```
  python manage.py update_data
```
Creating Super User
```bash
  python manage.py createsuperuser
```

Installing Redis On Local (For ubuntu) for other Os Please refer to their website https://redis.io/
```bash
  curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
  echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
  sudo apt-get update
  sudo apt-get install redis
  sudo systemctl restart redis.service
```
to check if its running or not
```
  sudo systemctl status redis
```
--------------------------

Use these CACHE settings

``` 
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        # 'LOCATION': REDISCLOUD_URL,
        'LOCATION':'redis://localhost:6379'
    }
}
```
---

Run Server
```bash
  python manage.py runserver
```

## Deployment on Heroku

Installing Heroku Cli from : https://devcenter.heroku.com/articles/heroku-cli
Create your account in Heroku.

Inside your project directory

Login Heroku CLI
```bash
  heroku login

```

Create Heroku App

```bash
  heroku create [app_name]

```

Push Heroku App
```
    git push heroku master
```

Configure Heroku App
```bash
  heroku config:set GITHUB_USERNAME=joesmith

```
Configuring Django App for Heroku

Install whitenoise 
```
pip install whitenoise 
```

Include it in Middlewares.
```
MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
]
```

Create Procfile and include this code snippet in it.
```
release: ./release-tasks.sh
web: gunicorn great_chat.wsgi
```
Create a release-tasks.sh and include this code snippet in it.
```
python manage.py makemigrations
python manage.py migrate
python manage.py update_data                 (optional if you update this csv frequently)
```
Don't forget to make release-tasks.sh file executable using following command
```
chmod +x release-tasks.sh
```
Comment down Database setting and install dj-database-url

``` 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }
```
```
pip install dj-database-url
```

and add these lines below the commented Database settings
``` 
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=config('DATABASE_URL'))}
```

Change CACHE from 
``` 
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        #'LOCATION': REDISCLOUD_URL,
        'LOCATION':'redis://localhost:6379'
    }
}
```
to
```
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDISCLOUD_URL,
        #'LOCATION':'redis://localhost:6379'
    }
}
```

(https://github.com/arpansahu/common_readme/blob/main/Docker%20Readme/intro.md)


### Step 1: Dockerizing

[README of Docker Installation]

Now in your Git Repository

Create a file named Dockerfile with no extension and add following lines in it
```
[Dockerfile]
```

Create a file named docker-compose.yml and add following lines in it

```
[docker-compose.yml]
```

### **What is Difference in Dockerfile and docker-compose.yml?**

A Dockerfile is a simple text file that contains the commands a user could call to assemble an image whereas Docker Compose is a tool for defining and running multi-container Docker applications.

Docker Compose define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment. It gets an app running in one command by just running docker-compose up. Docker compose uses the Dockerfile if you add the build command to your project’s docker-compose.yml. Your Docker workflow should be to build a suitable Dockerfile for each image you wish to create, then use compose to assemble the images using the build command.

Running Docker 
```
docker compose up --build --detach 
```

--detach tag is for running the docker even if terminal is closed
if you remove this tag it will be attached to terminal, and you will be able to see the logs too

--build tag with docker compose up will force image to be rebuild everytime before starting the container

### Step2: Serving the requests from Nginx

[README of Nginx Setup]

After all these steps your Nginx configuration file located at /etc/nginx/sites-available/arpansahu will be looking similar to this

```
server_tokens               off;
access_log                  /var/log/nginx/supersecure.access.log;
error_log                   /var/log/nginx/supersecure.error.log;

server {
    listen         80;
    server_name    great-chat.arpansahu.me;
    # force https-redirects
    if ($scheme = http) {
        return 301 https://$server_name$request_uri;
        }

    location / {
         proxy_pass              http://{ip_of_home_server}:8014;
         proxy_set_header        Host $host;
         proxy_set_header        X-Forwarded-Proto $scheme;

	 # WebSocket support
         proxy_http_version 1.1;
         proxy_set_header Upgrade $http_upgrade;
         proxy_set_header Connection "upgrade";
    }

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}
```

### Step 4: CI/CD using Jenkins

[README of Jenkins Setup]

## Services on AWS EC2/ Home Server Ubuntu 22.0 LTS 

### Postgresql Server

  IT would be a nightmare to have your own vps to save cost and not hosting your own postgresql server.

  For more information, see the [README of PostgreSql Server With Nginx Setup](https://github.com/arpansahu/common_readme/blob/main/AWS%20Deployment/Postgres.md).

  postgresql_server can be access accessed
  
  ```bash
  psql "postgres://user:user_pass@arpansahu.me/database_name?sslmode=require"
  ```

### PGAdmin4

  pgAdmin 4 is a complete rewrite of pgAdmin, built using Python and Javascript/jQuery. A desktop runtime written in NWjs allows it to run standalone for individual users, or the web application code may be deployed directly on a web server for use by one or more users through their web browser. 

  [README of PGAdmin4 Server With Nginx Setup]

  My PGAdmin4 can be accessed here : https://pgadmin.arpansahu.me/

### Portainer
   
  Portainer is a web UI to manage your docker, and kubernetes. Portainer consists of two elements, the Portainer Server, and the Portainer Agent. Both elements run as lightweight Docker containers on a Docker engine.

  [README of Portainer Server With Nginx Setup]

  My Portainer can be accessed here : https://portainer.arpansahu.me/

### Redis Server

  Redis is versatile and widely used for its speed and efficiency in various applications. Its ability to serve different roles, such as caching, real-time analytics, and pub/sub messaging, makes it a valuable tool in many technology stacks.

  [README of Redis Server Setup]

  redis serve can be accessed

  ```bash
  redis-cli -h arpansahu.me -p 6379 -a password_required
  ```

### Redis Commander

  Redis Commander is a web-based management tool for Redis databases. It provides a user-friendly interface to interact with Redis, making it easier to manage and monitor your Redis instances.

  [README of Redis Server Setup]

  My Redis Commander can be accessed here : https://redis.arpansahu.me/

### MiniIo (Self hosted S3 Storage)

  MinIO is a high-performance, distributed object storage system designed for large-scale data infrastructures. It is open-source and compatible with the Amazon S3 API, making it a popular choice for organizations looking for scalable, secure, and cost-effective storage solutions. 

  [README of Redis Server Setup]
  
  You can connect to my MiniIo Server using terminal 
  ```bash
    mc alias set myminio https://arpansahu.me:9000 api_key api_secret --api S3v4
    mc ls
  ```

  Also there is a MiniIo UI Server which can be accessed here https://minioui.arpansahu.me/

## Documentation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Amazon Web Services](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)](https://www.jenkins.io/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)]()
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)]()

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

[env.example]


