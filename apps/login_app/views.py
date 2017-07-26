from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *


def index(request):
    print 'In home page...'
    return render(request, 'index.html')


def registration(request):
    print 'View says: Creating registration...'
    errors = User.objects.register(request.POST)
    
    try:
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags='tag')
                print 'View says:', error
                return redirect('/')
    except TypeError:
        print 'View says: TypeError'

    context = { 'display_name':request.POST['first_name']}
    return render(request, 'success.html', context)


def login(request):
    print 'View says: logging in...'
    user_logged_in = User.objects.login(request.POST)
    
    if user_logged_in:
        user = User.objects.get(email=request.POST['login_email'])
        # return render(request, 'friends_app/index.html')
        return redirect('friends_app/')
    else:
        context = { 'login_failed':'You have entered invalid credentials.'}
        return render(request, 'index.html', context)
