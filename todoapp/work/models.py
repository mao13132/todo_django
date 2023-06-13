from django.db import models

# Create your models here.

class Work(models.Model):
    id_pk = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    price = models.IntegerField()
    title_full = models.CharField(max_length=500)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
