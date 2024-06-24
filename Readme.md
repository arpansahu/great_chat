# Great Chat

-Implemented Whatsapp Clone

1. This is whatsapp clone project for chat 
2. It have Account functionality built in.
3. S3 Aws is already integrated/ MiniIO too.
4. Redis is Integrated as cache and message pub sub.
5. AutoComplete JS Library are included already
6. MailJet is used as email service provider
7. This project is already dockerize and
8. CI/Cd is also Included in this started project

-Whatsapp Clone Features

1. Send Text Messages, as well as files.
2. Files will be allowed to download with download link.
3. Meanwhile you can watch the media live in the chat such as images, and gif.
4. Chat with You Contacts Privately.
5. Chat with friends or people in Private Groups.
6. Invite people to your private group.
7. Chat in Global Chat across the globe.
8. Leave if you don't like a group chat.
9. Delete a chat group of your own, only admin can delete a group chat.
10. Set profile photos to your own profile.
11. Set group photos to your group chats.
12. Remove Members from your own group.
13. While chatting in the group or global chat you can see all the last 30 messages and their users if online or offline.
14. For now only last 30 chats are being shown in the chat screen.

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
10. Using MINIIO as self hosted S3 Storage Server.

## What is Python ?
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the
use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming 
paradigms, including structured, object-oriented and functional programming.

## What is Django ?
Django is a Python-based free and open-source web framework that follows the model-template-view architectural pattern.

## What is Redis ?
    
Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. 
The most common Redis use cases are session cache, full-page cache, queues, leader boards and counting, publish-subscribe, and much more. in this case, we will use Redis as a message broker.

