from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *

def index(request):
    return render(request, 'index.html')

def add_guest(request):
    is_shu_friend_relative = False
    if request.POST.get('is_shu_friend_relative'):
        is_shu_friend_relative = True
    is_peggy_friend_relative = False
    if request.POST.get('is_peggy_friend_relative'):
        is_peggy_friend_relative = True
    
    errors=Guest.objects.validator(
        request.POST, is_shu_friend_relative, is_peggy_friend_relative)

    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/#rsvp')

    diet_restriction = 'none'
    other_diet_message = ''
    if request.POST.get('diet_restriction'):
        diet_restriction = request.POST['diet_restriction']
        if diet_restriction == 'others':
            other_diet_message = request.POST['other']
    
    message = ''
    if request.POST.get('message'):
        message = request.POST['message']
    
    print(message)

    full_name=request.POST['full_name']
    email=request.POST['email']
    number_of_guests=int(request.POST['number_of_guests'])
    
    Guest.objects.create(
        full_name=full_name, email=email, is_shu_friend_relative=is_shu_friend_relative,
        is_peggy_friend_relative=is_peggy_friend_relative,
        number_of_guests=number_of_guests, diet_restriction=diet_restriction,
        diet_message=other_diet_message, message=message)
    return redirect('/submited')

def submited(request):
    return render(request, 'submited.html')