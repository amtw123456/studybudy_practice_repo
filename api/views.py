from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend Developers'},
# ]

# Create your views here.
def home(request):
    room = Room.objects.all()
    context = {'rooms':room}
    return render(request, 'api/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'api/room.html', context)