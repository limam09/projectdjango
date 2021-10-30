#from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import OrderForm,CreateNewUser,CustomerForm   # 1,2,3=forms.py,
from django.forms import  inlineformset_factory  # pour formset dans [my_order_form.html]

from django.contrib import messages  # pour envoier message des errors "forms"  "register.html"
from django.contrib.auth.forms import UserCreationForm  # [veiws == register] user auth et [forms.py]
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required # decorators = [cachee les fonction]---> aller ou login direct
from .decorators import notLoggedUsers,allowedUsers,forAdmins   #file decorators.py

from django.contrib.auth.models import Group


import requests
from django.conf import settings


@login_required(login_url='login')
#@allowedUsers(allowedGroups=['admin'])    #il faut que dans group [admin]
@forAdmins    # for 'admin' unique show file [decorators.py]
def home(request):
    # pics = Image.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    t_orders = orders.count()
    p_orders = orders.filter(status='pending').count()
    d_orders = orders.filter(status='Delivered').count()
    in_orders = orders.filter(status='in progress').count()
    out_orders = orders.filter(status='out of order').count()
    context = {'customers': customers ,
                'orders': orders,
                't_orders':t_orders,
                'p_orders': p_orders,
                'd_orders': d_orders,
                'in_orders': in_orders,
                'out_orders': out_orders}
                # 'pics':pics}
    return render(request , 'bookstore/dashboard.html',context)

@login_required(login_url='login')
@forAdmins
def books(request):
    books=Book.objects.all()
    return render(request,'bookstore/books.html',{'look':books})


@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    number_orders =orders.count()
    # searchFilter = OrderFilter(request.GET ,querySet =orders)
    # orders =searchFilter.qs
    
    context = {'customer': customer ,
                'orders': orders, 'number_orders': number_orders}
    return render(request,'bookstore/customer.html', context)

# def create(request):
#     form = OrderForm()
#     if request.method == 'POST' :
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {'form':form}

#     return render(request,'bookstore/my_order_form.html', context)

@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def create(request,pk):
    OrderFormSet =inlineformset_factory(Customer,Order,fields=('book','status'),extra=4)
    customer =Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
    #form = OrderForm()
    if request.method == 'POST' :
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    #context = {'form':form}
    context = {'formset':formset}

    return render(request,'bookstore/my_order_form.html', context)

@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def update(request,pk):
    order =Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST' :
        form = OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}

    return render(request,'bookstore/update_form.html', context)

@login_required(login_url='login')
@allowedUsers(allowedGroups=['admin'])
def delete(request,pk):
    order =Order.objects.get(id=pk)
    if request.method == 'POST' :
        order.delete()
        return redirect('/')
    context = {'order':order}

    return render(request,'bookstore/delete_form.html', context)

# def login(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     context = {}

#     return render(request,'bookstore/login.html', context)

@notLoggedUsers  #file --->decorators.py
def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateNewUser()
    if request.method == 'POST':
            form = CreateNewUser(request.POST)
            if form.is_valid():

             recaptcha_response = request.POST.get('g-recaptcha-response')
             data = {
                 'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                 'response': recaptcha_response 

                 }
             r =requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
             result = r.json() 
             if result['success']:   
                user = form.save()
                username = form.cleaned_data.get('username')
                # group = Group.objects.get(name="customer")    3quand on enrgister en niveau user devient direct dans group [customer]
                # user.groups.add(group)
                messages.success(request ,username + ' Created Sucessfully !')
                return redirect('login')
            else:
               messages.error(request , 'InValid Recaptcha please try again !') 
    context ={'form':form}

    return render(request,'bookstore/register.html', context)

@notLoggedUsers      #file --->decorators.py
def userLogin(request):
    # if request.user.is_authenticated:      #file --->decorators.py {func: wrapper_func}
    #     return redirect('home')
    # else:
        if request.method == 'POST':
           username= request.POST.get('username')
           password= request.POST.get('password')
           user = authenticate(request,username = username, password=password )
           if user is not None:
            login(request, user)
            return redirect('home')
           else:
            messages.info(request, 'Credentials error')
        context ={}

        return render(request,'bookstore/login.html', context)

def userLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def userProfile(request):
    orders = request.user.customer.order_set.all()

    
    orders = Order.objects.all()
    t_orders = orders.count()
    p_orders = orders.filter(status='pending').count()
    d_orders = orders.filter(status='Delivered').count()
    in_orders = orders.filter(status='in progress').count()
    out_orders = orders.filter(status='out of order').count()
    list_articles=Article.objects.all()
    context = {
                'orders': orders,
                't_orders':t_orders,
                'p_orders': p_orders,
                'd_orders': d_orders,
                'in_orders': in_orders,
                'out_orders': out_orders,
                'list_articles':list_articles}
    
    

    return render(request,'bookstore/profile.html', context)


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def detail(request,id_article):
    #ident =Order.objects.get(id=pk)
    article =Article.objects.get(id=id_article)
    category=article.category
    articles_en_relation=Article.objects.filter(category=category)[:5]  #pour nbrs max qui vas afficher art
    context={'article':article,
             "aer":articles_en_relation
    }
    #print("l'identite de l'article est : " ,id_article)
    return render(request,'bookstore/detail.html',context)


@login_required(login_url='login') 
#@allowedUsers(allowedGroups=['customer'])
def ProfileInfo(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form =CustomerForm(request.POST ,request.FILES ,instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form} # [profile_info.html],[my_order_form.html],[update.html]
    

    return render(request,'bookstore/profile_info.html', context)





# def handle_server_error(request):
#     return render(request,'server_error.html')