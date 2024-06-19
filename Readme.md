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

## Deployment on AWS EC2/ Home Server Ubuntu 22.0 LTS/ Hostinger VPS Server

Previously This project was hosted on Heroku, but so I started hosting this and all other projects in a 
Single EC2 Machine, which costed me a lot, so now I have shifted all the projects into my own Home Server with 
Ubuntu 22.0 LTS Server, except for portfolio project at https://www.arpansahu.me along with Nginx 


Now there is EC2 server running with a nginx server and arpansahu.me portfolio
Nginx forward https://arpansahu.me/ to Home Server 

Multiple Projects are running inside dockers so all projects are dockerized.
You can refer to all projects on https://www.arpansahu.me/projects

Every project have different port on which its running predefined inside Dockerfile and docker-compose.yml

![EC2 and Home Server along with Nginx, Docker and Jenkins Arrangement](https://github.com/arpansahu/common_readme/blob/main/Images/ec2_and_home_server.png)

Note: Update as of Aug 2023, I have decided to make some changes to my lifestyle, and from now i will be constantly on the go
      from my past experience with running free EC2 server for arpansahu.me and nginx in it and then using another home server
      with all the other projects hosted, my experience was
      
      1. Downtime due to Broadband Service Provider Issues
      2. Downtime due to Weather Sometimes
      3. Downtime due to Machine Breakdown
      4. Downtime due to Power Cuts (even though i had a inverted with battery setup for my room)
      5. Remotely it would be harder to fix these problems 

  and due to all these reasons i decided to shift all the projects to single EC2 Server, at first i was using t2.medium which costs more than 40$ a month 
  then i switched to t2.small and it only costs you 15$ and if we take pre paid plans prices can be slashed much further. 

  Then again i shifted to Hostinger VPS which was more cost friendly then EC2 Server. on Jan 2024

Now My project arrangements looks something similar to this

![EC2 Sever along with Nginx, Docker and Jenkins Arrangement](https://github.com/arpansahu/common_readme/blob/main/Images/One%20Server%20Configuration%20for%20arpanahuone.png)


### Step 1: Dockerizing

# Dockerizing

Installing Docker on Home Server

Reference: https://docs.docker.com/engine/install/ubuntu/

1. Setting up the Repository
   1. Update the apt package index and install packages to allow apt to use a repository over HTTPS: 
       ```
       sudo apt-get update
    
       sudo apt-get install \
       ca-certificates \
       curl \
       gnupg \
       lsb-release
       ```
   2. Add Docker’s official GPG key:

       ```
       sudo mkdir -p /etc/apt/keyrings
    
       curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
       ```

   3. Use the following command to set up the repository:

       ```
       echo \
         "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
         $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
       ```
2. Install Docker Engine
    
   1. Update the apt package index:

      ```
       sudo apt-get update
      ```
    
      1. Receiving a GPG error when running apt-get update?

         Your default umask may be incorrectly configured, preventing detection of the repository public key file. Try granting read permission for the Docker public key file before updating the package index:
            ```
            sudo chmod a+r /etc/apt/keyrings/docker.gpg
            sudo apt-get update
            ```
   2. Install Docker Engine, containerd, and Docker Compose.

        ```
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
        ```
   3. Verify that the Docker Engine installation is successful by running the hello-world image:

        ```
         sudo docker run hello-world
        ```

Now in your Git Repository

Create a file named Dockerfile with no extension and add following lines in it
```
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

```
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
```
docker compose up --build --detach 
```

--detach tag is for running the docker even if terminal is closed
if you remove this tag it will be attached to terminal, and you will be able to see the logs too

--build tag with docker compose up will force image to be rebuild everytime before starting the container

### Step2: Serving the requests from Nginx

Installing Nginx server

```
sudo apt-get install nginx
```

Starting Nginx and checking its status 

```
sudo systemctl start nginx
sudo systemctl status nginx
```

#### Modify DNS Configurations

Add these two records to your DNS Configurations
```
A Record	*	0.227.49.244 (public ip of ec2)	Automatic
A Record	@	0.227.49.244 (public ip of ec2)	Automatic
```

Note: now you will be able to see nginx running page if you open public ip of the machine

Make Sure your EC2 security Group have this entry inbound rules 

```
random-hash-id	IPv4	HTTP	TCP	80	0.0.0.0/0	–
```

Open a new Nginx Configuration file name can be anything i am choosing arpansahu since my domain is arpansahu.me. there is already a default configuration file but we will leave it like that only

```
sudo vi /etc/nginx/sites-available/arpansahu
```

paste this content in the above file

```
server_tokens               off;
access_log                  /var/log/nginx/supersecure.access.log;
error_log                   /var/log/nginx/supersecure.error.log;

server {
  server_name               arpansahu.me;        
  listen                    80;
  location / {
    proxy_pass              http://{ip_of_home_server}:8014;
    proxy_set_header        Host $host;
  }
}
```

Basically this single Nginx File will be hosting all the multiple projects which I have listed before also.

Checking if configurations fie is correct

```
sudo service nginx configtest /etc/nginx/sites-available/arpansahu
```

Now you need to symlink this file to the sites-enabled directory:

``` 
cd /etc/nginx/sites-enabled
sudo ln -s ../sites-available/arpansahu
```

Restarting Nginx Server 
```
sudo systemctl restart nginx
```

Now It's time to enable HTTPS for this server

### Step 3: Enabling HTTPS 

1. Base Domain:  Enabling https for base domain only or a single sub domain

    To allow visitors to access your site over HTTPS, you’ll need an SSL/TLS certificate that sits on your web server. Certificates are issued by a Certificate Authority (CA).We’ll use a free CA called Let’s Encrypt. To actually install the certificate, you can use the Certbot client, which gives you an utterly painless step-by-step series of prompts.
    Before starting with Certbot, you can tell Nginx up front to disable TLS version 1.0 and 1.1 in favor of versions 1.2 and 1.3. TLS 1.0 is end-of-life (EOL), while TLS 1.1 contained several vulnerabilities that were fixed by TLS 1.2. To do this, open the file /etc/nginx/nginx.conf. Find the following line:
    
    Open nginx.conf file end change ssl_protocols 
    
    ```
    sudo vi /etc/nginx/nginx.conf
    
    From ssl_protocols TLSv1 TLSv1.1 TLSv1.2; to ssl_protocols TLSv1.2 TLSv1.3;
    ```
    
    Use this command to verify if nginx.conf file is correct or not
    
    ```
    sudo nginx -t
    ```
    
    Now you’re ready to install and use Certbot, you can use snap to install Certbot:
    
    ```
    sudo snap install --classic certbot
    sudo ln -s /snap/bin/certbot /usr/bin/certbot
    ```
    
    Now installing certificate
    
    ```
    sudo certbot --nginx --rsa-key-size 4096 --no-redirect
    ```
    
    It will be asking for domain name then you can enter your base domain 
    I have generated ssl for arpansahu.me
    
    Then a few questions will be asked by them answer them all and done your ssl certificate will be generated
    
    Now These lines will be added to your # Nginx configuration: /etc/nginx/sites-available/arpansahu
    
    ```
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/www.supersecure.codes/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.supersecure.codes/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
    ```
    
    Redirecting HTTP to HTTPS
    Open nginx configuration file  and make it like this

    ```
    sudo vi /etc/nginx/sites-available/arpansahu
    ```
    ```
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
        proxy_pass              http://{ip_of_home_server}:8014;
        proxy_set_header        Host $host;
        
        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/arpansahu.me/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/arpansahu.me/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }                          
    ``` 
    
    You can dry run and check weather it's renewal is working or not
    ```
    sudo certbot renew --dry-run
    ```
    
    Note: this process was for borcelle-crm.arpansahu.me and not for all subdomains.
        For all subdomains we will have to setup a wildcard ssl certificate


2. Enabling a Wildcard certificate

    Here we will enable ssl certificate for all subdomains at once
    
    Run following Command
    ```
    sudo certbot certonly --manual --preferred-challenges dns
    ```
    
    Again you will be asked domain name and here you will use *.arpansahu.me. and second domain you will use is
    arpansahu.me.
    
    Now, you should be having a question in your mind that why we are generating ssl for arpansahu.me separately.
    It's because Let's Encrupt does not include base doamin with wildcard certificates for subdomains.

    After running above command you will see a message similar to this
    
    ```
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
    check if it has finished deploying with aid of online tools, such as the Google
    Admin Toolbox: https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.arpansahu.me.
    Look for one or more bolded line(s) below the line ';ANSWER'. It should show the
    value(s) you've just added.
   
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Press Enter to Continue
    ```
   
    You will be given a dns challenge called ACME challenger you have to create a dns TXT record in DNS.
    Similar to below record.
    
    ```
    TXT Record	_acme-challenge	dpWCxvq3mARF5iGzSfaRNXwmdkUSs0wgsTPhSaX1gK4	5 Automatic
    ```
    
    Now, use this url to verify records are updated or not

    https://toolbox.googleapps.com/apps/dig/#TXT/_acme-challenge.arpansahu.me (arpansahu.me is domain)

    If its verified then press enter the terminal as mentioned above
    
    Then your certificate will be generated
    ```
    Successfully received certificate.
    Certificate is saved at: /etc/letsencrypt/live/arpansahu.me-0001/fullchain.pem            (use this in your nginx configuration file)
    Key is saved at:         /etc/letsencrypt/live/arpansahu.me-0001/privkey.pem
    This certificate expires on 2023-01-20.
    These files will be updated when the certificate renews.
    ```
    
    You can notice here, certificate generated is arpansahu.me-0001 and not arpansahu.me
    because we already generated a certificate named arpansahu.me
    
    So remember to delete it before generating this wildcard certificate
    using command

    ```
    sudo certbot delete
    ```
    
    Note: This certificate will not be renewed automatically. Auto-renewal of --manual certificates requires the use of an authentication hook script (--manual-auth-hook) but one was not provided. To renew this certificate, repeat this same certbot command before the certificate's expiry date.

3. Generating Wildcard SSL certificate and Automating its renewal

    1. Modify your ec2 inbound rules 
    
      ```
      –	sgr-0219f1387d28c96fb	IPv4	DNS (TCP)	TCP	53	0.0.0.0/0	–	
      –	sgr-01b2b32c3cee53aa9	IPv4	SSH	TCP	22	0.0.0.0/0	–
      –	sgr-0dfd03bbcdf60a4f7	IPv4	HTTP	TCP	80	0.0.0.0/0	–
      –	sgr-02668dff944b9b87f	IPv4	HTTPS	TCP	443	0.0.0.0/0	–
      –	sgr-013f089a3f960913c	IPv4	DNS (UDP)	UDP	53	0.0.0.0/0	–
      ```
    
   2. Install acme-dns Server

      * Create folder for acme-dns and change directory

        ```
         sudo mkdir /opt/acme-dns
         cd !$
        ```
      * Download and extract tar with acme-dns from GitHub

        ```
        sudo curl -L -o acme-dns.tar.gz \
        https://github.com/joohoi/acme-dns/releases/download/v0.8/acme-dns_0.8_linux_amd64.tar.gz
        sudo tar -zxf acme-dns.tar.gz
        ```
      * List files
        ```
        sudo ls
        ```
      * Clean Up
        ```
        sudo rm acme-dns.tar.gz
        ```
      * Create soft link
        ```
        sudo ln -s \
        /opt/acme-dns/acme-dns /usr/local/bin/acme-dns
        ```
      * Create a minimal acme-dns user
         ```
         sudo adduser \
         --system \	
         --gecos "acme-dns Service" \
         --disabled-password \
         --group \
         --home /var/lib/acme-dns \
         acme-dns
        ```
      * Update default acme-dns config compare with IP from the AWS console. CAn't bind to the public address need to use private one.
        ```
        ip addr
	  
        sudo mkdir -p /etc/acme-dns
	  
        sudo mv /opt/acme-dns/config.cfg /etc/acme-dns/
	  
        sudo vim /etc/acme-dns/config.cfg
        ```
      
      * Replace
        ```
        listen = "127.0.0.1:53” to listen = “private ip of the ec2 instance” 172.31.93.180:53(port will be 53)
 
        Similarly Edit other details mentioned below  

        # domain name to serve the requests off of
        domain = "auth.arpansahu.me"
        # zone name server
        nsname = "auth.arpansahu.me"
        # admin email address, where @ is substituted with .
        nsadmin = "admin@arpansahu.me"


        records = [
          # domain pointing to the public IP of your acme-dns server
           "auth.arpansahu.me. A 44.199.177.138. (public elastic ip)”,
          # specify that auth.example.org will resolve any *.auth.example.org records
           "auth.arpansahu.me. NS auth.arpansahu.me.”,
        ]
	
        [api]
        # listen ip eg. 127.0.0.1
        ip = "127.0.0.1”. (Changed)

        # listen port, eg. 443 for default HTTPS
        port = "8080" (Changed).         ——— we will use port 8090 because we will also use Jenkins which will be running on 8080 port
        # possible values: "letsencrypt", "letsencryptstaging", "cert", "none"
        tls = "none"   (Changed)

        ```
      * Move the systemd service and reload
        ```
        cat acme-dns.service
     
        sudo mv \
        acme-dns.service /etc/systemd/system/acme-dns.service
	  
        sudo systemctl daemon-reload
        ```
      * Start and enable acme-dns server
        ```
        sudo systemctl enable acme-dns.service
        sudo systemctl start acme-dns.service
        ```
      * Check acme-dns for posible errors
        ```
        sudo systemctl status acme-dns.service
        ```
      * Use journalctl to debug in case of errors
         ```
         journalctl --unit acme-dns --no-pager --follow
         ```
      * Create A record for your domain
         ```
         auth.arpansahu.me IN A <public-ip>
         ```
      * Create NS record for auth.arpansahu.me pointing to auth.arpansahu.me. This means, that auth.arpansahu.me is
        responsible for any *.auth.arpansahu.me records
        ```
        auth.arpansahu.me IN NS auth.arpansahu.me
        ```
      * Your DNS record will be looking like this
        ```
        A Record	auth	44.199.177.138	Automatic	
        NS Record	auth	auth.arpansahu.me.	Automatic
        ```
      * Test acme-dns server (Split the screen)
        ```
        journalctl -u acme-dns --no-pager --follow
        ```
      * From local host try to resolve random DNS record
        ```
        dig api.arpansahu.me
        dig api.auth.arpansahu.me
        dig 7gvhsbvf.auth.arpansahu.me
        ``` 
        
   3. Install acme-dns-client 
     ```
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
     ```
     cd
     sudo snap install core; sudo snap refresh core
     sudo snap install --classic certbot
     sudo ln -s /snap/bin/certbot /usr/bin/certbot
     ```
    Note: you can skip step4 if Certbot is already installed

    5. Get Letsencrypt Wildcard Certificate
       * Create a new acme-dns account for your domain and set it up
         ```
         sudo acme-dns-client register \
         -d arpansahu.me -s http://localhost:8090
         ```
         Note: When we edited acme-dns config file there we mentioned the port 8090 and thats why we are using this port here also
       * Creating Another DNS Entry 
         ```
         CNAME Record	_acme-challenge	e6ac0f0a-0358-46d6-a9d3-8dd41f44c7ec.auth.arpansahu.me.	Automatic
         ```
         Same as an entry is needed to be added to complete one time challenge as in previously we did.
       * Check the entry is added successfully or not
         ```
         dig _acme-challenge.arpansahu.me
         ```
       * Get wildcard certificate
         ```
         sudo certbot certonly \
         --manual \
         --test-cert \ 
         --preferred-challenges dns \ 
         --manual-auth-hook 'acme-dns-client' \ 
         -d ‘*.arpansahu.me’ -d arpansahu.me
         ```
         Note: Here we have to mention both the base and wildcard domain names with -d since let's encrypt don't provide base domain ssl by default in wildcard domain ssl
       *Verifying the certificate
         ```
         sudo openssl x509 -text -noout \
         -in /etc/letsencrypt/live/arpansahu.me/fullchain.pem
         ```
       * Renew certificate (test)
         ```
         sudo certbot renew \
         --manual \ 
         --test-cert \ 
         --dry-run \ 
         --preferred-challenges dns \
         --manual-auth-hook 'acme-dns-client'       
         ```
       * Renew certificate (actually)
         ```
         sudo certbot renew \
         --manual \
         --preferred-challenges dns \
         --manual-auth-hook 'acme-dns-client'       
         ```
       * Check the entry is added successfully or not
         ```
         dig _acme-challenge.arpansahu.me
         ```
    6. Setup Auto-Renew for Letsencrypt WILDCARD Certificate
       * Setup cronjob
         ```
         sudo crontab -e
         ```
       * Add following lines to the file
         ```
         0 */12 * * * certbot renew --manual --test-cert --preferred-challenges dns --manual-auth-hook 'acme-dns-client'
         ```

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

Installing Jenkins

Reference: https://www.jenkins.io/doc/book/installing/linux/

Jenkins requires Java in order to run, yet certain distributions don’t include this by default and some Java versions are incompatible with Jenkins.

There are multiple Java implementations which you can use. OpenJDK is the most popular one at the moment, we will use it in this guide.

Update the Debian apt repositories, install OpenJDK 11, and check the installation with the commands:

```
sudo apt update

sudo apt install openjdk-11-jre

java -version
openjdk version "11.0.12" 2021-07-20
OpenJDK Runtime Environment (build 11.0.12+7-post-Debian-2)
OpenJDK 64-Bit Server VM (build 11.0.12+7-post-Debian-2, mixed mode, sharing)
```

Long Term Support release

```
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

Start Jenkins

```
sudo systemctl enable jenkins
```

You can start the Jenkins service with the command:

```
sudo systemctl start jenkins
```

You can check the status of the Jenkins service using the command:
```
sudo systemctl status jenkins
```

Now for serving the Jenkins UI from Nginx add these following lines to the Nginx file located at 
/etc/nginx/sites-available/arpansahu by running the following command

```
sudo vi /etc/nginx/sites-available/arpansahu
```

* Add these lines to it.

    ```
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
just make sure you place the server block for base domain at the last

* To copy .env from local server directory while buidling image

add Jenkins ALL=(ALL) NOPASSWD: ALL
inside /etc/sudoers file

and then put 

stage('Dependencies') {
            steps {
                script {
                    sh "sudo cp /root/env/project_name/.env /var/lib/jenkins/workspace/project_name"
                }
            }
        }

in jenkinsfile

* Now Create a file named Jenkinsfile at the root of Git Repo and add following lines to file

```
pipeline {
    agent { label 'local' }
    stages {
        stage('Dependencies') {
            steps {
                script {
                    sh "sudo cp /root/projectenvs/{project_name}/.env /var/lib/jenkins/workspace/{project_name}"
                }
            }
        }
        stage('Production') {
            steps {
                script {
                    sh "docker compose up --build --detach"
                }
            }
        }
    }
    post {
        success {
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
                                "Subject": "${currentBuild.fullDisplayName} deployed succcessfully",
                                "TextPart": "Hola Development Team, your project ${currentBuild.fullDisplayName} is now deployed",
                                "HTMLPart": "<h3>Hola Development Team, your project ${currentBuild.fullDisplayName} is now deployed </h3> <br> <p> Build Url: ${env.BUILD_URL}  </p>"
                        }
                ]
            }'"""
        }
        failure {
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
                                                "Name": "Developer Team"
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
```

Note: agent {label 'local'} is used to specify which node will execute the jenkins job deployment. Basically there are two nodes in this project 
      One is my local Linux Server and Another is AWS EC2 machine where nginx is hosted there arpansahu.me my portfolio is also hosted is also hosted.
      So local linux server is labelled with 'local' are the project with this label will be executed in local machine node.


* Configure a Jenkins project from jenkins ui located at https://jenkins.arpansahu.me

Make sure to use Pipline project and name it whatever you want I have named it as great_chat

![Jenkins Project for borcelle CRM Configuration File](/great_chat-Config-Jenkins-.png)

In this above picture you can see credentials right? you can add your github credentials
from Manage Jenkins on home Page --> Manage Credentials

and add your GitHub credentials from there

* Add a .env file to you project using following command (This step is no more required stage('Dependencies'))

    ```
    sudo vi  /var/lib/jenkins/workspace/borcelle_crm_declarative_pipeline_project/.env
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


This approach should help you manage the dependencies and resolve the version conflicts more effectively.

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

My PGAdmin4 can be accessed here : https://pgadmin.arpansahu.me/

## Portainer
   
Portainer is a web UI to manage your docker, and kubernetes. Portainer consists of two elements, the Portainer Server, and the Portainer Agent. Both elements run as lightweight Docker containers on a Docker engine.

### Installation

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

### Installation

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

tls-port 6379
port 0

tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-dh-params-file /path/to/dhparam.pem

tls-auth-clients no

Add this configuration 

Mostly redis is used as cache and we want it to be super fast hence we are not putting it behind reverse proxy e.g. nginx same as postgres

Also one more thing redis by default don't support ssl connections even if u use ssl

redis serve can be accessed

```bash
redis-cli -h arpansahu.me -p 6379 -a password_required
```

## Redis Commander

Redis Commander is a web-based management tool for Redis databases. It provides a user-friendly interface to interact with Redis, making it easier to manage and monitor your Redis instances.

### Installation

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

tls-port 6379
port 0

tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-dh-params-file /path/to/dhparam.pem

tls-auth-clients no

Add this configuration 

Mostly redis is used as cache and we want it to be super fast hence we are not putting it behind reverse proxy e.g. nginx same as postgres

Also one more thing redis by default don't support ssl connections even if u use ssl

My Redis Commander can be accessed here : https://redis.arpansahu.me/

## MiniIo (Self hosted S3 Storage)

MinIO is a high-performance, distributed object storage system designed for large-scale data infrastructures. It is open-source and compatible with the Amazon S3 API, making it a popular choice for organizations looking for scalable, secure, and cost-effective storage solutions. 

### Installation

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

tls-port 6379
port 0

tls-cert-file /path/to/redis.crt
tls-key-file /path/to/redis.key
tls-dh-params-file /path/to/dhparam.pem

tls-auth-clients no

Add this configuration 

Mostly redis is used as cache and we want it to be super fast hence we are not putting it behind reverse proxy e.g. nginx same as postgres

Also one more thing redis by default don't support ssl connections even if u use ssl

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

SECRET_KEY=

DEBUG=

ALLOWED_HOSTS=

MAIL_JET_API_KEY=

MAIL_JET_API_SECRET=

MY_EMAIL_ADDRESS=

# bucket
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_STORAGE_BUCKET_NAME=

BUCKET_TYPE=

DOMAIN=

PROTOCOL=

DATABASE_URL=

REDISCLOUD_URL=


