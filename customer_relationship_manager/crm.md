# Project to build a basic CRM using Django

CRM: Customer Relationship Manager
mySQL: Database for the backend
`pip install mysql`

`pip install mysql-connector-python`

`pip install mysql-connector`

- Postgres can be swapped out with just a couple settings

## Virtual Environment Setup

Terminal Commands
`python -m venv venv  `

`Set-ExecutionPolicy Unrestricted -Scope Process`

`venv\Scripts\activate`

`djando-admin startproject customer_relationship_manager`

## Django Setup

`python manage.py startapp website`

1. _pycache_-> Settings.py -> add `website` to the INSTALLED_APPS

2. Add the usernames to Database

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CRMdatabase',
        'USER': 'Root',
        'PASSWORD': 'Voongra_mysql18',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

3. Migrate
   `python manage.py migrate`

4. Run the Django Server
   `python manage.py runserver`

5. Git

```
git add .
git commit -am "Initial Commit"
git remote add origin https://github.com/rvoong/DjangoCRM.git
git branch -M main
git push -u origin main
```

6. Create a urls.py file in the website folder

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

7. Create a views.py file

```
def home(request):
    return render(request, 'home.html', {})
```

8. Create a Templates folder. Django knows to look for the templates folder

- Inside the templates folder create `home.html`

* There are three important template files: HTML page, URL, view
*
