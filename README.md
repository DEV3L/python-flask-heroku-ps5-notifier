# Python Flask Heroku PS5 Notifier

A Python Flask application that can searches and notifies through Twillio when a PS5 console/digital is available.

## Prerequisites

- Python 3x
- MongoDB

### Recommendations

- PyCharm
- MongoDB Compass
- Docker

## Environment Variables

Copy the contents of .env.local into a new file named .env

```
cp .env.local .env
```

## Running Locally

1. Setup MongoDb

`docker run -d -p 27017:27017 --name ps5-notifier mongo`

2. Install Python Dependencies

```
~ python3 -m venv python-flask-heroku-ps5-notifier
~ source python-flask-heroku-ps5-notifier/bin/activate
(python-flask-heroku-ps5-notifier) ~ python setup.py develop
```

3. Run Tests

`(python-flask-heroku-ps5-notifier) ~ pytest`

4. Run Application for Development

`(python-flask-heroku-ps5-notifier) ~ python app.py runserver`


#### PyCharm

Dependency management and interactive debugging are available using PyCharm.

The [Configure a virtual environment](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
can help with questions on how to do this.

## Components

#### Flask

#### MongoDb

#### Logging

`logs` directory - Rotating 10mb

#### Swagger

http://localhost:5000/swagger

#### Scripts
