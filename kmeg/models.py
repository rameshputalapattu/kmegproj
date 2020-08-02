from django.db import models
from PIL import Image
import os

# Create your models here.


class KmegImage(models.Model):

    jpeg_picture = models.ImageField()
    thumb_nail = models.ImageField()
    quantized_picture = models.ImageField()
    quantized_thumb_nail = models.ImageField()
    title = models.CharField(max_length=30)
    colors = models.IntegerField(default=25)

    def save(self):
        super().save()

        img = Image.open(self.jpeg_picture.path)

        output_size = (200, 200)
        dir_name = os.path.dirname(self.jpeg_picture.path)
        base_file_name = os.path.basename(self.jpeg_picture.path)
        file_name, ext = os.path.splitext(base_file_name)
        img.thumbnail(output_size)
        img.save(os.path.join(dir_name, file_name+"_tb"+ext))
        self.thumb_nail = os.path.join(dir_name, file_name+"_tb"+ext)

    def __str__(self):
        return str(self.id) + " " +str(self.title)




