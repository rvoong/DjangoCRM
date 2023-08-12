from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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
    
def update_record(request, pk):
    if request.user.is_authenticated: 
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, 'Record Updated')
                return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else: 
        messages.success(request, "You Must be Logged In...")
        return redirect('home')