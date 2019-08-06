## Description

<p>This is a temporary repository to showcase the solution for the programming tasks
explained below:</p>

## Main Tasks

1. Create the Django polls app with Django version 2.2 or later, Python 3.7 or later and PostgreSQL version 11.0 or later as database system

   - [x] Completed! -> reach out

---

2. Implement a Django command for importing thousands of polls at a time from a source of your choice (e.g. CSV)

   - 2.1 Validate the functionality of your command by implementing unit and/or integration tests

   - [x] Completed! -> Please see tests/test_commands.py for details. You can run tests inside docker container. See details in docker section below.

---

3. Add an IP address field to the author model and implement a custom lookup field for IsContainedByOrEqual using PostgreSQL inet operators

   - [x] Completed! -> I've implemented [django-netfields](https://pypi.org/project/django-netfields/ "django-netfiels") and I've written a test to show how it can be used. Please see tests/test_lookups.py for details

---

4. Implement a password protected healthcheck endpoint covering:

   - 1. Django app is up and running and not in dev mode
   - 2. Database is accessible and can be queried
   - 3. App server has disk space left

   - [x] Completed! -> I've implemented [watchman](https://github.com/mwarkentin/django-watchman "watchman") for monitoring the health of databases, caches and default file storage.

You have to be a logged-in staff user to display the page for system status at:

```shell
{website}/watchman/dashboard/
```

---

5. Adjust the Django admin panel for the Author model that IP addresses are displayed but the last 8 bits are masked with asterisk

   - [x] Completed! -> last 8 bits of IP addresses are encrypted with using regex in a custom method for django admin list display field.

---

## Optional Tasks

1. Provide a brief concept of how you would provide a redundant setup of the above Django app. (at least one App/DB server at a time can fail) in any form you prefer (e.g. Text, Diagram, Presentation, Dockerfiles etc.)

   - [x] Completed! -> I've used containerization with Docker. Please see build instructions below to test the functionality of the app.

---

2. Describe briefly how you would build and distribute this app for a Debian based server infrastructure

---

## Build instructions with Docker Compose

1. Clone the repo

```shell
git clone https://github.com/talented/Django-Polls-App-Extended.git
```

2. Run

```shell
cd django-polls-app-extended

docker-compose build

docker-compose up
```

3. Without stopping the running server open a new tab in your terminal, get into the same directory and run command below to run tests

```
docker-compose run app sh -c "python manage.py test"
```

4. In order to populate the database for testing purposes with a few poll questions with author information, run commands below to get into the running container and run command to import data from given csv file

```
docker exec -it django-polls-app-extended_app_1 sh

python manage.py import_from_csv /pgdata/polls.csv
```

5. You have to create a superuser to see the admin backend functionality. Run command below inside the docker container to create an admin user

```
python manage.py createsuperuser
```
