from django.db import models

class Article(models.Model):
    CHOICES = (
        ('new', 'новая'),
        ('progress', 'процесс'),
        ('done', 'сделано'),
    )

    title = models.CharField(verbose_name='название', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='описание', max_length=3000, null=False, blank=False)
    status = models.CharField(max_length=10, choices=CHOICES, default='new')
    datetime = models.DateField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.status}'
