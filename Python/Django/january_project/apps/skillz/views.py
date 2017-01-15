from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print request
    context = {
    'name': "TJ",
    'my_dict': {
        'thing1': "thing1",
        'thing2': "thing2",
        }
    }
    return render(request, 'skillz/index.html', context)

def process(request):
    print 'processing'
    print request.POST
    return redirect('/')
