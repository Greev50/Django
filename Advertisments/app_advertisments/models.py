from django.db import models

# Create your models here.

class Advertisment(models.Model):
    class Meta: 
        db_table = 'advertisements'
    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    title = models.CharField("Название", max_length=120)
    descriptions = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=9, decimal_places=2)
    trades = models.BooleanField("Торг", help_text = "Если хотим торговаться")
    date_now = models.DateField("Создание дата", auto_now_add=True)
    date_update = models.DateField("Обновление дата", auto_now=True)
    pass