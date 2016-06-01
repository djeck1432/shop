from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория ")
    alias = models.SlugField(verbose_name="alias  категории")

    class Meta:
        verbose_name = "Категория "
        verbose_name_plural = "Категории"

    def __str__(self):
        return "Категория %s" % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Названия товара")
    price = models.IntegerField(default=0, verbose_name="Цена")
    image = models.CharField(max_length=1000, verbose_name="Photo link")
    alias = models.SlugField(verbose_name="alias  категория")

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = "Товар "
        verbose_name_plural = "Товары"

    def __str__(self):
        return "Товар %s" % self.name


class Forma(models.Model):
    name = models.CharField(max_length=55)
    familiy_name = models.CharField(max_length=55)
    number = models.IntegerField(default=0)
    email = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    city = models.CharField(max_length=55)
    adress = models.SlugField()

    class Meta:
        verbose_name = "Форма оплаты"
        verbose_name_plural = "Формы оплаты"

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.number)
