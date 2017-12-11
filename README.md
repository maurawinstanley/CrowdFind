# CrowdFind
CSCI 3308 - Team 63 Project - CrowdFind

How to Run:
1) Create new MySQL Database
2) In settings.py, under DATABASES:
    a) Update ENGINE to 'django.db.backends.mysql'
    b) Update NAME to name of the database you created
    c) Update USER to the username of the database
    d) Update PASSWORD' to the password of the database
3) Open terminal and navigate to CrowdFind/website directory
4) To sync your database with django run 'python manage.py makemigrations' and once that finishes run 'python manage.py migrate'
5) To then run the application run 'python manage.py runserver'
6) Navigate to http://127.0.0.1:8000 to get to login/registraion portion

Testing:
See previous Testing file
https://github.com/michaelmdresser/CrowdFind/blob/master/TESTING.md
