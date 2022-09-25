
from django.db import models
from django.utils import timezone

class Request(models.Model):
    '''
        REQUEST_METHOD: GET
        PATH_INFO: /
        QUERY_STRING: 
        REMOTE_ADDR: 127.0.0.1
        CONTENT_TYPE: text/plain
        HTTP_HOST: localhost:8000
        HTTP_CONNECTION: keep-alive
        HTTP_CACHE_CONTROL: max-age=0
        HTTP_SEC_CH_UA: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
        HTTP_SEC_CH_UA_MOBILE: ?0
        HTTP_SEC_CH_UA_PLATFORM: "macOS"
        HTTP_UPGRADE_INSECURE_REQUESTS: 1
        HTTP_USER_AGENT: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
    '''
    created = models.DateTimeField(null=True,blank=True, default=timezone.now)    
    username = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    REQUEST_METHOD = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    PATH_INFO = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    QUERY_STRING = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    REMOTE_ADDR = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    CONTENT_TYPE = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_HOST = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_CONNECTION = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_CACHE_CONTROL = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_SEC_CH_UA = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_SEC_CH_UA_MOBILE = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_SEC_CH_UA_PLATFORM = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_UPGRADE_INSECURE_REQUESTS = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    HTTP_USER_AGENT = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    

    # def save(self, *args, **kwargs):
    #     if not self.rank:
    #         self.rank = Product.objects.latest('rank')
    #     super(Product, self).save(*args, **kwargs)

    class Meta:
            db_table = "request"


