from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    main_image = models.ImageField(upload_to='notices/images/')
    content = RichTextField(blank=True)
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    notice_category = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Noticia no. {self.id}'

class Categoria(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'


class HomeSlide(models.Model):
    image = models.ImageField(upload_to='homeCarousel/images/')
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=72)
    noticia = models.ForeignKey('Notice', on_delete=models.CASCADE)

    def __str__(self):
        return f'Slide no. {self.id}'