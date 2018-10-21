from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class PropertyStatus(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)

class AdditionalFeatures(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Apartment(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class PropertyType(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Preference(models.Model):
    preference = models.CharField(max_length=30)

    def __str__(self):
        return str(self.preference)


class OwnerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_mobile = models.CharField(max_length=10)
    confirmation_code = models.CharField(max_length=50)
    # propertie=models.ForeignKey(Property,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.owner_mobile)


class Property(models.Model):
    name = models.CharField(max_length=500)
    owner = models.ForeignKey(OwnerInfo, on_delete=models.CASCADE)
    location = models.CharField(max_length=1000)
    status = models.IntegerField(blank=True, null=True, default=1)
    rating = models.IntegerField(blank=True, null=True, default=5)
    created_at = models.DateField(blank=True, null=True)
    budget = models.CharField(blank=True, null=True, max_length=500)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True, null=True)
    property_status = models.ForeignKey(PropertyStatus, on_delete=models.CASCADE, blank=True, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE, blank=True, null=True)
    preference = models.ManyToManyField(Preference)
    add_feature = models.ManyToManyField(AdditionalFeatures)
    # image=models.ForeignKey(Images,on_delete=models.CASCADE,blank=True,null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(str(self.name)+'  '+str(self.location))


class Images(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

# class PropertyImages(models.Model):
# 	property = models.ForeignKey(Property, default=None)
#     image = models.ImageField(upload_to=property_images,verbose_name='Image')
# 	def __str__(self):
# 		return str(self.name)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    addhar = models.CharField(max_length=15)

    def __str__(self):
        return str(self.name)


class ClientReivew(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    owner = models.ForeignKey(OwnerInfo, on_delete=models.CASCADE)
    review = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)
