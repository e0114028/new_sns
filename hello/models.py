from distutils.command.upload import upload
from multiprocessing.reduction import register
from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    register_date = models.DateTimeField(auto_now_add=True)
    icon_image = models.ImageField(upload_to='images/',null=True,blank=True )
     
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + self.name + '(' + str(self.age) + ')>'