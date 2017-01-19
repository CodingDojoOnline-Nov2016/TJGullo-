from django.shortcuts import render, redirect
import random, datetime
# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'gold/index.html')

def process(request):
    print '\n', '***'*20, 'we made it to the guessing route!!!'
    request.session['building'] = request.POST['building']
    building = request.session['building']
    timestamp = datetime.datetime.now()

    # locations = {
    #     'farm': random.randint(10,20)),
    #     'cave': random.randint(5,10)),
    #     'house': random.randint(2,5)),
    #     'casino': random.randint(-50,50)),
    #     }

    if building == 'farm':
        farm_gold = int(random.randint(10,20))
        request.session['gold'] += farm_gold
        request.session['activities'] = "Earned {} from the {} on {}".format(farm_gold, building, timestamp)
        print farm_gold

    if building == 'cave':
        cave_gold = int(random.randint(5,10))
        request.session['gold'] += cave_gold
        print cave_gold


    if building == 'house':
        house_gold = int(random.randint(2,5))
        request.session['gold'] += house_gold
        print house_gold

    if building == 'casino':
        casino_gold = int(random.randint(-50,50))
        request.session['gold'] += casino_gold
        print casino_gold

    return redirect('/')
