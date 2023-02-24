from django.db import models
from django.utils import timezone


class Article(models.Model):
    CHOICES = (
        ('new', 'новая'),
        ('progress', 'процесс'),
        ('done', 'сделано'),
    )

    title = models.CharField(verbose_name='название', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='описание', max_length=3000, null=False, blank=False)
    detailed_view = models.TextField(verbose_name='детальное_описание', max_length=3500, null=False, blank=True)
    status = models.CharField(max_length=10, choices=CHOICES, default='new')
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    datetime = models.DateField(auto_now=True, verbose_name='дата изменения')
    deleted_at = models.DateField(verbose_name='дата удаления', null= True,default=None)


    def __str__(self):
        return f'{self.title} - {self.description} - {self.status} - {self.detailed_view}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()