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

9. Within the base.html file, copy the example from bootstrap

```
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
  </body>
</html>
```

9. Include a div and break for the block content

base.html

```
<div class="container">
    <br />
    {% block content%} {% endblock%}
</div>
```

9. In home.html

```
{% extends 'base.html' %} {%block content%}
<h1>Hello World!</h1>
{% endblock %}

```

10. Include the navbar.html in the base.html

```
    {% include 'navbar.html'%}
    <div class="container">
      <br />
      {% block content%} {% endblock%}
    </div>
```

11. Change the background color of the navbar to black

`<nav class="navbar navbar-expand-lg navbar-dark bg-dark">`

12. Delete all the navbar features that you don't need in navbar.html

13. Login Users

In views.py

```
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def login_user(request):
    pass


def logout_user(request):
    pass

```

In urls.py

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
```

14. Create the form whenever the user enters the site to prompt for login information. Put it in the home.html

home in action needs the ''
copy the form from bootstrap

```
{% extends 'base.html' %} {%block content%}

<div class="col-md-6 offset-md-3">
  <h1>Login</h1>
  <form method="POST" action="{% url 'home' %}">
    {% csrf_token %}
    <form>
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
        />
        <div id="emailHelp" class="form-text">
          We'll never share your email with anyone else.
        </div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          id="exampleInputPassword1"
        />
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1" />
        <label class="form-check-label" for="exampleCheck1">Check me out</label>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </form>
</div>
{% endblock %}
```

15. Change the button to a secondary to make it gray

```
<button type="submit" class="btn btn-secondary">Submit</button>
```

16. Removing some things to clean up the form
    The check me out dive to get rid of the checkbox

```
<div class="mb-3 form-check">
  <input type="checkbox" class="form-check-input" id="exampleCheck1" />
  <label class="form-check-label" for="exampleCheck1">Check me out</label>
</div>
```

```
<label for="exampleInputPassword1" class="form-label">Password</label>
```

```
<label for="exampleInputPassword1" class="form-label">Password</label>
```

1.

# Major Takeaways

- Django projects need these three important files: View, HTML page, URL