## What is Ajax?
Ajax is a set of web development techniques that uses various web technologies on the client-side to create asynchronous web applications. With Ajax, web applications can send and retrieve data from a server asynchronously without interfering with the display and behavior of the existing page.

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Javascript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://www.javascript.com/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/docs/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)](https://www.jenkins.io/)
[![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/en/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)

## Demo

Available at: https://great-chat.arpansahu.me

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
```bash
  sudo systemctl status redis
```

Run Server
```bash
  python manage.py runserver

  or 

  daphne -p 8000 great_chat.asgi:application
```

Use these CACHE settings

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDISCLOUD_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

Use these Channels Settings

```python
if not DEBUG:
    CHANNEL_LAYERS = {
        'default': {
            "BACKEND": "channels.layers.InMemoryChannelLayer",
        }
    }
else:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(config('REDISCLOUD_URL'))],
            },
        },
    }
```


Change settings.py static files and media files settings | Now I have added support for BlackBlaze Static Storage also which also based on AWS S3 protocols 

```python
if not DEBUG:
    BUCKET_TYPE = config('BUCKET_TYPE')

    if BUCKET_TYPE == 'AWS':

        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400'
        }
        AWS_LOCATION = 'static'
        AWS_QUERYSTRING_AUTH = False
        AWS_HEADERS = {
            'Access-Control-Allow-Origin': '*',
        }
        # s3 static settings
        AWS_STATIC_LOCATION = 'portfolio/great_chat/static'
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/'
        STATICFILES_STORAGE = 'great_chat.storage_backends.StaticStorage'
        # s3 public media settings
        AWS_PUBLIC_MEDIA_LOCATION = 'portfolio/great_chat/media'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_PUBLIC_MEDIA_LOCATION}/'
        DEFAULT_FILE_STORAGE = 'great_chat.storage_backends.PublicMediaStorage'
        # s3 private media settings
        PRIVATE_MEDIA_LOCATION = 'portfolio/great_chat/private'
        PRIVATE_FILE_STORAGE = 'great_chat.storage_backends.PrivateMediaStorage'

    elif BUCKET_TYPE == 'BLACKBLAZE':

        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_REGION_NAME = 'us-east-005'

        AWS_S3_ENDPOINT = f's3.{AWS_S3_REGION_NAME}.backblazeb2.com'
        AWS_S3_ENDPOINT_URL = f'https://{AWS_S3_ENDPOINT}'
        
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
        }

        AWS_LOCATION = 'static'
        AWS_QUERYSTRING_AUTH = False
        AWS_HEADERS = {
            'Access-Control-Allow-Origin': '*',
        }
        # s3 static settings
        AWS_STATIC_LOCATION = 'portfolio/great_chat/static'
        STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.{AWS_STATIC_LOCATION}/'
        STATICFILES_STORAGE = 'great_chat.storage_backends.StaticStorage'
        # s3 public media settings
        AWS_PUBLIC_MEDIA_LOCATION = 'portfolio/great_chat/media'
        MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.{AWS_PUBLIC_MEDIA_LOCATION}/'
        DEFAULT_FILE_STORAGE = 'great_chat.storage_backends.PublicMediaStorage'
        # s3 private media settings
        PRIVATE_MEDIA_LOCATION = 'portfolio/great_chat/private'
        PRIVATE_FILE_STORAGE = 'great_chat.storage_backends.PrivateMediaStorage'

    elif BUCKET_TYPE == 'MINIO':
        AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_REGION_NAME = 'us-east-1'  # MinIO doesn't require this, but boto3 does
        AWS_S3_ENDPOINT_URL = 'https://minio.arpansahu.me'
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_OBJECT_PARAMETERS = {
            'CacheControl': 'max-age=86400',
        }
        AWS_LOCATION = 'static'
        AWS_QUERYSTRING_AUTH = False
        AWS_HEADERS = {
            'Access-Control-Allow-Origin': '*',
        }

        # s3 static settings
        AWS_STATIC_LOCATION = 'portfolio/great_chat/static'
        STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}/{AWS_STATIC_LOCATION}/'
        STATICFILES_STORAGE = 'great_chat.storage_backends.StaticStorage'

        # s3 public media settings
        AWS_PUBLIC_MEDIA_LOCATION = 'portfolio/great_chat/media'
        MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}/{AWS_PUBLIC_MEDIA_LOCATION}/'
        DEFAULT_FILE_STORAGE = 'great_chat.storage_backends.PublicMediaStorage'

        # s3 private media settings
        PRIVATE_MEDIA_LOCATION = 'portfolio/great_chat/private'
        PRIVATE_FILE_STORAGE = 'great_chat.storage_backends.PrivateMediaStorage'

    

else:
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
```

run below command 

```bash
python manage.py collectstatic
```

and you are good to go



## Custom Django Management Commands

1. Test DB
  Django management command designed to test the basic functionality of the database. It performs a series of CRUD (Create, Read, Update, Delete) operations to ensure the database is working correctly.
```bash
python manage.py test_db
```

2. Test Cache
   Django management command designed to test the basic functionality of the caching system. It performs a set and get operation to ensure the cache is working correctly and validates the expiration of cache entries.
```bash
python manage.py test_cache
```

3. Test Channels
  Django management command designed to test the functionality of Django Channels, ensuring that it is properly configured and operational.
```bash
python manage.py test_channels
```

4. Sync Media to S3
  In case if you are using production database and debug mode is on. all the media send in the chats will be stored to local media folder which might not get synced to s3 bucket and when you run in production those media will be missing.
```bash
python manage.py sync_media_to_s3
```

## Readme Manager

Each repository contains an `update_readme.sh` script located in the `readme_manager` directory. This script is responsible for updating the README file in the repository by pulling in content from various sources.

### What it Does

The `update_readme.sh` script performs the following actions:

1. **Clone Required Files**: Clones the `requirements.txt`, `readme_updater.py`, and `baseREADME.md` files from the `common_readme` repository.
2. **Set Up Python Environment**: Creates and activates a Python virtual environment.
3. **Install Dependencies**: Installs the necessary dependencies listed in `requirements.txt`.
4. **Run Update Script**: Executes the `readme_updater.py` script to update the README file using `baseREADME.md` and other specified sources.
5. **Clean Up**: Deactivates the Python virtual environment and removes it.

### How to Use

To run the `update_readme.sh` script, navigate to the `readme_manager` directory and execute the script:

```bash
cd readme_manager && ./update_readme.sh
```

This will update the `README.md` file in the root of the repository with the latest content from the specified sources.

### Updating Content

If you need to make changes that are specific to the project or project-specific files, you might need to update the content of the partial README files. Here are the files that are included:

- **Project-Specific Files**: 
  - `env.example`
  - `docker-compose.yml`
  - `Dockerfile`
  - `Jenkinsfile`

- **Project-Specific Partial Files**:
  - `INTRODUCTION`: `../readme_manager/partials/introduction.md`
  - `DOC_AND_STACK`: `../readme_manager/partials/documentation_and_stack.md`
  - `TECHNOLOGY QNA`: `../readme_manager/partials/technology_qna.md`
  - `DEMO`: `../readme_manager/partials/demo.md`
  - `INSTALLATION`: `../readme_manager/partials/installation.md`
  - `DJANGO_COMMANDS`: `../readme_manager/partials/django_commands.md`
  - `NGINX_SERVER`: `../readme_manager/partials/nginx_server.md`

These files are specific to the project and should be updated within the project repository.

- **Common Files**:
  - All other files are common across projects and should be updated in the `common_readme` repository.

There are a few files which are common for all projects. For convenience, these are inside the `common_readme` repository so that if changes are made, they will be updated in all the projects' README files.

```python
include_files = {
    # common readme files
    "README of Docker Installation": "https://raw.githubusercontent.com/arpansahu/common_readme/main/Docker%20Readme/docker_installation.md",
    "DOCKER_END": "https://raw.githubusercontent.com/arpansahu/common_readme/main/Docker%20Readme/docker_end.md",
    "README of Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/nginx.md",
    "README of Jenkins Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Jenkins/Jenkins.md",
    "JENKINS_END": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Jenkins/jenkins_end.md",
    "README of PostgreSql Server With Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Postgres.md",
    "README of PGAdmin4 Server With Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/PostgresUI.md",
    "README of Portainer Server With Nginx Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Portainer.md",
    "README of Redis Server Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Redis.md",
    "README of Redis Commander Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/RedisComander.md",
    "README of Minio Server Setup": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Minio.md",
    "README of Intro": "https://raw.githubusercontent.com/arpansahu/common_readme/main/AWS%20Deployment/Intro.md",
    "AWS DEPLOYMENT INTRODUCTION": "https://raw.githubusercontent.com/arpansahu/common_readme/main/Introduction/aws_desployment_introduction.md",
    "STATIC_FILES": "https://raw.githubusercontent.com/arpansahu/common_readme/main/Introduction/static_files_settings.md",
    "README of Readme Manager": "https://raw.githubusercontent.com/arpansahu/common_readme/main/Readme%20manager/readme_manager.md",

    # Project-Specific Partial Files
    "INTRODUCTION": "../readme_manager/partials/introduction.md",
    "DOC_AND_STACK": "../readme_manager/partials/documentation_and_stack.md",
    "TECHNOLOGY QNA": "../readme_manager/partials/technology_qna.md",
    "DEMO": "../readme_manager/partials/demo.md",
    "INSTALLATION": "../readme_manager/partials/installation.md",
    "DJANGO_COMMANDS": "../readme_manager/partials/django_commands.md",
    "NGINX_SERVER": "../readme_manager/partials/nginx_server.md",

    # Project-Specific Core Files
    "env.example": "../env.example",
    "docker-compose.yml": "../docker-compose.yml",
    "Dockerfile": "../Dockerfile",
    "Jenkinsfile": "../Jenkinsfile",
}
```

Also, remember if you want to include new files, you need to change the `baseREADME` file and the `include_files` array in the `common_readme` repository itself.

## Deployment on AWS EC2/ Home Server Ubuntu 22.0 LTS/ Hostinger VPS Server

Previously This project was hosted on Heroku, but so I started hosting this and all other projects in a 
Single EC2 Machine, which cost me a lot, so now I have shifted all the projects to my own Home Server with 
Ubuntu 22.0 LTS Server, except for portfolio project at https://www.arpansahu.me along with Nginx 


Now there is an EC2 server running with an nginx server and arpansahu.me portfolio
Nginx forwarded https://arpansahu.me/ to the Home Server 

Multiple Projects are running inside dockers so all projects are dockerized.
You can refer to all projects at https://www.arpansahu.me/projects

Every project has a different port on which it runs predefined inside Dockerfile and docker-compose.yml

![EC2 and Home Server along with Nginx, Docker and Jenkins Arrangement](https://github.com/arpansahu/common_readme/blob/main/Images/ec2_and_home_server.png)

Note: Update as of Aug 2023, I have decided to make some changes to my lifestyle, and from now I will be constantly on the go
 from my experience with running a free EC2 server for arpansahu. me and nginx in it and then using another home server
 with all the other projects hosted, my experience was
      
 1. Downtime due to Broadband Service Provider Issues
 2. Downtime due to Weather Sometimes
 3. Downtime due to Machine Breakdown
 4. Downtime due to Power Cuts (even though I had an inverted battery setup for my room)
 5. Remotely it would be harder to fix these problems 

 and due to all these reasons I decided to shift all the projects to a single EC2 Server, at first I was using t2.medium which costs more than 40$ a month 
 then I switched to t2.small and it only costs you 15$ if we take pre-paid plans prices can be slashed much further. 

 Then again I shifted to Hostinger VPS which was more cost-friendly than EC2 Server. On Jan 2024

Now My project arrangements look something similar to this

![EC2 Sever along with Nginx, Docker and Jenkins Arrangement](https://github.com/arpansahu/common_readme/blob/main/Images/One%20Server%20Configuration%20for%20arpanahuone.png)


### Step 1: Dockerize

#### Installing Redis Commander

Reference: https://docs.docker.com/engine/install/ubuntu/

1. Setting up the Repository
   1. Update the apt package index and install packages to allow apt to use a repository over HTTPS: 

       ```bash
       sudo apt-get update
    
       sudo apt-get install \
       ca-certificates \
       curl \
       gnupg \
       lsb-release
       ```

   2. Add Docker’s official GPG key:

       ```bash
       sudo mkdir -p /etc/apt/keyrings
       
       curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
       ```

   3. Use the following command to set up the repository:

       ```bash
       echo \
         "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
         $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       ```

2. Install Docker Engine
    
   1. Update the apt package index:

      ```bash
       sudo apt-get update
      ```
    
      1. Receiving a GPG error when running apt-get update?

         Your default umask may be incorrectly configured, preventing detection of the repository public key file. Try granting read permission for the Docker public key file before updating the package index:
         
            ```bash
            sudo chmod a+r /etc/apt/keyrings/docker.gpg
            sudo apt-get update
            ```
            
   2. Install Docker Engine, containerd, and Docker Compose.

        ```bash
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
        ```

   3. Verify that the Docker Engine installation is successful by running the hello-world image:

        ```bash
         sudo docker run hello-world
        ```

Now in your Git Repository

Create a file named Dockerfile with no extension and add following lines in it

```bash
FROM python:3.10.7

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8002

CMD python manage.py collectstatic
CMD gunicorn --bind 0.0.0.0:8002 great_chat.wsgi
```

Create a file named docker-compose.yml and add following lines in it

```bash
version: '3'

services:
  web:
    build: .
    env_file: ./.env
    command: bash -c "python manage.py makemigrations && python manage.py migrate && daphne -b 0.0.0.0 -p 8002 great_chat.asgi:application"
    container_name: great_chat
    volumes:
      - .:/great_chat
    ports:
      - "8002:8002"
    restart: unless-stopped
```

### **What is Difference in Dockerfile and docker-compose.yml?**

A Dockerfile is a simple text file that contains the commands a user could call to assemble an image whereas Docker Compose is a tool for defining and running multi-container Docker applications.

Docker Compose define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment. It gets an app running in one command by just running docker-compose up. Docker compose uses the Dockerfile if you add the build command to your project’s docker-compose.yml. Your Docker workflow should be to build a suitable Dockerfile for each image you wish to create, then use compose to assemble the images using the build command.

Running Docker 

```bash
docker compose up --build --detach 
```

--detach tag is for running the docker even if terminal is closed
if you remove this tag it will be attached to terminal, and you will be able to see the logs too

--build tag with docker compose up will force image to be rebuild every time before starting the container

### Step2: Serving the requests from Nginx

#### Installing the Nginx server

```bash
sudo apt-get install nginx
```

Starting Nginx and checking its status 

```bash
sudo systemctl start nginx
sudo systemctl status nginx
```

#### Modify DNS Configurations

Add these two records to your DNS Configurations

```bash
A Record	*	0.227.49.244 (public IP of ec2)	Automatic
A Record	@	0.227.49.244 (public IP of ec2)	Automatic
```

Note: now you will be able to see nginx running page if you open the public IP of the machine
IP
Make Sure your EC2 security Group have these entry inbound rules 

```bash
random-hash-id	IPv4	HTTP	TCP	80	0.0.0.0/0	–
```

Open a new Nginx Configuration file name can be anything i am choosing arpansahu since my domain is arpansahu.me. there is already a default configuration file but we will leave it like that only

```bash
sudo vi /etc/nginx/sites-available/arpansahu
```

paste this content in the above file

```bash
server_tokens               off;
access_log                  /var/log/nginx/supersecure.access.log;
error_log                   /var/log/nginx/supersecure.error.log;

server {
  server_name               arpansahu.me;        
  listen                    80;
  location / {
    proxy_pass              http://{ip_of_home_server/localhost}:8000;
    proxy_set_header        Host $host;
  }
}
```

This single Nginx File will be hosting all the multiple projects which I have listed before also.

Checking if the configurations file is correct

```bash
sudo service nginx configtest /etc/nginx/sites-available/arpansahu
```

Now you need to symlink this file to the sites-enabled directory:

```bash
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/arpansahu
```

Restarting Nginx Server 

```bash
sudo systemctl restart nginx
```

Now it's time to enable HTTPS for this server

### Step 3: Enabling HTTPS 

1. Base Domain:  Enabling HTTPS for base domain only or a single subdomain

    To allow visitors to access your site over HTTPS, you’ll need an SSL/TLS certificate that sits on your web server. Certificates are issued by a Certificate Authority (CA). We’ll use a free CA called Let’s Encrypt. To install the certificate, you can use the Certbot client, which gives you an utterly painless step-by-step series of prompts.
    Before starting with Certbot, you can tell Nginx up front to disable TLS versions 1.0 and 1.1 in favour of versions 1.2 and 1.3. TLS 1.0 is end-of-life (EOL), while TLS 1.1 contained several vulnerabilities that were fixed by TLS 1.2. To do this, open the file /etc/nginx/nginx.conf. Find the following line:

    Open nginx.conf file end change ssl_protocols 
    
    ```bash
    sudo vi /etc/nginx/nginx.conf
    
    From ssl_protocols TLSv1 TLSv1.1 TLSv1.2; to ssl_protocols TLSv1.2 TLSv1.3;
    ```
    
    Use this command to verify if nginx.conf file is correct or not
    
    ```bash
    sudo nginx -t
    ```
    
    Now you’re ready to install and use Certbot, you can use Snap to install Certbot:
    
    ```bash
    sudo snap install --classic certbot
    sudo ln -s /snap/bin/certbot /usr/bin/certbot
    ```
    
    Now installing certificate
    
    ```bash
    sudo certbot --nginx --rsa-key-size 4096 --no-redirect
    ```
    
    It will ask for the domain name then you can enter your base domain 
    I have generated SSL for arpansahu.me
    
    Then a few questions will be asked answer them all and your SSL certificate will be generated

    Now These lines will be added to your # Nginx configuration: /etc/nginx/sites-available/arpansahu
    
    ```bash
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/www.supersecure.codes/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.supersecure.codes/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
    ```
    
    Redirecting HTTP to HTTPS
    Open the nginx configuration file  and make it like this

    ```bash
    sudo vi /etc/nginx/sites-available/arpansahu
    ```

    ```bash
    server_tokens               off;
    access_log                  /var/log/nginx/supersecure.access.log;
    error_log                   /var/log/nginx/supersecure.error.log;
     
    server {
      server_name               arpansahu.me;
      listen                    80;
      return                    307 https://$host$request_uri;
    }
    
    server {
    
      location / {
        proxy_pass              http://{ip_of_home_server/ localhost}:8000;
        proxy_set_header        Host $host;
        
        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }                          
    ``` 
    
    You can dry run and check whether it's renewal is working or not

    ```bash
    sudo certbot renew --dry-run
    ```
    
    Note: this process was for arpansahu.me and not for all subdomains.
    For all subdomains, we will have to set a wildcard SSL certificate


2. Enabling a Wildcard certificate

    Here we will enable an SSL certificate for all subdomains at once
        
    Run the following Command

    ```bash
    sudo certbot certonly --manual --preferred-challenges dns
    ```
    
    Again you will be asked domain name and here you will use *.arpansahu.me. and second domain you will use is
    arpansahu.me.
    
    Now, you should have a question in your mind about why we are generating SSL for arpansahu.me separately.
    It's because Let's Encrypt does not include a base domain with wildcard certificates for subdomains.

    After running the above command you will see a message similar to this
      
    ```bash
    Saving debug log to /var/log/letsencrypt/letsencrypt.log
    Please enter the domain name(s) you would like on your certificate (comma and/or
    space separated) (Enter 'c' to cancel): *.arpansahu.me
    Requesting a certificate for *.arpansahu.me
    
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Please deploy a DNS TXT record under the name:
    
    _acme-challenge.arpansahu.me.
    
    with the following value:
    
    dpWCxvq3mARF5iGzSfaRNXwmdkUSs0wgsTPhSaX1gK4
    
    Before continuing, verify the TXT record has been deployed. Depending on the DNS
    provider, this may take some time, from a few seconds to multiple minutes. You can
    check if it has finished deploying with the aid of online tools, such as Google
    Admin Toolbox: https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.arpansahu.me.
    Look for one or more bolded line(s) below the line '; ANSWER'. It should show the
    value(s) you've just added.
   
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue
    ```
   
    You will be given a DNS challenge called ACME challenger you have to create a DNS TXT record in DNS.
    Similar to the below record.
        
    ```bash
    TXT Record  _acme-challenge dpWCxvq3mARF5iGzSfaRNXwmdkUSs0wgsTPhSaX1gK4 5 Automatic
    ```
    
    Now, use this URL to verify whether records are updated or not

    https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.arpansahu.me (arpansahu.me is domain)

    If it's verified then press enter the terminal as mentioned above
        
    Then your certificate will be generated

    ```bash
    Successfully received a certificate.
    The certificate is saved at: /etc/letsencrypt/live/arpansahu.me-0001/fullchain.pem            (use this in your nginx configuration file)
    Key is saved at:         /etc/letsencrypt/live/arpansahu.me-0001/privkey.pem
    This certificate expires on 2023-01-20.
    These files will be updated when the certificate is renewed.
    ```
        
    You can notice here, the certificate generated is arpansahu.me-0001 and not arpansahu.me
    because we already generated a certificate named arpansahu.me
        
    So remember to delete it before generating this wildcard certificate
    using command

    ```bash
    sudo certbot delete
    ```
        
    Note: This certificate will not be renewed automatically. Auto-renewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same Certbot command before the certificate's expiry date.

3. Generating Wildcard SSL certificate and Automating its renewal

    1. Modify your ec2 inbound rules 
    
      ```bash
      –	sgr-0219f1387d28c96fb	IPv4	DNS (TCP)	TCP	53	0.0.0.0/0	–	
      –	sgr-01b2b32c3cee53aa9	IPv4	SSH	TCP	22	0.0.0.0/0	–
      –	sgr-0dfd03bbcdf60a4f7	IPv4	HTTP	TCP	80	0.0.0.0/0	–
      –	sgr-02668dff944b9b87f	IPv4	HTTPS	TCP	443	0.0.0.0/0	–
      –	sgr-013f089a3f960913c	IPv4	DNS (UDP)	UDP	53	0.0.0.0/0	–
      ```
    
   2. Install acme-dns Server

      * Create a folder for acme-dns and change the directory

        ```bash
         sudo mkdir /opt/acme-dns
         cd !$
        ```

      * Download and extract tar with acme-dns from GitHub

        ```bash
        sudo curl -L -o acme-dns.tar.gz \
        https://github.com/joohoi/acme-dns/releases/download/v0.8/acme-dns_0.8_linux_amd64.tar.gz
        sudo tar -zxf acme-dns.tar.gz
        ```

      * List files

        ```bash
        sudo ls
        ```

      * Clean Up

        ```bash
        sudo rm acme-dns.tar.gz
        ```

      * Create a soft link

        ```bash
        sudo ln -s \
        /opt/acme-dns/acme-dns /usr/local/bin/acme-dns
        ```

      * Create a minimal acme-dns user

         ```bash
         sudo adduser \
         --system \	
         --gecos "acme-dns Service" \
         --disabled-password \
         --group \
         --home /var/lib/acme-dns \
         acme-dns
        ```

      * Update default acme-dns config compared with IP from the AWS console. Can't bind to the public address need to use private one.

        ```bash
        IP addr
	  
        sudo mkdir -p /etc/acme-dns
	  
        sudo mv /opt/acme-dns/config.cfg /etc/acme-dns/
	  
        sudo vim /etc/acme-dns/config.cfg
        ```
      
      * Replace

        ```bash
        listen = "127.0.0.1:53” to listen = “private IP of the ec2 instance” 172.31.93.180:53(port will be 53)
 
        Similarly, Edit other details mentioned below  

        # domain name to serve the requests off of
        domain = "auth.arpansahu.me"
        # zone name server
        nsname = "auth.arpansahu.me"
        # admin email address, where @ is substituted with .
        nsadmin = "admin@arpansahu.me"


        records = [
          # domain pointing to the public IP of your acme-dns server
           "auth.arpansahu.me. A 44.199.177.138. (public elastic IP)”,
          # specify that auth.example.org will resolve any *.auth.example.org records
           "auth.arpansahu.me. NS auth.arpansahu.me.”,
        ]
	
        [api]
        # listen IP eg. 127.0.0.1
        IP = "127.0.0.1”. (Changed)

        # listen port, eg. 443 for default HTTPS
        port = "8080" (Changed).         ——— We will use port 8090 because we will also use Jenkins which will be running on 8080 port
        # possible values: "letsencrypt", "letsencryptstaging", "cert", "none"
        tls = "none"   (Changed)

        ```

      * Move the systemd service and reload

        ```bash
        cat acme-dns.service
     
        sudo mv \
        acme-dns.service /etc/systemd/system/acme-dns.service
	  
        sudo systemctl daemon-reload
        ```

      * Start and enable acme-dns server

        ```bash
        sudo systemctl enable acme-dns.service
        sudo systemctl start acme-dns.service
        ```

      * Check acme-dns for possible errors

        ```bash
        sudo systemctl status acme-dns.service
        ```

      * Use journalctl to debug in case of errors

         ```bash
         journalctl --unit acme-dns --no-pager --follow
         ```

      * Create A record for your domain

         ```bash
         auth.arpansahu.me IN A <public-IP>
         ```

      * Create NS record for auth.arpansahu.me pointing to auth.arpansahu.me. This means, that auth.arpansahu.me is
        responsible for any *.auth.arpansahu.me records

        ```bash
        auth.arpansahu.me IN NS auth.arpansahu.me
        ```

      * Your DNS record will be looking like this

        ```bash
        A Record	auth	44.199.177.138	Automatic	
        NS Record	auth	auth.arpansahu.me.	Automatic
        ```

      * Test acme-dns server (Split the screen)

        ```bash
        journalctl -u acme-dns --no-pager --follow
        ```

      * From the local host try to resolve the random DNS record

        ```bash
        dig api.arpansahu.me
        dig api.auth.arpansahu.me
        dig 7gvhsbvf.auth.arpansahu.me
        ``` 
        
   3. Install acme-dns-client 

     ```bash
     sudo mkdir /opt/acme-dns-client
     cd !$
    
     sudo curl -L \
     -o acme-dns-client.tar.gz \
     https://github.com/acme-dns/acme-dns-client/releases/download/v0.2/acme-dns-client_0.2_linux_amd64.tar.gz
    
     sudo tar -zxf acme-dns-client.tar.gz
     ls
     sudo rm acme-dns-client.tar.gz
     sudo ln -s \
     /opt/acme-dns-client/acme-dns-client /usr/local/bin/acme-dns-client 
     ```

   4. Install Certbot

     ```bash
     cd
     sudo snap install core; sudo snap refresh core
     sudo snap install --classic certbot
     sudo ln -s /snap/bin/certbot /usr/bin/certbot
     ```

    Note: you can skip this step if Certbot is already installed

    5. Get Letsencrypt Wildcard Certificate
       * Create a new acme-dns account for your domain and set it up

         ```bash
         sudo acme-dns-client register \
         -d arpansahu.me -s http://localhost:8090
         ```

        The above command is old now we will use the new command 

         ```bash
         sudo acme-dns-client register \
          -d arpansahu.me \
          -allow 0.0.0.0/0 \
          -s http://localhost:8080
         ```

         Note: When we edited acme-dns config file there we mentioned the port 8090 and thats why we are using this port here also
         
       * Creating Another DNS Entry 

         ```bash
         CNAME Record	_acme-challenge	e6ac0f0a-0358-46d6-a9d3-8dd41f44c7ec.auth.arpansahu.me.	Automatic
         ```

        Since the last update in  the last step now two more entries should be added 

         ```bash
         CAA Record @	0 issuewild "letsencrypt.org; validationmethods=dns-01; accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/1424899626"  Automatic

         CAA Record @	0 issue "letsencrypt.org; validationmethods=dns-01; accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/1424899626"
         Automatic
         ```

        Same as an entry that needs to be added to complete a time challenge as previously we did.
       * Check whether the entry is added successfully or not

         ```bash
         dig _acme-challenge.arpansahu.me
         ```

       * Get a wildcard certificate

         ```bash
         sudo certbot certonly \
         --manual \
         --test-cert \ 
         --preferred-challenges dns \ 
         --manual-auth-hook 'acme-dns-client' \ 
         -d ‘*.arpansahu.me’ -d arpansahu.me
         ```

        Note: Here we have to mention both the base and wildcard domain names with -d since let's encrypt don't provide base domain ssl by default in wildcard domain ssl
       
       * Verifying the certificate

         ```bash
         sudo openssl x509 -text -noout \
         -in /etc/letsencrypt/live/arpansahu.me/fullchain.pem
         ```

       * Renew certificate (test)

         ```bash
         sudo certbot renew \
         --manual \ 
         --test-cert \ 
         --dry-run \ 
         --preferred-challenges dns \
         --manual-auth-hook 'acme-dns-client'       
         ```
         
       * Renew certificate (actually)

         ```bash
         sudo certbot renew \
         --manual \
         --preferred-challenges dns \
         --manual-auth-hook 'acme-dns-client'       
         ```

       * Check the entry is added successfully or not

         ```bash
         dig _acme-challenge.arpansahu.me
         ```

    6. Setup Auto-Renew for Letsencrypt WILDCARD Certificate
       * Setup cronjob

         ```bash
         sudo crontab -e
         ```

       * Add the following lines to the file

         ```bash
         0 */12 * * * certbot renew --manual --test-cert --preferred-challenges dns --manual-auth-hook 'acme-dns-client'
         ```

After all these steps your Nginx configuration file located at /etc/nginx/sites-available/arpansahu will be looking similar to this

```bash
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

### Installing Jenkins

Reference: https://www.jenkins.io/doc/book/installing/linux/

Jenkins requires Java to run, yet certain distributions don’t include this by default and some Java versions are incompatible with Jenkins.

There are multiple Java implementations which you can use. OpenJDK is the most popular one at the moment, we will use it in this guide.

Update the Debian apt repositories, install OpenJDK 11, and check the installation with the commands:

```bash
sudo apt update

sudo apt install openjdk-11-jre

java -version
openjdk version "11.0.12" 2021-07-20
OpenJDK Runtime Environment (build 11.0.12+7-post-Debian-2)
OpenJDK 64-Bit Server VM (build 11.0.12+7-post-Debian-2, mixed mode, sharing)
```

Long Term Support release

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

Start Jenkins

```bash
sudo systemctl enable jenkins
```

You can start the Jenkins service with the command:

```bash
sudo systemctl start jenkins
```

You can check the status of the Jenkins service using the command:

```bash
sudo systemctl status jenkins
```

Now for serving the Jenkins UI from Nginx add the following lines to the Nginx file located at 
/etc/nginx/sites-available/arpansahu by running the following command

```bash
sudo vi /etc/nginx/sites-available/arpansahu
```

* Add these lines to it.

    ```bash
    server {
        listen         80;
        server_name    jenkins.arpansahu.me;
        # force https-redirects
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
            }
    
        location / {
             proxy_pass              http://{ip_of_home_server}:8080;
             proxy_set_header        Host $host;
             proxy_set_header    X-Forwarded-Proto $scheme;
        }
    
        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }
    ```

You can add all the server blocks to the same nginx configuration file
just make sure you place the server block for the base domain at the last

* To copy .env from the local server directory while building image

add Jenkins ALL=(ALL) NOPASSWD: ALL
inside /etc/sudoers file

and then put 

```bash
stage('Dependencies') {
            steps {
                script {
                    sh "sudo cp /root/env/project_name/.env /var/lib/jenkins/workspace/pipeline_project_name"
                }
            }
        }
```

in Jenkinsfile




* Now Create a file named Jenkinsfile at the root of Git Repo and add following lines to file

```bash
pipeline {
    agent { label 'local' }
    stages {
        stage('Initialize') {
            steps {
                script {
                    // Log the current workspace path
                    echo "Current workspace path is: ${env.WORKSPACE}"
                }
            }
        }
        stage('Checkout') {
            steps {
                // Checkout code from SCM
                checkout scm
            }
        }
        stage('Dependencies') {
            steps {
                script {
                    // Copy .env file to the workspace
                    sh "sudo cp /root/projectenvs/great_chat/.env ${env.WORKSPACE}/"
                }
            }
        }
        stage('Production') {
            when {
                expression {
                    // Collect all changed files
                    def changes = currentBuild.changeSets.collect { it.items.collect { it.affectedFiles.collect { it.path } } }.flatten()

                    // Define the file(s) to be excluded from triggering a deploy
                    def excludedFiles = ['Readme.md']

                    // Check if the only changed files are in the excluded list
                    def onlyExcludedFilesChanged = changes.every { changedFile -> 
                        excludedFiles.contains(changedFile)
                    }

                    // Proceed with deployment if not only excluded files are changed
                    return !onlyExcludedFilesChanged
                }
            }
            steps {
                script {
                    // Deploy using Docker Compose
                    sh "docker compose up --build --detach"
                    
                    // Set a flag to indicate deployment execution
                    currentBuild.description = 'DEPLOYMENT_EXECUTED'
                }
            }
        }
    }
    post {
        success {
            script {
                if (currentBuild.description == 'DEPLOYMENT_EXECUTED') {
                    // Send success notification email
                    sh """curl -s \
                    -X POST \
                    --user $MAIL_JET_API_KEY:$MAIL_JET_API_SECRET \
                    https://api.mailjet.com/v3.1/send \
                    -H "Content-Type:application/json" \
                    -d '{
                        "Messages":[
                                {
                                        "From": {
                                                "Email": "$MAIL_JET_EMAIL_ADDRESS",
                                                "Name": "ArpanSahuOne Jenkins Notification"
                                        },
                                        "To": [
                                                {
                                                        "Email": "$MY_EMAIL_ADDRESS",
                                                        "Name": "Development Team"
                                                }
                                        ],
                                        "Subject": "${currentBuild.fullDisplayName} deployed successfully",
                                        "TextPart": "Hola Development Team, your project ${currentBuild.fullDisplayName} is now deployed",
                                        "HTMLPart": "<h3>Hola Development Team, your project ${currentBuild.fullDisplayName} is now deployed </h3> <br> <p> Build Url: ${env.BUILD_URL}  </p>"
                                }
                        ]
                    }'"""
                    // Trigger another Jenkins job
                    build job: 'common_readme', parameters: [string(name: 'project_git_url', value: 'https://github.com/arpansahu/great_chat'), string(name: 'environment', value: 'prod')], wait: false
                }
            }
        }
        failure {
            script {
                // Send failure notification email
                sh """curl -s \
                -X POST \
                --user $MAIL_JET_API_KEY:$MAIL_JET_API_SECRET \
                https://api.mailjet.com/v3.1/send \
                -H "Content-Type:application/json" \
                -d '{
                    "Messages":[
                            {
                                    "From": {
                                            "Email": "$MAIL_JET_EMAIL_ADDRESS",
                                            "Name": "ArpanSahuOne Jenkins Notification"
                                    },
                                    "To": [
                                            {
                                                    "Email": "$MY_EMAIL_ADDRESS",
                                                    "Name": "Development Team"
                                            }
                                    ],
                                    "Subject": "${currentBuild.fullDisplayName} deployment failed",
                                    "TextPart": "Hola Development Team, your project ${currentBuild.fullDisplayName} deployment failed",
                                    "HTMLPart": "<h3>Hola Development Team, your project ${currentBuild.fullDisplayName} is not deployed, Build Failed </h3> <br> <p> Build Url: ${env.BUILD_URL}  </p>"
                            }
                    ]
                }'"""
            }
        }
    }
}
```

Note: agent {label 'local'} is used to specify which node will execute the jenkins job deployment. So local linux server is labelled with 'local' are the project with this label will be executed in local machine node.

* Configure a Jenkins project from jenkins ui located at https://jenkins.arpansahu.me

Make sure to use Pipeline project and name it whatever you want I have named it as great_chat

![Jenkins Pipeline Configuration](/Jenkins.png)

In this above picture you can see credentials right? you can add your github credentials
from Manage Jenkins on home Page --> Manage Credentials

and add your GitHub credentials from there

* Add a .env file to you project using following command (This step is no more required stage('Dependencies'))

    ```bash
    sudo vi  /var/lib/jenkins/workspace/great_chat/.env
    ```

    Your workspace name may be different.

    Add all the env variables as required and mentioned in the Readme File.

* Add Global Jenkins Variables from Dashboard --> Manage --> Jenkins
  Configure System
 
  * MAIL_JET_API_KEY
  * MAIL_JET_API_SECRET
  * MAIL_JET_EMAIL_ADDRESS
  * MY_EMAIL_ADDRESS

Now you are good to go.

## Postgresql Server

IT would be a nightmare to have your own vps to save cost and not hosting your own postgresql server.

For more information, see the ### Installing PostgreSql

1. Update the package list to make sure you have the latest information

    ```bash
    sudo apt update
    ```

2. Install the PostgreSQL package

    ```bash
    sudo apt install postgresql postgresql-contrib
    ```

3. PostgreSQL should now be installed on your server. By default, PostgreSQL creates a user named `postgres` with administrative privileges. You can switch to this user to perform administrative tasks:

    ```bash
    sudo -i -u postgres
    ```

4. Access the PostgreSQL interactive terminal by running:

    ```bash
    psql
    ```

5. Set a password for the `postgres` user:

    ```sql
    ALTER USER postgres WITH PASSWORD 'your_password';
    ```

   Replace `'your_password'` with the desired password.

6. Exit the PostgreSQL shell:

    ```sql
    \q
    ```

7. Exit the `postgres` user session:

    ```bash
    exit
    ```

Now, PostgreSQL is installed on your Ubuntu server. You can access the PostgreSQL database by logging in with the `postgres` user and the password you set.

Remember to configure your PostgreSQL server according to your security needs, such as modifying the `pg_hba.conf` file to control access, setting up SSL for secure connections, and configuring other PostgreSQL settings as required for your environment.


## Configuring Postgresql

1. open postgresql.conf file

    ```bash
    sudo vi /etc/postgresql/14/main/postgresql.conf
    ```
     
    14 is the version which i have installed your version can be different

2. Find the listen_addresses line and set it to:

    ```bash
    listen_addresses = 'localhost'
    ```

    Now the thing is if u don't want to serve it using nginx u can also set it to * all so that database can be connected from any where

3. 	Edit pg_hba.conf to allow connections:

    ```bash
    sudo nano /etc/postgresql/14/main/pg_hba.conf
    ```

    14 is the version which i have installed your version can be different

4. 	Add the following line in the end:

    ```bash
    host    all             all             127.0.0.1/32            md5
    ```

    if u want to use without nginx

    ```bash
    host    all             all             0.0.0.0/0            md5
    ```

    I have added both 

5. Restart PostgreSQL to apply changes:

    ```bash
    sudo systemctl restart postgresql
    ```

## Configuring Nginx as Reverse proxy

Note: In previous steps we have already seen how to setup the reverse proxy with Nginx for Django projects and installation process and everything

1.	Install the nginx-extras package to support the stream module:

    ```bash
    sudo apt install nginx-extras
    ````

2.	Add a stream configuration file for the PostgreSQL stream:

    ```bash
    sudo vi /etc/nginx/nginx.conf
    ```

    1.	Add the following configuration:

    ```bash
    stream {
        upstream postgresql_upstream {
            server 127.0.0.1:5432;  # PostgreSQL server
        }

        server {
            listen 9550 ssl;  # Use SSL on port 443
            proxy_pass postgresql_upstream;

            ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem;  # SSL certificate
            ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem;  # SSL certificate key
            ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;  # SSL DH parameters
            include /etc/letsencrypt/options-ssl-nginx.conf;  # SSL options

            proxy_timeout 600s;
            proxy_connect_timeout 600s;
        }
    }
    ```

    Since i have generated ssl certs already in nginx setup i am using those certificates here itself

    2. 	Test the Nginx Configuration:

    ```bash
    sudo nginx -t
    ```

    If error comes nginx: [emerg] "stream" directive is not allowed here in /etc/nginx/conf.d/postgresql.conf:1
    nginx: configuration file /etc/nginx/nginx.conf test failed    

    Follow these steps: 

        0.	Remove the custom configuration file:

            ```bash
            sudo rm /etc/nginx/conf.d/postgresql.conf
            ```

        1.	Open the main Nginx configuration file: 

            ```bash
            sudo nano /etc/nginx/nginx.conf
            ```

        2.	Add the Stream Block at the Appropriate Place
        Add the following stream block at the end of the nginx.conf file, or within the appropriate context:

            ```bash
            user www-data;
            worker_processes auto;
            pid /run/nginx.pid;
            include /etc/nginx/modules-enabled/*.conf;

            events {
                worker_connections 768;
            }

            http {
                sendfile on;
                tcp_nopush on;
                tcp_nodelay on;
                keepalive_timeout 65;
                types_hash_max_size 2048;

                include /etc/nginx/mime.types;
                default_type application/octet-stream;

                access_log /var/log/nginx/access.log;
                error_log /var/log/nginx/error.log;

                gzip on;
                gzip_disable "msie6";

                include /etc/nginx/conf.d/*.conf;
                include /etc/nginx/sites-enabled/*;
            }

            stream {
                upstream postgresql_upstream {
                    server 127.0.0.1:5432;  # PostgreSQL server
                }

                server {
                    listen 9550 ssl;  # Use SSL on port different 443
                    proxy_pass postgresql_upstream;

                    ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem;  # SSL certificate
                    ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem;  # SSL certificate key
                    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;  # SSL DH parameters
                    include /etc/letsencrypt/options-ssl-nginx.conf;  # SSL options

                    proxy_timeout 600s;
                    proxy_connect_timeout 600s;
                }
            }
            ```
        
        3.	Test the Nginx Configuration
        
            ```bash
            sudo nginx -t
            ```

    3. Reload Nginx to apply the new configuration:

    ```bash
    sudo systemctl reload nginx
    ```

3. Testing connecting with postgres without ip and using domain

    ```bash
    psql "postgres://username:password@domain/database_name?sslmode=require"
    ```

    (https://github.com/arpansahu/common_readme/blob/main/AWS%20Deployment/Postgres.md).

postgresql_server can be access accessed

```bash
psql "postgres://user:user_pass@arpansahu.me/database_name?sslmode=require"
```

# Services on AWS EC2/ Home Server Ubuntu 22.0 LTS s

## PGAdmin4

pgAdmin 4 is a complete rewrite of pgAdmin, built using Python and Javascript/jQuery. A desktop runtime written in NWjs allows it to run standalone for individual users, or the web application code may be deployed directly on a web server for use by one or more users through their web browser. 

### Installing PgAdmin

1. **Create a Virtual Environment:**

   It's good practice to use virtual environments to isolate your project's dependencies. This helps avoid conflicts with system packages. You can create a virtual environment like this:

   ```bash
   python3 -m venv pgadmin_venv
   source pgadmin_venv/bin/activate
   ```

2. **Install pgAdmin 4:**

   Once you are in the virtual environment, install pgAdmin 4:

   ```bash
   pip install pgadmin4
   ```

   If you encounter any dependency conflicts, the virtual environment will help isolate the packages.

3. **Run pgAdmin 4:**

   After installing, try running pgAdmin 4:

   ```bash
   pgadmin4
   ```

    To ensure pgAdmin runs in the background, use `nohup`:

    ```bash
    nohup pgadmin4 &>/dev/null &
    ```
    
By using a virtual environment, you avoid potential conflicts with system packages, and you can manage dependencies for pgAdmin 4 more effectively.

Remember to activate your virtual environment whenever you want to run pgAdmin 4:

```bash
source pgadmin_venv/bin/activate
pgadmin4
```

And deactivate it when you're done:

```bash
deactivate
```



4. Edit Host from 127.0.0.1 tto 0.0.0.0

```bash
vi /root/pgadmin_venv/lib/python3.10/site-packages/pgadmin4/config.py
```


### Configuring Nginx as Reverse proxy

1. Edit Nginx Configuration

    ```bash
    sudo vi /etc/nginx/sites-available/arpansahu
    ```

2. Add this server configuration

    ```bash
    server {
        listen         80;
        server_name    pgadmin.arpansahu.me;
        # force https-redirects
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
            }

        location / {
            proxy_pass              http://0.0.0.0:9997;
            proxy_set_header        Host $host;
            proxy_set_header    X-Forwarded-Proto $scheme;
        }

        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }
    ```

3. Test the Nginx Configuration

    ```bash
    sudo nginx -t
    ```

4. Reload Nginx to apply the new configuration

    ```bash
    sudo systemctl reload nginx
    ```

### Conclusion

This approach should help you manage the dependencies and resolve the version conflicts more effectively while ensuring pgAdmin runs in the background and is accessible via Nginx as a reverse proxy.


My PGAdmin4 can be accessed here : https://pgadmin.arpansahu.me/

## Portainer
   
Portainer is a web UI to manage your docker, and kubernetes. Portainer consists of two elements, the Portainer Server, and the Portainer Agent. Both elements run as lightweight Docker containers on a Docker engine.

### Installing Portainer

1. **Create a Docker Volume for Portainer Data (optional but recommended):**
   This step is optional but recommended as it allows you to persist Portainer's data across container restarts.

    ```bash
    docker volume create portainer_data
    ```

2. **Run Portainer Container:**
   Run the Portainer container using the following command. Replace `/var/run/docker.sock` with the path to your Docker socket if it's in a different location.

    ```bash
    docker run -d -p 0.0.0.0:9998:9000 -p 9444:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
    to use it in nginx server configuration
    ```

   This command pulls the Portainer Community Edition image from Docker Hub, creates a persistent volume for Portainer data, and starts the Portainer container. The `-p 9000:9000` option maps Portainer's web interface to port 9000 on your host.

3. **Access Portainer UI:**
   Open your web browser and go to `http://localhost:9000` (or replace `localhost` with your server's IP address if you are using a remote server). You will be prompted to set up an admin user and password.

4. **Connect Portainer to the Docker Daemon:**
   On the Portainer setup page, choose the "Docker" environment, and connect Portainer to the Docker daemon. You can usually use the default settings (`unix:///var/run/docker.sock` for the Docker API endpoint).

5. **Complete Setup:**
   Follow the on-screen instructions to complete the setup process. You may choose to deploy a local agent for better performance, but it's not required for basic functionality.

Once the setup is complete, you should have access to the Portainer dashboard, where you can manage and monitor your Docker containers, images, volumes, and networks through a user-friendly web interface.

Keep in mind that the instructions provided here assume a basic setup. For production environments, it's recommended to secure the Portainer instance, such as by using HTTPS and setting up authentication. Refer to the [Portainer documentation](https://documentation.portainer.io/) for more advanced configurations and security considerations.


### Configuring Nginx as Reverse proxy

1. Edit Nginx Configuration

    ```bash
    sudo vi /etc/nginx/sites-available/arpansahu
    ```

2. Add this server configuration

    ```bash
    server {
        listen         80;
        server_name    portainer.arpansahu.me;
        # force https-redirects
        if ($scheme = http) {
            return 301 https://$server_name$request_uri;
            }

        location / {
            proxy_pass              http://0.0.0.0:9998;
            proxy_set_header        Host $host;
            proxy_set_header    X-Forwarded-Proto $scheme;
        }

        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }
    ```

3. Test the Nginx Configuration

    ```bash
    sudo nginx -t
    ```

4. Reload Nginx to apply the new configuration

    ```bash
    sudo systemctl reload nginx
    ```

My Portainer can be accessed here : https://portainer.arpansahu.me/

## Redis Server

Redis is versatile and widely used for its speed and efficiency in various applications. Its ability to serve different roles, such as caching, real-time analytics, and pub/sub messaging, makes it a valuable tool in many technology stacks.

### Installing Redis

1. **Create a Docker Volume for Portainer Data (optional but recommended):**
   This step is optional but recommended as it allows you to persist Portainer's data across container restarts.

    ```bash
    docker volume create portainer_data
    ```

2. **Run Portainer Container:**
   Run the Portainer container using the following command. Replace `/var/run/docker.sock` with the path to your Docker socket if it's in a different location.

    ```bash
    docker run -d -p 0.0.0.0:9998:9000 -p 9444:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
    to use it in nginx server configuration
    ```

   This command pulls the Portainer Community Edition image from Docker Hub, creates a persistent volume for Portainer data, and starts the Portainer container. The `-p 9000:9000` option maps Portainer's web interface to port 9000 on your host.

3. **Access Portainer UI:**
   Open your web browser and go to `http://localhost:9000` (or replace `localhost` with your server's IP address if you are using a remote server). You will be prompted to set up an admin user and password.

4. **Connect Portainer to the Docker Daemon:**
   On the Portainer setup page, choose the "Docker" environment, and connect Portainer to the Docker daemon. You can usually use the default settings (`unix:///var/run/docker.sock` for the Docker API endpoint).

5. **Complete Setup:**
   Follow the on-screen instructions to complete the setup process. You may choose to deploy a local agent for better performance, but it's not required for basic functionality.

Once the setup is complete, you should have access to the Portainer dashboard, where you can manage and monitor your Docker containers, images, volumes, and networks through a user-friendly web interface.

Keep in mind that the instructions provided here assume a basic setup. For production environments, it's recommended to secure the Portainer instance, such as by using HTTPS and setting up authentication. Refer to the [Portainer documentation](https://documentation.portainer.io/) for more advanced configurations and security considerations.

Note: if u want to use ssl connection you can 

/etc/redis/redis.conf open this file and 

```bash
tls-port 6379
port 0

tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-dh-params-file /path/to/dhparam.pem

tls-auth-clients no
```

Add this configuration 

Mostly redis is used as cache and we want it to be super fast hence we are not putting it behind reverse proxy e.g. nginx same as postgres

Also one more thing redis by default don't support ssl connections even if u use ssl

redis serve can be accessed

```bash
redis-cli -h arpansahu.me -p 6379 -a password_required
```

## Redis Commander

Redis Commander is a web-based management tool for Redis databases. It provides a user-friendly interface to interact with Redis, making it easier to manage and monitor your Redis instances.

### Installing Redis

1. **Create a Docker Volume for Portainer Data (optional but recommended):**
   This step is optional but recommended as it allows you to persist Portainer's data across container restarts.

    ```bash
    docker volume create portainer_data
    ```

2. **Run Portainer Container:**
   Run the Portainer container using the following command. Replace `/var/run/docker.sock` with the path to your Docker socket if it's in a different location.

    ```bash
    docker run -d -p 0.0.0.0:9998:9000 -p 9444:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
    to use it in nginx server configuration
    ```

   This command pulls the Portainer Community Edition image from Docker Hub, creates a persistent volume for Portainer data, and starts the Portainer container. The `-p 9000:9000` option maps Portainer's web interface to port 9000 on your host.

3. **Access Portainer UI:**
   Open your web browser and go to `http://localhost:9000` (or replace `localhost` with your server's IP address if you are using a remote server). You will be prompted to set up an admin user and password.

4. **Connect Portainer to the Docker Daemon:**
   On the Portainer setup page, choose the "Docker" environment, and connect Portainer to the Docker daemon. You can usually use the default settings (`unix:///var/run/docker.sock` for the Docker API endpoint).

5. **Complete Setup:**
   Follow the on-screen instructions to complete the setup process. You may choose to deploy a local agent for better performance, but it's not required for basic functionality.

Once the setup is complete, you should have access to the Portainer dashboard, where you can manage and monitor your Docker containers, images, volumes, and networks through a user-friendly web interface.

Keep in mind that the instructions provided here assume a basic setup. For production environments, it's recommended to secure the Portainer instance, such as by using HTTPS and setting up authentication. Refer to the [Portainer documentation](https://documentation.portainer.io/) for more advanced configurations and security considerations.

Note: if u want to use ssl connection you can 

/etc/redis/redis.conf open this file and 

```bash
tls-port 6379
port 0

tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-dh-params-file /path/to/dhparam.pem

tls-auth-clients no
```

Add this configuration 

Mostly redis is used as cache and we want it to be super fast hence we are not putting it behind reverse proxy e.g. nginx same as postgres

Also one more thing redis by default don't support ssl connections even if u use ssl

My Redis Commander can be accessed here : https://redis.arpansahu.me/

## MiniIo (Self hosted S3 Storage)

MinIO is a high-performance, distributed object storage system designed for large-scale data infrastructures. It is open-source and compatible with the Amazon S3 API, making it a popular choice for organizations looking for scalable, secure, and cost-effective storage solutions. 

### Installing Redis

1. **Create a Docker Volume for Portainer Data (optional but recommended):**
   This step is optional but recommended as it allows you to persist Portainer's data across container restarts.

    ```bash
    docker volume create portainer_data
    ```

2. **Run Portainer Container:**
   Run the Portainer container using the following command. Replace `/var/run/docker.sock` with the path to your Docker socket if it's in a different location.

    ```bash
    docker run -d -p 0.0.0.0:9998:9000 -p 9444:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
    to use it in nginx server configuration
    ```

   This command pulls the Portainer Community Edition image from Docker Hub, creates a persistent volume for Portainer data, and starts the Portainer container. The `-p 9000:9000` option maps Portainer's web interface to port 9000 on your host.

3. **Access Portainer UI:**
   Open your web browser and go to `http://localhost:9000` (or replace `localhost` with your server's IP address if you are using a remote server). You will be prompted to set up an admin user and password.

4. **Connect Portainer to the Docker Daemon:**
   On the Portainer setup page, choose the "Docker" environment, and connect Portainer to the Docker daemon. You can usually use the default settings (`unix:///var/run/docker.sock` for the Docker API endpoint).

5. **Complete Setup:**
   Follow the on-screen instructions to complete the setup process. You may choose to deploy a local agent for better performance, but it's not required for basic functionality.

Once the setup is complete, you should have access to the Portainer dashboard, where you can manage and monitor your Docker containers, images, volumes, and networks through a user-friendly web interface.

Keep in mind that the instructions provided here assume a basic setup. For production environments, it's recommended to secure the Portainer instance, such as by using HTTPS and setting up authentication. Refer to the [Portainer documentation](https://documentation.portainer.io/) for more advanced configurations and security considerations.

Note: if u want to use ssl connection you can 

/etc/redis/redis.conf open this file and 

```bash
tls-port 6379
port 0

tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-dh-params-file /path/to/dhparam.pem

tls-auth-clients no
```

Add this configuration 

Mostly redis is used as cache and we want it to be super fast hence we are not putting it behind reverse proxy e.g. nginx same as postgres

Also one more thing redis by default don't support ssl connections even if u use ssl

You can connect to my MiniIo Server using terminal 
```bash
  mc alias set myminio https://arpansahu.me api_key api_secret --api S3v4
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
[![Heroku](https://img.shields.io/badge/-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/)
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white)](https://www.jenkins.io/)
[![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://nginx.org/en/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

SECRET_KEY=

DEBUG=

ALLOWED_HOSTS=

MAIL_JET_API_KEY=

MAIL_JET_API_SECRET=

MY_EMAIL_ADDRESS=

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_STORAGE_BUCKET_NAME=

BUCKET_TYPE=

DOMAIN=

PROTOCOL=

DATABASE_URL=

REDISCLOUD_URL=


