from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# from .models import Email
# Create your views here.

def index(request):
    return render(request, 'LoginAndReg/index.html')

def success(request):
    print 'in process method'
    print request.POST

    response = User.objects.validate_new_user(request.POST)

    if response[0] == False:
        for error in response[1]:
            messages.error(request, error)
            print '7'*50
            print error
            return redirect('/')
    else:
        print '9'*50
        print 'got to the "else"'
        print response[1]
        # try:
        #     request.session['first_name'] = response[1].first_name
        # except MultiValueDictKeyError:
        #     pass
        return redirect('/success')

def validation(request):
    print "*"*50
    return render(request, 'LoginAndReg/success.html')
