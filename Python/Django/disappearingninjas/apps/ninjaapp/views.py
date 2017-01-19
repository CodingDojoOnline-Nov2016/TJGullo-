from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjaapp/index.html')

def show(request, ninja_color):
    turtle_options = {
    'red': 'ninjaapp/raphael.jpg',
    'blue': 'ninjaapp/leonardo.jpg',
    'orange': 'ninjaapp/michaelangelo.jpg',
    'purple': 'ninjaapp/donatello.jpg'
    }
    if ninja_color in turtle_options:
        context = {
        'image': turtle_options[ninja_color]
        }
    else:
        context = {
        'image': 'ninjaapp/april.jpg'
        }
    return render(request, 'ninjaapp/index.html', context)
