from django.shortcuts import render, redirect
import random, string

def index(request):
    print "*"*50
    print request.method
    print "*"*50
    random_word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    context = {
    'random_word': random_word,
    }
    print "*"*50
    print random_word
    print "*"*50
    request.session.random_word = random_word
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
    return render(request, 'rwg/index.html', context)

def random_word(request):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    request.session['attempt'] += 1
    return redirect('/')

def reset(request):
	del request.session['attempt']
	del request.session['random_word']
	return redirect('/')

# Create your views here.
