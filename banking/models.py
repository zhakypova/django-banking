from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20, default='КР')
    birth_year = models.IntegerField()
    work_place = models.CharField(max_length=30, null=True, blank=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    number = models.IntegerField()
    account_type = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Credit(models.Model):
    sum = models.IntegerField()
    date = models.DateField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class MyModel(models.Model):
    my_field_name = models.CharField(max_length=255, verbose_name='пример поля', help_text='введите строковое значение')

    class Meta:
        verbose_name = 'моя модель'
        verbose_name_plural = 'мои модели'

    def len_of_my_field_name(self):
        return len(str(self.my_field_name))

    def __str__(self):
        return self.my_field_name




