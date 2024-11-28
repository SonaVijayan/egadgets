from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from account.models import Products,Cart,Orders
from django.contrib import messages

# # Create your views here.
# class CustomerHomeView(View):
#     def get(self,request):
#         return render(request,'home.html')

class CustomerHomeView(TemplateView):
    template_name='home.html'


class ProductListView(ListView):
    template_name='productlist.html'
    queryset=Products.objects.all()
    context_object_name="products"
    def get_queryset(self):
        cat=self.kwargs.get('cat')
        return self.queryset.filter(category=cat)
    
class ProductDetailView(DetailView):
    template_name='productdetail.html'
    queryset=Products.objects.all()
    context_object_name="product"
    pk_url_kwarg="pid"

def addToCart(request,*args,**kwargs):
    try:
        pid=kwargs.get('pid')
        product=Products.objects.get(id=pid)
        user=request.user
        cartcheck=Cart.objects.filter(product=product,user=user).exists()
        if cartcheck:
            cartitem=Cart.objects.get(product=product,user=user)
            cartitem.quantity+=1
            cartitem.save()
            messages.success(request,'CartItem quantity incraesed!!!')
            return redirect('home')
        else:
            cartitem=Cart.objects.create(product=product,user=user)
            messages.success(request,f"{product.title}Added to Cart")
            return redirect('home')
    except Exception as e:
        print(e)
        messages.warning(request,"Something went wrong")
        return redirect('home')
        
class CartListView(ListView):
    template_name='cartlist.html'
    queryset=Cart.objects.all()
    context_object_name="carts"
    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
        return qs
    
def increaseQuantity(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        cart.quantity+=1
        cart.save()
        return redirect('cartlist')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('cartlist')
    
def decreaseQuantity(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        if cart.quantity == 1:
            cart.delete()
            return redirect('cartlist')
        else:
          cart.quantity -= 1
          cart.save()
        return redirect('cartlist')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('cartlist')
    
def deleteCartItem(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        cart.delete()
        messages.success(request,"Items Removed from Cart!!!")
        return redirect('cartlist')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('cartlist')
    
def placeOrderView(request,*args,**kwargs):
    try:
        cid=kwargs.get('id')
        cart=Cart.objects.get(id=cid)
        Orders.objects.create(product=cart.product,user=request.user,quantity=cart.quantity)
        cart.delete()
        messages.success(request,f'{cart.product.title}\'s Order Placed!!!')
        return redirect('cartlist')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('cartlist')
    
class OrderListView(ListView):
    template_name='orders.html'
    queryset=Orders.objects.all()
    context_object_name="orders"
    def get_queryset(self):
        qs=self.queryset.filter(user=self.request.user)
        return qs

    
def cancelOrder(request,*args,**kwargs):
    try:
        oid=kwargs.get('id')
        order=Orders.objects.get(id=oid)
        order.status="Cancelled"
        order.save()
        messages.success(request,"Order Cancelled!!")
        return redirect('orders')
    except:
        messages.warning(request,"Something Went Wrong!!")
        return redirect('orders')
    
        



