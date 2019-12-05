from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.id = 1
    # dest1.img = 'destination_1.jpg'
    # dest1.name = "Magodo"
    # dest1.desc = 'A nice quiet place to live in'
    # dest1.price =  8000
    # dest1.specialoffer = False

    # dest2 = Destination()
    # dest2.id = 2
    # dest2.img = 'destination_2.jpg'
    # dest2.name = "Agege"
    # dest2.desc = 'Not an etirely bad place if you ask me'
    # dest2.price =  800
    # dest2.specialoffer = True

    # dest3 = Destination()
    # dest3.id = 3
    # dest3.img = 'destination_3.jpg'
    # dest3.name = "Lekki"
    # dest3.desc = 'An appropriate place to work in'
    # dest3.price = 10000
    # dest3.specialoffer = False

    # destinations = [dest1, dest2, dest3]
    destinations = Destination.objects.all()
    return render(request, 'index.html', {'destination': destinations})


def calculator(request):

    if request.method == 'GET':
        user = User()
        print('name: ', user.email, 'auth? : ', user.username)
        if (user.is_authenticated):
            
            return render(request,'home.html',{'name':user.first_name})
        else:
            return redirect('/travello')


def displayResult(request):
    if request.method == 'POST':
        val1 = request.POST['num1']
        val2 = request.POST['num2']
        result = int(val1) + int(val2)
        return render(request, 'result.html', {'result' : result})
    else:
        return redirect('calculator')
