from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
# Create your views here.
def index(request):
    return render(request, 'validation/index.html')

def validation(request):
    print 'in process method'
    print request.POST

    response = Email.emailManager.isValidEmail(request.POST)

    if response[0] == False:
        for error in response[1]:
            messages.error(request, error)
            return redirect('/')
    else:
        return redirect('validation/success.html')





def success(request):
    emails = Email.emailManage.all()
    context = {
    'curr_email': request.session('email')
    }
    return render(request, 'validation/success.html', context)
