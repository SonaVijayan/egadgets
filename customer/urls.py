from django.urls import path
from .views import *



urlpatterns=[
    path('home',CustomerHomeView.as_view(),name='home'),
    path('plist/<str:cat>',ProductListView.as_view(),name='plist'),
    path('pdetail/<int:pid>',ProductDetailView.as_view(),name='pdetail'),
    path('addtocart/<int:pid>',addToCart,name='addtocart'),
    path('cartlist',CartListView.as_view(),name='cartlist'),
    path('inc/<int:id>',increaseQuantity,name='inc'),
     path('dec/<int:id>',decreaseQuantity,name='dec'),
      path('deleteitem/<int:id>',deleteCartItem,name='deleteitem'),
      path('porder/<int:id>',placeOrderView,name='porder'),
       path('orderlist',OrderListView.as_view(),name='orders'),
       path('corder/<int:id>',cancelOrder,name='corder'),
   
    


]
