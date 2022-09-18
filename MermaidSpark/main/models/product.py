#     type: 'leggings',
#     url: '',
#     img_front: 'https://ae01.alicdn.com/kf/S01910b98e7564953af81886412c9af72M/Noctilucent-Yoga-Leggings-Quick-Dry-Yoga-Pants-Women-Leggins-Sport-Women-Fitness-Night-Glowing-Tights-Leggings.jpg_Q90.jpg_.webp',
#     img_back: 'https://ae01.alicdn.com/kf/HTB1mBS_cu3tHKVjSZSgq6x4QFXaH/Noctiluce-collant-lastique-brillant-pour-femmes-pantalon-de-Sport-r-fl-chissant-rayures-Slim-sans-couture.jpg_Q90.jpg_.webp',
#     price: 'MAD 175',
#     oldprice: '',
#     description: 'Quick Dry and Night Glowing Women Leggins for Fitness',
#     star: 4,
#     Reviews: 85,
#     long_description: "----------------------------------------",
#     added:false,

from django.db import models
from django.utils import timezone

class Product(models.Model):
    '''
    Example \n
    type: 'leggings',
    url: '',
    img_front: 'https://ae01.alicdn.com/kf/S01910b98e7564953af81886412c9af72M/Noctilucent-Yoga-Leggings-Quick-Dry-Yoga-Pants-Women-Leggins-Sport-Women-Fitness-Night-Glowing-Tights-Leggings.jpg_Q90.jpg_.webp',
    img_back: 'https://ae01.alicdn.com/kf/HTB1mBS_cu3tHKVjSZSgq6x4QFXaH/Noctiluce-collant-lastique-brillant-pour-femmes-pantalon-de-Sport-r-fl-chissant-rayures-Slim-sans-couture.jpg_Q90.jpg_.webp',
    price: 'MAD 175',
    oldprice: '',
    description: 'Quick Dry and Night Glowing Women Leggins for Fitness',
    star: 4,
    Reviews: 85,
    long_description: "----------------------------------------",
    added:false,
    '''
    created = models.DateTimeField(null=True,blank=True, default=timezone.now)
    rank = models.IntegerField(null=True,blank=True, db_index=True)
    type = models.CharField(max_length=10000,null=True,blank=True, db_index=True, 
        choices=[
            ("accessories","accessories"),
            ("bras","bras"),
            ("leggings","leggings"),
            ("shorts","shorts"),
            ("sneakers","sneakers"),
            ("tank_tops","tank_tops")
        ])
    url = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    img_front = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    img_back = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    price = models.CharField(max_length=10000,null=True,blank=True)
    oldprice = models.CharField(max_length=10000,null=True,blank=True)
    star = models.IntegerField(blank=True,null=True,default=5)
    Reviews = models.IntegerField(null=True,blank=True, default=0)
    description = models.CharField(max_length=10000,null=True,blank=True, db_index=True)
    long_description = models.CharField(max_length=10000,null=True,blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.rank:
    #         self.rank = Product.objects.latest('rank')
    #     super(Product, self).save(*args, **kwargs)

    class Meta:
            db_table = "product"


