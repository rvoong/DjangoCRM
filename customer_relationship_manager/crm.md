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

Create `website`
`python manage.py startapp website`

Migrate
`python manage.py migrate`

Run the Django Server
`python manage.py runserver`

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

Inside the templates folder create `home.html`

1. Within the base.html file, copy the example from bootstrap

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

17. Editing the home.html so the names match up with the views.py

```
{% extends 'base.html' %} {%block content%}

<div class="col-md-6 offset-md-3">
  <h1>Login</h1>
  <br />

  {% if user.is_authenticated%}

  <h1>Hello World</h1>

  {% else %}

  <form method="POST" action="{% url 'home' %}">
    {% csrf_token %}
      <div class="mb-3">
        <label for="Username" class="form-label">Username</label>
        <input
          type="email"
          class="form-control"
          name="username"
          placeholder="Username"
          required
        />
      </div>

      <br />
      <div class="mb-3">
        <input
          type="password"
          class="form-control"
          name="password"
          placeholder="password"
          required
        />
      </div>

      <button type="login" class="btn btn-secondary">Submit</button>
  </form>
</div>

{% endif %} {% endblock %}
```

18. Edit the views.py home function with the necessary variables

```

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']
    # Authenticate
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "Error logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {})



```

Add into the base.html
```
  <body>
    {% include 'navbar.html'%}
    <div class="container">
      <br />
      {% if messages %} 
        {% for message in messages %} 
         {{message}} 
        {% endfor %}
      {% endif %} 
      
      {% block content%} 
      {% endblock%}
    </div>
    ...

```
19. Go to bootstrap

add a new bootstrap alert component 
```
  <body>
    {% include 'navbar.html'%}
    <div class="container">
      <br />
      {% if messages %} 
        {% for message in messages %} 
        <div class="alert alert-warning alert-dismissible fade show" role="alert">
          <strong>Failed Login</strong>
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        {% endfor %}
      {% endif %} 

      {% block content%} 
      {% endblock%}
```

21. Create the logout function 

```
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect('home')
```

In the navbar
```
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="{% url 'home' %}"> Navbar</a>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        {% if user.is_authenticated %}
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="{% url 'logout'%}">Logout</a>
        </li>
        {% else %}
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="{% url 'home'%}">Login</a>
        </li>

        {% endif %}
      </ul>
    </div>
  </div>
</nav>

```
22. Create the register button

Create a new HTML file 
```
{% extends 'base.html' %}
{% block content %}

<h1> register </h1>

{% endblock %}
```

add to the navbar

```
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="{% url 'register' %}">Register</a>
        </li>
```

23. Create a forms.py

* using forms, user and UserCreationForm to simplify the creation of users

```
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
            
```

24. import the forms.py into the views to extend the functionality of register_user

```
def register_user(request):
    ## only occurs if they are posting the SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            #Authenticate and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Sucessfully Registered")
            return redirect('home')
    else: 
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form': form})
```

25. Django abstracts away the database aspects of the code. Create the Record in models.py
```
from django.db import models

# Create your models here.
class Record(models.Model):
    ## tells you when the model was created
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address =models.CharField(max_length=100)
    city =models.CharField(max_length=15)
    state =models.CharField(max_length=100)
    zipcode =models.CharField(max_length=50)
    email =models.CharField(max_length=50)
    phone =models.CharField(max_length=20)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
```


26. Create a migration for the database model. It sets the primary key etc.
`python manage.py makemigrations`

27. `python manage.py migrate`
migrates the server to mysqlworkbench websites_record

28. In the admin.py, we register the Record model
```
from django.contrib import admin
from .models import Record
# Register your models here.

admin.site.register(Record)

```
29. Edit the home function. Pass in the records:records
```
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
    
    # Check to see if logging in
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']
    # Authenticate
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "Error logging in")
            return redirect('home')
    # if the user isn't POST-ing to log in
    else:
        return render(request, 'home.html', {'records': records})

```
30. Edit home.html for table format as well as the record
```
{% extends 'base.html' %} {%block content%}


  {% if user.is_authenticated%}

  <table class="table table-striped table-hover table-bordered">
    <thead class="table-dark">
        <th scope="col">Name</th>
        <th scope="col">Email</th>
        <th scope="col">Phone</th>
        <th scope="col">Address</th>
        <th scope="col">City</th>
        <th scope="col">Zipcode</th>
        <th scope="col">ID</th>
    </thead>
    <tbody>
      

      {% if records %}
      {% for record in records %}
        <tr>
          <td>{{record.first_name}} {{record.last_name}} </td>
          <td>{{record.email}}</td>
          <td>{{record.phone}}</td>
          <td>{{record.address}} </td>
          <td>{{record.city}}</td>
          <td>{{record.zipcode}}</td>
          <td>{{record.id}}</td>
        </tr>
        <br>
      {% endfor %}
    {% endif %}

    {% else %}
    </tbody>
  </table>



  <form method="POST" action="{% url 'home' %}">
    {% csrf_token %}
      <div class="mb-3">
        <label for="Username" class="form-label">Username</label>
        <input
          type="text"
          class="form-control"
          name="username"
          placeholder="Username"
          required
        />
      </div>

      <br />
      <div class="mb-3">
        <input
          type="password"
          class="form-control"
          name="password"
          placeholder="password"
          required
        />
      </div>

      <button type="login" class="btn btn-secondary">Submit</button>
  </form>
</div>

{% endif %} 
{% endblock %}

```

