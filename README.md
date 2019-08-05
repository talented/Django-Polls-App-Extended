## Description

<p>This is a temporary repository to showcase the solution for the programming tasks
explained below:</p>

### Main Tasks

[x] 1. Create the Django polls app with Django version 2.2 or later, Python 3.7 or later and PostgreSQL version 11.0 or later as database system

![#157500](https://placehold.it/20/157500?text=+) Completed!

[x] 2. Implement a Django command for importing thousands of polls at a time from a source of your choice (e.g. CSV)

<p style="margin-left:20px;">2.1 Validate the functionality of your command by implementing unit and/or integration tests</p>

![#157500](https://placehold.it/20/157500?text=+) Completed -> Please see tests/test_commands.py for details

3. Add an IP address field to the author model and implement a custom lookup field for IsContainedByOrEqual using PostgreSQL inet operators

4. Implement a password protected healthcheck endpoint covering:

<span style="margin-left:20px;">
1.	Django app is up and running and not in dev mode
2.	Database is accessible and can be queried
3.	App server has disk space left
5. Adjust the Django admin panel for the Author model that IP addresses are displayed but the last 8 bits are masked with asterisk
</span>

###Optional Tasks

1. Provide a brief concept of how you would provide a redundant setup of the above Django app. (at least one App/DB server at a time can fail) in any form you prefer (e.g. Text, Diagram, Presentation, Dockerfiles etc.)

2. Describe briefly how you would build and distribute this app for a Debian based server infrastructure
