from django.db import models

# Create your models here.
class Note(models.Model):
    url = models.CharField('URL', max_length=255, default='')
    note = models.TextField('Note', default='')

    def __str__(self):
        return f'{self.pk}. {self.url}'