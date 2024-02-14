from django.db import models
import uuid

# Create your models here.


class AssetCatg(models.Model):

    asset_cat = models.CharField(max_length=120,unique=True)
    asset_discription = models.TextField(max_length=500,blank=False,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)


    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.asset_cat
    
class AssetManage(models.Model):

    asset_name = models.CharField(max_length=120)
    asset_code = models.CharField(max_length=16,unique=True)
    asset_catg = models.ForeignKey(AssetCatg,on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default=False)
    # image_url = models.ImageField(upload_to = 'images/', blank=True, null=True)

    class Meta:
        ordering = ('-created_on',)

    def save(self, *args, **kwargs):
        if not self.asset_code:
            self.asset_code = uuid.uuid4().hex[:16]  # Generates a 16-digit UUID
        super().save(*args, **kwargs)

    def __str__(self):
        return self.asset_name


class Image(models.Model):
    main_model = models.ForeignKey(AssetManage, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')