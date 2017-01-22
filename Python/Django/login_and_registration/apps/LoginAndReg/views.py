from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# from .models import Email
# Create your views here.

def index(request):
    context = {
    'users': User.objects.all()
    }
    return render(request, 'LoginAndReg/index.html', context)

def validation(request):
    print 'in process method'
    print request.POST

    response = User.objects.validate_new_user(request.POST)

    if response[0] == False:
        for error in response[1]:
            messages.error(request, error)
            print '*'*50
            print error
            return redirect('/')
    else:
        print '*'*50
        print 'got to the "else"'
        print response[1]
        request.session['first_name'] = response[1].first_name
        return redirect('/success')

def success(request):
    user = user.objects.all()
    context = {
    'user': user
    }
    return render(request, 'LoginAndReg/success.html', context)
