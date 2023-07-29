from django.contrib.auth import login
from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignupForm
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def homme(request):
    rooms=Rooms.objects.all()
    context={
        'rooms':rooms
    }
    return render(request,'chat/romms.html',context)
@login_required
def deleterooom(request,room_id):

    room=get_object_or_404(Rooms,id=room_id,user=request.user)
    room.delete()
    return redirect('home')
@login_required(login_url='login')
def roomchat(request,slug):
    theroom=Rooms.objects.get(slug=slug)
    messages=Message.objects.filter(room=theroom)[0:25]
    context={
        'theroom':theroom,
        'messages':messages

    }
    return render(request,'chat/roomchat.html',context)
@login_required
def createroom(request):
    if request.method=='POST':
        room_name=request.POST['roomname']
        description=request.POST['description']
        room=Rooms.objects.create(name=room_name,description=description,user=request.user)
        room.save()
        return redirect('home')
    
    return render(request,'roomcreate/createroom.html')
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect('home')
    else:
        form=SignupForm()
    context={
            'form':form
        }
    return render(request,'authentication/Signup.html',context)