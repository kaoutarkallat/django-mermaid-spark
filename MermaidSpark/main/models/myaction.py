
from django.db import models
from django.utils import timezone

class MyAction(models.Model):
    '''
    '''
    created = models.DateTimeField(null=True,blank=True, default=timezone.now)    
    username = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    action_type = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    text = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    
    

    # def save(self, *args, **kwargs):
    #     if not self.rank:
    #         self.rank = Product.objects.latest('rank')
    #     super(Product, self).save(*args, **kwargs)

    class Meta:
            db_table = "myaction"


