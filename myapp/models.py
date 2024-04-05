from django.db import models

# Create your models here.


# create category fields models

# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     desc = models.TextField()

#     def __str__(self):
#         return self.title

# create a image   modes for image

class Images(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
    timestamp = models.DateField()
    # cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class buyproduct(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images')
   
    # cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    message = models.TextField() 
    
    def __str__(self):
        return self.name   