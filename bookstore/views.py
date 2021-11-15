#from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from django.db.models import query
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.utils.translation import gettext as _

# Create your views here.
from .models import *
from .forms import OrderForm,CreateNewUser,CustomerForm  #,NameForm    #, CommandForm  # 1,2,3=forms.py,
from django.forms import  inlineformset_factory  # pour formset dans [my_order_form.html]

from django.contrib import messages  # pour envoier message des errors "forms"  "register.html"
from django.contrib.auth.forms import UserCreationForm  # [veiws == register] user auth et [forms.py]
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required # decorators = [cachee les fonction]---> aller ou login direct
from .decorators import notLoggedUsers,allowedUsers,forAdmins   #file decorators.py

from django.contrib.auth.models import Group

# from django.core.paginator import Paginator



import requests
from django.conf import settings




# from django.contrib.auth.decorators import login_required

# from .models import Notification
# from bookstore.utilities import create_notification

# @login_required
# def notifications(request):
#     goto = request.GET.get('goto', '')
#     notification_id = request.GET.get('notification', 0)
#     extra_id = request.GET.get('extra_id', 0)

#     if goto != '':
#         notification = Notification.objects.get(pk=notification_id)
#         notification.is_read = True
#         notification.save()

#         if notification.notification_type == Notification.MESSAGE:
#             return redirect('view_application', application_id=notification.extra_id)
#         elif notification.notification_type == Notification.APPLICATION:
#             return redirect('view_application', application_id=notification.extra_id)
    
#     return render(request, 'bookstore/notifications.html')


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

    # product_objet=Article.objects.all()
    # # article=request.GET.get('article')
    # # if article !='' and article is not None:
    # #     product_objet=Article.objects.filter(title_iconctains=article)
    # paginator=Paginator(product_objet, 5)
    # page=request.GET.get('page')
    # product_objet=paginator.get_page(page)



    
    orders = Order.objects.all()
    t_orders = orders.count()
    p_orders = orders.filter(status='pending').count()
    d_orders = orders.filter(status='Delivered').count()
    in_orders = orders.filter(status='in progress').count()
    out_orders = orders.filter(status='out of order').count()
    # list_articles=Article.objects.all()
    context = {
                'orders': orders,
                't_orders':t_orders,
                'p_orders': p_orders,
                'd_orders': d_orders,
                'in_orders': in_orders,
                'out_orders': out_orders}
                # 'list_articles':list_articles}
                # 'product_objet':product_objet}
    
    

    return render(request,'bookstore/profile.html', context)

@login_required(login_url='login') 
# @allowedUsers(allowedGroups=['customer'])
def ProfileInfo(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form =CustomerForm(request.POST ,request.FILES ,instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form} # [profile_info.html],[my_order_form.html],[update.html]
    

    return render(request,'bookstore/profile_info.html', context)


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def detail(request,id_article):
    #ident =Order.objects.get(id=pk)
    article =Article.objects.get(id=id_article)
    category=article.category
    articles_en_relation=Article.objects.filter(category=category)[:2]  #pour nbrs max qui vas afficher art
    context={'article':article,
             "aer":articles_en_relation
    }
    #print("l'identite de l'article est : " ,id_article)
    return render(request,'bookstore/detail.html',context)


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def search(request):
    # GET={"article":"cafe"}
    query=request.GET["article"]
    List_article=Article.objects.filter(title__icontains=query)
    return render(request,"bookstore/search.html",{"List_article":List_article})


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def shop(request):
    article=Article.objects.all()
    # itme-name=request.GET.get('itme-name')
    # if itme-name !='' and itme-name is not None:
    #     product_objet=Article.objects.filter(title__iconctains=itme-name)
    list_articles=Article.objects.all()
    paginator=Paginator(list_articles, 4)
    page=request.GET.get('page')
    list_articles=paginator.get_page(page)
    # list_articles=Article.objects.all()
    context={'article':article,'list_articles':list_articles}


    return render(request,'bookstore/base.html',context)


@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
# def checkout(request,id_cmd):
def checkout(request,id_cmd):
    article =Article.objects.get(id=id_cmd)
    # query=request.GET["article"]
    # article =Article.objects.get(id=id_cmd)

    # article = request.article.title
    # tit = CommandForm(instance=article)
    if request.method =="POST":
        items = request.POST.get('items')
        # items = NameForm(request.POST)
        # if items.is_valid():
        #     #return HttpResponseRedirect('/thanks/')
        #     return redirect('confirmation')
        # else:
        #     items = NameForm()
        # total = request.POST.get('total')
        # tit =request.POST.get('tit')
        # tit = NameForm(request.POST)
        # tit =CommandForm(request.POST ,request.FILES ,instance=article)
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        numerophone = request.POST.get('numerophone')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        payerpar = request.POST.get('payerpar')
        numcart = request.POST.get('numcart')
        com =Commande(items=items,  nom=nom ,email=email ,  address=address , numerophone=numerophone ,  ville=ville,
        pays=pays , zipcode=zipcode, payerpar=payerpar ,numcart=numcart)
        com.save()
        return redirect('confirmation')

    return render(request,'bookstore/checkout.html')
    # ,{'id_cmd':id_cmd})

@login_required(login_url='login')
@allowedUsers(allowedGroups=['customer'])
def confirmation(request):
    info =Commande.objects.all()[:1]
    for item in info:
        nom =item.nom
    return render(request,'bookstore/conf.html',{"nom":nom})


# @login_required(login_url='login')
# @allowedUsers(allowedGroups=['customer'])
# def notification(request):
#     if request.user.is_authencticated:
#         return {'notification':request.user.notification.filter(is_read=False)}
#     else:
#         return {'notification': []}

#  return render(request, 'bookstore/notification.html')

# @login_required(login_url='login')
# @allowedUsers(allowedGroups=['customer'])
# def notification(request):
#     goto = request.GET.get('goto', '')
#     notification_id = request.GET.get('notification', 0)
#     extra_id = request.GET.get('extra_id', 0)

#     if goto != '':
#         notification = Notification.objects.get(pk=notification_id)
#         notification.is_read = True
#         notification.save()

#         if notification.notification_type == Notification.MESSAGE:
#             return redirect('view_application', 
# application_id=notification.extra_id)
#         elif notification.notification_type == Notification.APPLICATION:
#             return redirect('view_application', 
# application_id=notification.extra_id)

#     return render(request, 'web/notification.html')




# @login_required(login_url='login')
# @allowedUsers(allowedGroups=['customer'])
# def sms(request):
#     message=request.GET['body']
#     message_splited=message-split("-")
#     title=message_splited[0]
#     desc=message_splited[1]

#     agri_category=Category.objects.get(id=2)
#     article=Article(title=title,category=agri_category,desc=desc,image="http://default")
#     article.save()
#     print('data saved successfully')
#     return HttpResponse("data saved succesfully")







# def handle_server_error(request):
#     return render(request,'server_error.html')