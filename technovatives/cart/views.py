from django.shortcuts import render
from cart.models import cart_items
from django.http import HttpResponseRedirect
#Cart Items
def add_to_cart(request):
    if request.method == 'POST':
        try:
            newitem = cart_items(name = request.POST['name'],
                               price = request.POST['price'], 
                               img = request.POST['img'])    
            newitem.save()
        except:
            print('Error')    
    return HttpResponseRedirect('/') 

def cart_all_items(request):
    all_items = cart_items.objects.all()
    return render(request,'cart.html',
    {
        'cart_all' : all_items
    })

