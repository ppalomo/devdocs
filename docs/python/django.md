# Django

- [Django](#django)
  - [Installing Django](#installing-django)
  - [Creating a new Django project](#creating-a-new-django-project)
  - [???](#)


## Installing Django

```shell
# Installing pipenv to manage environments and dependencies
$ pip3 install pipenv

# Creating a new directory
$ mkdir my_project
$ cd my_project

# Installing django package through pipenv
$ pipenv install django

```

## Creating a new Django project

```shell
# Activating the environment
$ pipenv shell
$ django-admin startproject project_name .

# Running Django
$ python manage.py runserver

# Ctrl+C to stop the server and $exit to exit the env

# Creating a new django app (should be added in settings.pt -> INSTALLED_APPS)
$ python manage.py startapp app_name

```

## ???



