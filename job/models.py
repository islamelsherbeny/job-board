from collections import UserDict
from django.db import models
from django.db.models.deletion import CASCADE
from  django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
#you will enherit from models

'''
django model field : 
    - html widget
    - validation 
    - db size 

make this for every time you make a changes in model
    (job_board) λ python manage.py makemigrations
    (job_board) λ python manage.py migrate
    
model field django documentation
'''
JOB_TYPE= (
    ('Full time','full time'),
    ('Part time','part time'),
)


#instance : the object you will upload ==> the image
def image_upload(instace,filename):
    imagename , extension = filename.split('.')
    #02:10   don't forget rhe structure of your file system 
    return "jobs/%s.%s"%(instace.id, extension)


class Job (models.Model):        #looks like table in database
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)     #looks like column in database
    #location 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacuncy = models.IntegerField(default=1)
    sallary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    #here you will upload the image with the function 
    image = models.ImageField(upload_to=image_upload)
    
    slug = models.SlugField(null=True , blank=True)
    
    #this is save method of the mofel
    def save(self, *args, **kwargs):
        #logic
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):
    Job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, )
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
