import random
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def password(request):
    try:
        characters = list()

        if request.GET.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
        if request.GET.get('lowercase'):
            characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

        if request.GET.get('special'):
            characters.extend(list('~!@#$%^&*()_+"\/-?><.:;'))

        if request.GET.get('number'):
            characters.extend(list('0123456789'))

        length = int(request.GET.get('length', 14))
        thepassword = ''

        for data in range(length):
            thepassword += random.choice(characters)

    except:
        thepassword = 'Error : Select an option to generate password...'
    
    return render(request, 'password.html', {'password' : thepassword})

def auto_password(request):
    try:
        characters = list()

        uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')        
        lowercase = list('abcdefghijklmnopqrstuvwxyz')
        special = list('~!@#$%^&*()_+"\/-?><.:;')
        number = list('0123456789')
        datetime_var = str(datetime.today())

        characters.extend(uppercase)
        characters.extend(lowercase)
        characters.extend(special)
        characters.extend(number)
        characters.extend(datetime_var)
        
        length = int(12)
        thepassword = ''

        for data in range(length):
            thepassword += random.choice(characters)

    except:
        thepassword = 'Error : Select an option to generate password...'
    
    return render(request, 'password.html', {'password' : thepassword})


def about(request):
    return render(request, 'about.html')