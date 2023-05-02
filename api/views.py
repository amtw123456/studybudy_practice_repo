
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .serializers import RoomSerializer
from .models import Room
from .forms import RoomForm
# rooms = [
#     {'id':1, 'name':'Lets learn python!'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend Developers'},
# ]

# Create your views here.
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

def home(request):
    room = Room.objects.all()
    context = {'rooms':room}
    return render(request, 'api/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'api/room.html', context)

def createRoom(request): # POST METHOD THAT SAVES A NEW ROOM DATA TO THE api_room colleciton
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'api/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'api/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'api/delete.html', {'obj':room})