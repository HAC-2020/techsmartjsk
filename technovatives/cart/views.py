from django.shortcuts import render
from cart.models import cart_items
from django.http import HttpResponseRedirect

#Cart Items
def add_to_cart(request):
    newitem = cart_items(name = request.POST['name'],
                    price = request.POST['price'], 
                    img = request.POST['img'])    
    newitem.save()   
    return HttpResponseRedirect('/cart/') 

def cart_all_items(request):
    all_items = cart_items.objects.all()
    total = 0
    tax = 0
    for c in all_items:
        total += int(c.price)
        tax = 0.05 * total
    total_amount = total + tax    
    return render(request,'cart.html',
    {
        'cart_all' : all_items,
        'total': total_amount,
        'tax': tax,
    })

def delete_cart_item(request,item_id):
    item_to_delete = cart_items.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/cart/')
