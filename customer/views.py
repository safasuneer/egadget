from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View,ListView,DetailView
from account.models import products,Cart,Order
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
#decorator
def sigin_required(fn):
    def inner (request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,*kwargs)
        else:
            messages.error(request,"please login first!!")
            return redirect("home")
    return inner
docs=[never_cache,sigin_required]
# Create your views here.
@method_decorator([sigin_required],name='dispatch')

class CustomerHomeView(ListView):
    template_name="cust_home.html"
    # model=products
    queryset=products.objects.all()
    context_object_name="pro"
    


# class ProductdetailView(View):
#     def get(self,request,**kwargs):
#         pid=kwargs.get('id')
#         pro=products.objects.get(id=pid)
#         return render(request,"products_details.html",{"data":pid})

@method_decorator([sigin_required],name='dispatch')

class ProductDetailView(DetailView):
    template_name="product_details.html"
    pk_url_kwarg='id'
    queryset=products.objects.all()
    context_object_name='data'

def addcart(request,*args,**kwargs):
    id=kwargs.get("id")
    pro=products.objects.get(id=id)
    user=request.user
    qty=request.POST.get('qnt')
    Cart.objects.create(product=pro,user=user,quantity=qty)
    messages.success(request,"add to cart!!")
    return redirect('custhome')

@method_decorator([sigin_required],name='dispatch')

class CartListView(ListView):
    template_name='cart.html'
    queryset=Cart.objects.all()
    context_object_name='cart'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user,status='cart')
    
def removecart(request,**kwargs):
    pid=kwargs.get("id")
    c=Cart.objects.get(id=pid)
    c.delete()
    messages.success(request,"Cart Item Removed!!")
    return redirect('clist')

@method_decorator([sigin_required],name='dispatch')

class PaymentView(TemplateView):
    template_name="payment.html"


    def post(self,request,*args,**kwargs):
        cid=kwargs.get("id")
        cart=Cart.objects.get(id=cid)
        ad=request.POST.get("address")
        ph=request.POST.get("phone")
        Order.objects.create(cart=cart,address=ad,phone=ph)
        cart.status='Order placed'
        cart.save()
        messages.success(request,"Order placed Successfully!!!")
        return redirect("clist")
    
@method_decorator([sigin_required],name='dispatch')

class OrderListView(ListView):
        template_name="orders.html"
        queryset=Order.objects.all()
        context_object_name="order"

        def get_queryset(self):
            return Order.objects.filter(cart__user=self.request.user)

def cancelorder(request,*args,**kwargs):
    oid=kwargs.get("id")
    order=Order.objects.get(id=oid) 
    order.status='Cancelled'  
    order.save()
    messages.success(request,"Order cancelled!!")
    return redirect('olist')


    
