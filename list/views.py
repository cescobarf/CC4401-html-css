from django.shortcuts import render, redirect
from .models import Item


# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {'items': items}

    return render(request, 'list/index.html', context)

def add(request):
    item = Item(name=request.POST['item-name'])
    item.save()
    return redirect('list:index')

def delete(request):
    item = Item.objects.get(pk=request.POST['delete-pk'])
    item.delete()
    return redirect('list:index')

def decrease(request):
    item = Item.objects.get(pk=request.POST['decrease-pk'])
    if item.quantity > 0:
        item.quantity -= 1
        item.save()
    return redirect('list:index')

def increase(request):
    item = Item.objects.get(pk=request.POST['increase-pk'])
    item.quantity += 1
    item.save()
    return redirect('list:index')