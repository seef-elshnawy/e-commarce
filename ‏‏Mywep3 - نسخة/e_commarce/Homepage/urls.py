from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('',views.index,name='index'),
path('Sign',views.sign,name='sign'),
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('profile',views.profile,name='profile'),
path('product-men',views.productmen,name='men'),
path('product-women',views.productwomen,name='women'),
path('<int:Productmen_id>',views.productId,name='productId'),
path('Mycart',views.addtocart,name='addtocart'),
path('cart',views.updateCart,name='cart'),
path('remove/<int:Productmen_id>',views.remove,name='remove'),
#path('Mycart',views.addtocart2,name='addtocart1')
]
