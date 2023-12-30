# Micro
![GitHub repo size](https://img.shields.io/github/repo-size/FMularski/micro)
![GitHub last commit](https://img.shields.io/github/last-commit/FMularski/micro?color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/FMularski/micro?color=purple)

## ✉️ Created with
* Django 5.0
* Pika 1.3.2
* RabbitMQ 3.12.10 (management plugin)
* Celery 5.3.6
* Postrges 13
* Nginx 1.25.3
* Docker compose 3.9

## ✉️ About
Demo project presenting an implementation of an event-driven communication between applications in the minimalistic microservices architecture.  

## ✉️ Services
* users - django admin project for creating users
* email - django project handling delivery of emails

## ✉️ Setup and launching

* Download the project to your local machine
```bash
git clone https://github.com/FMularski/thebitbybit-recruitment.git
```

* Create the following .env files:
```bash
# micro/users/users/.env
SECRET_KEY=some-secret-key-users

POSTGRES_DB=users
POSTGRES_USER=users
POSTGRES_PASSWORD=users
POSTGRES_HOST=users-psql
POSTGRES_PORT=5432
PGUSER=users

MQ_USERNAME=users
MQ_PASSWORD=users
MQ_HOST=mq
MQ_PORT=5672
```

```bash
# micro/email/email_service/.env
SECRET_KEY=some-secret-key-email

MQ_USERNAME=email
MQ_PASSWORD=email
MQ_HOST=mq
MQ_PORT=5672

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST_USER=notifier@app.com
```

* Start the project with docker compose
```bash
docker compose up
```

## ✉️ Inspecting the communication

* Open the app in your browser at
```bash
http://localhost:80
```

* Log in as the admin and create a new user 
```bash
username: admin
password: admin
```

* When creating an user with an email, a welcome message is sent. If ```EMAIL_BACKEND``` is set to ```django.core.mail.backends.console.EmailBackend``` you can verify if the email has been sent by checking logs of the container ```micro-email-celery```:
```
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Welcome!
From: notifier@app.com
To: new-user@example.com
Date: Sat, 30 Dec 2023 19:23:01 -0000
Message-ID: <170396418105.9.252225622923189327@f643b277ea47>
 
Hello new-user, thanks for registration!
```
* You can also see logs of the ```micro-email-consumer``` container:
```
Starting AMQP consumer...
Consuming message from queue: user-created
Firing callback: send_welcome_email
```
* All properties of the broker such as connections, exchanges, queues, etc. can be inspected in the RabbitMQ manager  at ```http://localhost:15672```
