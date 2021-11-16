from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import(
  AbstractBaseUser,BaseUserManager,PermissionsMixin
)
from django.conf import settings
# Create your models here.
class Country(models.Model):
 code=models.AutoField(primary_key=True)   
 Countrys=models.CharField(max_length=64)
 def __str__(self):
  return f'{self.Countrys}' 

#class Usersmanger(BaseUserManager):
 
#  def create_staffuser(self,user_name,email,password,Phone,first_name,last_name,**other_fields):

#    other_fields.setdefault('is_superuser',False)
#    other_fields.setdefault('active',True)
#    other_fields.setdefault('is_staff',True)
#    return self.create_user(user_name,email,password,Phone,first_name,last_name,**other_fields)

#  def create_superuser(self,user_name,email,password,Phone,first_name,last_name,**other_fields):

#    other_fields.setdefault('is_superuser',True)
#    other_fields.setdefault('active',True)
#    other_fields.setdefault('is_staff',True)
#    return self.create_user(user_name,email,password,Phone,first_name,last_name,**other_fields)

# def create_user(self,user_name,email,password,Phone,first_name,last_name,**other_fields):
#   if not email:
#     raise TypeError('user must have email')
#   if not password:
#   raise TypeError('user must have password')  
#   user_obj=self.model( 
#   user_name=user_name,  
#   email=email,
#   Phone=Phone,
#   first_name=first_name,
#   last_name=last_name,
#   **other_fields
# )
#   user_obj.set_password(password)
#   user_obj.save(using=self._db)
#   return user_obj

 

class Users(AbstractBaseUser):
 id=models.AutoField(primary_key=True,auto_created=True)
 first_name=models.CharField(max_length=64,blank=True)
 last_name=models.CharField(max_length=64,blank=True)
 user_name=models.CharField(max_length=64,unique=True)
 email=models.EmailField(_('email address'),unique=True)
 Phone=models.IntegerField()
 password=models.CharField(max_length=14)
 Password2=models.CharField(max_length=14)
 Thecountry=models.ForeignKey(Country,on_delete=models.CASCADE,default=1)
 active=models.BooleanField(default=True)
 is_staff=models.BooleanField(default=False)
 last_login=models.DateTimeField(auto_now_add=True)

 USERNAME_FIELD='user_name'
 REQUIRED_FIELDS=['first_name','last_name','email','Phone','password','Password2']
# object=Usersmanger()
 def __str__(self):
  return f'{self.id} Username: {self.user_name} Name: {self.first_name} {self.last_name} {self.last_login}'
 @property
 def is_admin(self):
   return {self.admin}
  
 @property
 def is_active(self):
   return {self.active}

Type_Choice=(
('c','Coat'),
('j','Jacket'),
('b','Balzer'),
('o','Other'),
('b','jambsoat'),
('o','badboy'),
('d','dress'),
('a','accsesoris'),
('s','other'),
)

class Productmen(models.Model):
 men='a'
 women='b'
 choice=(
  (men,'men'),
  (women,'women')
)
 id=models.AutoField(primary_key=True,auto_created=True)
 name=models.CharField(max_length=64)
 smalldesc=models.CharField(max_length=20,default='wonder-ful cloth')
 desc=models.CharField(max_length=60)
 desc1=models.CharField(max_length=60,blank=True)
 desc2=models.CharField(max_length=60,blank=True)
 desc3=models.CharField(max_length=60,blank=True)
 desc4=models.CharField(max_length=60,blank=True)
 desc5=models.CharField(max_length=60,blank=True)
 desc6=models.CharField(max_length=60,blank=True)
 desc7=models.CharField(max_length=60,blank=True)
 desc8=models.CharField(max_length=60,blank=True)
 desc9=models.CharField(max_length=60,blank=True)
 price=models.IntegerField()
 image2=models.ImageField(default='image.png')
 image3=models.ImageField(default='image.png')
 image=models.ImageField()
 mainType=models.CharField(choices=choice,max_length=15)
 Type=models.CharField(choices=Type_Choice,max_length=1)
  
 def __str__(self):
  return f'  {self.name}  -{self.price} $'
 
 def women(self):
   self.mainType =='women'

  
 def __str__(self):
  return f'  {self.name}  -{self.price} $'

class addtocarts(models.Model):
  id=models.AutoField(primary_key=True,auto_created=True)
  image=models.ImageField()
  name=models.CharField(max_length=64)
  price2=models.IntegerField()
  Total=models.PositiveIntegerField(null=True, blank=True)
  user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  #customer=models.OneToOneField(Customer,blank=True,on_delete=models.CASCADE,default=1)

  @property
  def get_total(self):
        total = self.Total * self.price2*20/100
        if total == 0.00:
            self.delete()
        return total

  def __str__(self):
     return f'{self.image.url} {self.name} {self.price2.get_total}$ {self.image} {self.Total}'


class cart(models.Model):
  id=models.AutoField(primary_key=True,auto_created=True)
  product=models.ForeignKey(Productmen,on_delete=models.CASCADE)
  user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  Total=models.PositiveIntegerField(null=True, blank=True,default=0)

  #customer=models.OneToOneField(Customer,blank=True,on_delete=models.CASCADE,default=1)

  def __str__(self):
     return f'order:{self.product.id} {self.id} {self.product}'
  @property
  def get_total(self):
        total = self.Total *self.product.price +self.product.price*20/100
        if total == 0.00:
          self.delete()
        return total

  def image(self):
   image=self.product.image.url
   return image
  def price(self):
    price= self.product.price
    return price
  def name(self):
    name= self.product.name
    return name    

class addtocarts2(models.Model):
  id=models.AutoField(primary_key=True,auto_created=True)
  image=models.ImageField()
  name=models.CharField(max_length=64)
  price2=models.IntegerField()
  Total=models.PositiveIntegerField(null=True, blank=True)
  user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
  order=models.ManyToManyField(cart,blank=True)

  #customer=models.OneToOneField(Customer,blank=True,on_delete=models.CASCADE,default=1)
  @property
  def get_total(self):
        total = self.Total * self.price2
        if total == 0.00:
            self.delete()
        return total

  def __str__(self):
     return  f'{self.image.url} Name:{self.user}  Order_Name: {self.name} Price:  {self.get_total}$ Quantity:{self.Total}'


class cartorder(models.Model):
  id=models.AutoField(primary_key=True,auto_created=True)
  carts=models.ForeignKey(cart,on_delete=models.CASCADE)
  def __str__(self):
     return f'{self.carts.user}: {self.carts.product.name} {self.carts.product.price}$ {self.Total}'