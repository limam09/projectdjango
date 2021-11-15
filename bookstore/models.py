from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.enums import Choices
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User ,null=True ,on_delete=models.CASCADE)
    name =models.CharField(max_length=190, null=True)
    email =models.CharField(max_length=190, null=True)
    phone =models.CharField(max_length=190, null=True)
    age =models.CharField(max_length=190, null=True)
    avatar = models.ImageField(blank=True,null=True, default='person.png')
    date_created =models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self) :
        return self.name

class Tag(models.Model):
    name =models.CharField(max_length=190, null=True)

    def __str__(self) :
        return self.name

class Book(models.Model):
    CATEGORY =(
        ('classics','classics'),
        ('comik book','comik book'),
        ('Fantasy','Fantasy'),
        ('horror','horror')
    )
    name =models.CharField(max_length=190, null=True)
    author =models.CharField(max_length=190, null=True)
    price =models.FloatField( null=True)
    category =models.CharField(max_length=190, null=True,choices=CATEGORY)
    description =models.CharField(max_length=190, null=True)
    tags =models.ManyToManyField(Tag)
    date_created =models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) :
        return self.name



class Order(models.Model):
    STATUS =(
        ('pending','pending'),
        ('Delivered','Delivered'),
        ('in progress','in progress'),
        ('out of order','out of order')
    )
    STATUS_fr =(
        ('pending','pending'),
        ('Delivered','Delivered'),
        ('in progress','in progress'),
        ('out of order','out of order')
    )
    customer =models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    book =models.ForeignKey(Book,null=True,on_delete=models.SET_NULL)
    tags =models.ManyToManyField(Tag)
    date_created =models.DateTimeField(auto_now_add=True, null=True)
    status=models.CharField(max_length=200, null=True,choices=STATUS)


# class Image(models.Model):
#     caption=models.CharField(max_length=50)
#     image=models.ImageField(upload_to="img/%y")
#     def __str__(self):
#         return self.caption
class Category(models.Model):
    name=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=50)
    # title_ar=models.CharField(max_length=50)
    title_fr=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    # desc_ar=models.TextField()
    desc_fr=models.TextField()
    image=models.ImageField()
    # price=models.CharField(max_length=150)
    price=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Commande(models.Model):
    items=models.CharField(max_length=300)
    # total=models.CharField(max_length=200)
    # tit =models.ForeignKey(Article,on_delete=models.CASCADE,default="anything")
    nom = models.CharField(max_length=150)
    email=models.EmailField()
    address =models.CharField(max_length=200)
    numerophone=models.CharField(max_length=200)
    ville=models.CharField(max_length=200)
    pays=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=300)
    payerpar=models.CharField(max_length=300)
    numcart=models.CharField(max_length=300)
    date_commande= models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ['-date_commande']
        # fields =['tit',]

    def __str__(self):
        return self.nom


# class Notification(models.Model):
#     MESSAGE ='message'
#     APPLICATION ='application'

#     CHOICES =(
#         (MESSAGE,'Message'),
#         (APPLICATION, 'Application')
#     )

#     # order =models.ForeignKey(Order,related_name='notification',on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
#     notification_type= models.CharField(max_length=20,choices=CHOICES)
#     is_read =models.BooleanField(default=False)
#     extra_id= models.IntegerField(null=True, blank=True)
#     created_at=models.DateTimeField(auto_now_add=True)
#     created_by=models.ForeignKey(Order,related_name='creatednotification',on_delete=models.CASCADE)
    

#     class Meta:
#         ordering =['-created_at']


# class Notification(models.Model):
#     MESSAGE = 'message'
#     APPLICATION = 'application'

#     CHOICES = (
#         (MESSAGE, 'Message'),
#         (APPLICATION, 'Application')
#          )

#     to_member = models.ForeignKey(Member, related_name='notification', on_delete=models.CASCADE)
#     notification_type = models.CharField(max_length=20, choices=CHOICES)
#     is_read = models.BooleanField(default=False)
#     extra_id = models.IntegerField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(Member, related_name='creatednotifications', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ['created_at']