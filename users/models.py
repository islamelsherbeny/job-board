from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

class Profile(models.Model):
    #cascade means if a user is deleted them the profile will be deleted bt if profile is deleted then user still exist
    user = models.OneToOneField(User, on_delete = models.CASCADE)   
    #one user have one orofile and one profile can have one user
    #you can add bio or current city but now we will add image 
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
    
    #lesson 8 4.00
    #then you need to make migration 
    #first install pillow to deal with images
    # command    python manage.py makemigrations
    #python manage.py migrate
    #don't forget to add it in admin 
    def __str__(self):
        return f'{self.user.username} profile'
    
    #here i want to overwrite the save method to resize the profile picture
    #there is alof of ways to resize image ...this is easy
    def save(self):
        #i will run it with parent using super user
        super().save()
        #now i will open the image
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            #save it in the same path pass the same arguments
            img.save(self.image.path)
            #then i might need to write code to delete the old images after updating 