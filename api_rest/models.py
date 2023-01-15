from django.db import models

# Create your models here.

# model for user
class Tribe(models.Model):
    name = models.CharField(max_length=30)
    charge = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

# model for the ministry
class Ministry(models.Model):
    name = models.CharField(max_length=30)
    charge = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
        
# model for red
class Red(models.Model):
    name = models.CharField(max_length=30)
    charge = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
            
# model for user membership 
class Membership(models.Model):
    name = models.CharField(max_length=50)
    surname_paternal = models.CharField(max_length=30)
    surname_maternal = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    date_of_birth = models.DateTimeField("date birthday")
    red = models.ForeignKey(Red,on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry,on_delete=models.CASCADE)
    tribe = models.ForeignKey(Tribe,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

#model for users
class Users(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



