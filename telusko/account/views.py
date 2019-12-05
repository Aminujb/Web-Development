from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):

    if request.method == 'POST':
        print('I am in')
        l_username = request.POST.get('login_username')
        l_password = request.POST.get('login_password')

        user = auth.authenticate(username= l_username, password = l_password)
        if user is not None:
            auth.login(request, user)
            return redirect('/calc/home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username_client = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        collections = [first_name, last_name, username_client, password1, password2]
        for val in collections:
            if val == '':
                messages.info(request, 'No field can be empty')
                return redirect('/account/register')
            else:
                
                if password1 == password2:
                    
                    if User.objects.filter(username=username_client).exists():
                        messages.info(request, 'Username taken')
                        return redirect('/account/register')

                    elif User.objects.filter(email=email).exists():
                        messages.error(request, 'email taken')
                        return redirect('/account/register')
                        
                    else:
                        user = User.objects.create_user(
                            username=username_client,
                            password=password1,
                            email=email,
                            first_name=first_name,
                            last_name=last_name,
                        )
                        user.save()
                        print('user created')
                        return redirect('travello') #fix this direction
                else:
                    messages.error(request, 'Password not matching')
                return redirect('/account/register')

    return render(request, "register.html")

