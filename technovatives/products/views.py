from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from products.models import products
from cart.models import cart_items
from django.shortcuts import get_object_or_404

# Products
def index(request):
    product = products.objects.all()
    return render(request,'index.html',{
        'products':product,
    })
def getproducts(request):
    product = products.objects.all()
    return render(request,'products.html',{
        'products':product,
    })
def getproduct(request, request_id):
    product = products.objects.get(id=request_id)
    return render(request,'shop-detail.html',{
        'product':product,
    })
def CreateProduct(request):
    newProduct = products(name = request.POST['name'],
                               price = request.POST['price'], 
                               img = request.POST['img'])    
    newProduct.save()
    return HttpResponseRedirect('/products/')  
def deleteProduct(request,request_id):
    request_to_delete = products.objects.get(id=request_id)
    request_to_delete.delete()
    return HttpResponseRedirect('/products/')    

def checkout(request):
    all_items = cart_items.objects.all()
    total = 0
    tax = 0
    for c in all_items:
        total += int(c.price)
        tax = 0.05 * total
    total_amount = total + tax    
    return render(request,'checkout.html',
    {
        'cart_all' : all_items,
        'total': total_amount,
        'tax': tax,
    })                   

def about(request):
    return render(request,'about.html')   

def contactus(request):
    return render(request,'contact-us.html')
