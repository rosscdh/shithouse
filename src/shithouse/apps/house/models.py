from django.db import models
from comment.models import Comment
from django.urls import reverse_lazy
from django.contrib.contenttypes.fields import GenericRelation
from shithouse.apps.default.models import Image
from address.models import AddressField

class Address(models.Model):
    address = AddressField()
    agents = models.ManyToManyField("agency.Agent")
    comments = GenericRelation(Comment)
    data = models.JSONField(default=dict)

    images = models.ManyToManyField("default.Image")

    def get_absolute_url(self):
        return reverse_lazy("house-detail", kwargs={"pk": self.pk})
    
    @property
    def description(self):
        return self.data.get("description", "no description yet...")

    @property
    def feature_image(self):
        image = self.images.filter(is_feature=True).first() or self.images.filter().first()
        return getattr(image, "image", self.data.get("image", "images/128x128-house.png"))

    @property
    def mid(self):
        image = self.images.filter(is_feature=True).first() or self.images.filter().first()
        return getattr(image, "mid", self.data.get("image", "images/128x128-house.png"))

    @property
    def thumbnail(self):
        image = self.images.filter(is_feature=True).first() or self.images.filter().first()
        return getattr(image, "thumbnail", self.data.get("image", "images/128x128-house.png"))

    @property
    def non_feature_images(self):
        return self.images.filter(is_feature=False)


    def __str__(self):
        return str(self.address)