31. Create the url, views, and template for customer_record
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk', views.customer_record, name='record'),
]

```

in views.py
```

def customer_record(request, pk):
    if request.user.is_authenticated: 
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record} )    
    
    else: 
        messages.success(request, 'You must be logged in to view that page...')
        return redirect('home')
        
```

in templates folder. Create record.html.
```
{% extends 'base.html' %}
{% block content %}

<h1> Customer Record </h1>

{% endblock %}
```

32. Make the ID clickable. In home.html 
```
<td><a href="{% url 'record' record.id %}"> {{record.id}}</td>

```
33. Edit the record.html to get the card to be how you want it 

```
{% extends 'base.html' %}
{% block content %}

<div class="card">
    <div class="card-header">
        {{customer_record.first_name}} {{record.last_name}} 
    </div>
    <div class="card-body">
      <h5 class="card-title">Record</h5>
      <p class="card-text">
        {{customer_record.email}}
        {{customer_record.phone}}
        {{customer_record.address}} 
        {{customer_record.city}}
        {{customer_record.zipcode}}
        </p>
    </div>
  </div>
<br/> 
<a href="{url 'home' %}" class="btn btn-secondary">Back</a>
<a href="{url 'home' %}" class="btn btn-danger">Delete</a>


{% endblock %}
```

34. Add a delete button to the record by editing the views, url.py, and the record.html 

```
{% extends 'base.html' %}
{% block content %}

<div class="card">
    <div class="card-header">
        {{customer_record.first_name}} {{record.last_name}} 
    </div>
    <div class="card-body">
      <h5 class="card-title">Record</h5>
      <p class="card-text">
        {{customer_record.email}}
        {{customer_record.phone}}
        {{customer_record.address}} 
        {{customer_record.city}}
        {{customer_record.zipcode}}
        </p>
    </div>
  </div>
<br/> 
<a href="{% url 'home' %}" class="btn btn-secondary">Back</a>
<a href="{% url 'delete_record' customer_record.id %}" class="btn btn-danger">Delete</a>


{% endblock %}
```
```
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
    
    # Check to see if logging in
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']
    # Authenticate
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "Error logging in")
            return redirect('home')
    # if the user isn't POST-ing to log in
    else:
        return render(request, 'home.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect('home')

def register_user(request):
    ## only occurs if they are posting the SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            #Authenticate and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have Sucessfully Registered")
            return redirect('home')
    else: 
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated: 
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record} )    
    
    else: 
        messages.success(request, 'You must be logged in to view that page...')
        return redirect('home')
    

def delete_record(request, pk):
    if request.user.is_authenticated: 
        delete_rec = Record.objects.get(id=pk)
        delete_rec.delete()
        messages.success(request, 'Record deleted sucessfully')
        return redirect('home')
    else: 
        messages.success(request, 'You must be logged in to view that page...')
        return redirect('home')

```

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    
]

```


35. add_record 

```
def add_record(request):
    if request.user.is_authenticated: 
        return render(request, 'add_record.html',{})
    else: 
        messages.success(request, 'You must be logged in to view that page...')
        return redirect('home')
```
```

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record')
]

```

36. Add to forms.py 
```
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'first name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name'}))
    
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
            
# Create Add Record Form 
class AddRecordForm(forms.ModelForm):
    created_at = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"created_at", "class":"form-control"}), label="")
    first_name = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    address = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
    zipcode = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zip", "class":"form-control"}), label="")
    email = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone = forms.DateTimeField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    
    class Meta:
        model = Record
        exclude = ("user",)
    
```
Add to views.py
```
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated: 
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else: 
        messages.success(request, "You Must be Logged In...")
        return redirect('home')
```
37. Add update_record url, views and html



# Major Takeaways

- Django projects need these three important files: view, HTML page, URL
- The url patterns pull from the views. The views call on the html file
- 
