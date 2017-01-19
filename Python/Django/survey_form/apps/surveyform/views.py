from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    title = "Survey Form"
    location = ['New York', 'California', 'Online', 'Other']
    language = ['Python', 'Javascript', 'Html']
    context = {
        'title': title,
        'locations': location,
        'languages': language
    }
    return render(request, 'surveyform/index.html', context)

def result(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count']
    }
    return render(request, 'surveyform/result.html', context)

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
