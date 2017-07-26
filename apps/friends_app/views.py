from django.shortcuts import render, redirect

from .models import *

def index(request):
    
    request.session['user_id'] = 1 

    print '########', request.session['user_id']

    context = {
        'users':User.objects.all(),
        'sorted_friends':Friend.objects.all().filter(user=request.session['user_id']).order_by('created_at')[:3],
    }

    return render(request, 'friends_app/index.html', context)


def all_friends(request):

    context = {
        'friends':Friend.objects.all(),
        'count':Friend.objects.filter(user=request.session['user_id']).count()
    }

    return render(request, 'friends_app/friends.html', context)


def add_friend(request):
    
    context = {
        'users':User.objects.all().exclude(id=request.session['user_id']).exclude()
    }

    return render(request, 'friends_app/add_friend.html', context)


def process_friend(request, id):

    Friend.objects.addFriend(id, request.session['user_id'])

    return redirect('/friends_app/add_friend')