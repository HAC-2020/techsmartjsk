from django.conf import settings
if settings.DEBUG:
    from django.contrib import admin
    from django.conf.urls.static import static
    from django.urls import path
    from products.views import getproducts, CreateProduct,deleteProduct,getproduct,index,checkout,about,contactus
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from cart.views import add_to_cart,cart_all_items
    urlpatterns = [
        path('',index),
        path('admin/', admin.site.urls),
        path('products/',getproducts),
        path('products/add/',CreateProduct),
        path('products/<int:request_id>/delete/',deleteProduct),
        path('products/<int:request_id>/',getproduct),
        path('cartItem/add/',add_to_cart),
        path('checkout/',checkout),
        path('cart/',cart_all_items),
        path('about/',about),
        path('contactus/',contactus)
    ]

    urlpatterns += staticfiles_urlpatterns()
