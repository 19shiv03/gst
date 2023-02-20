from django.db import models
import uuid
import dateutil.parser
from datetime import datetime
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.CharField(max_length=10)
    # updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
          ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def clean(self):
        self.slug = str(uuid.uuid4()) 
        
    def date(self):
         self.created_on=''
         self.created_on=str(self.created_on.year)+'-'+str(self.created_on.month)+'-'+str(self.created_on.day)
            
        
    
    
