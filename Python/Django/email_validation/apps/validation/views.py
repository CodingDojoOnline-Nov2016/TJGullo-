from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
# Create your views here.
def index(request):
    return render(request, 'validation/index.html')

def validation(request):
    print 'in process method'
    print request.POST

    response = Email.objects.isValidEmail(request.POST)

    if response[0] == False:
        for error in response[1]:
            messages.error(request, error)
            return redirect('/')
    else:
        print response[1]
        request.session['curr_email'] = response[1].email
        return redirect('/success')





def success(request):
    emails = Email.objects.all()
    context = {
    'emails': emails
    }
    return render(request, 'validation/success.html', context)
