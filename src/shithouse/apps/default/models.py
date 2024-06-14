from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Image(models.Model):
    is_feature = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images', null=True)
    mid = ImageSpecField(source='image',
                         processors=[ResizeToFill(145, 145)],
                         format='JPEG',
                         options={'quality': 60})
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFill(100, 100)],
                               format='JPEG',
                               options={'quality': 60})
    def __str__(self):
        return self.image.file.name