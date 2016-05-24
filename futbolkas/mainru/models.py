from django.db import models


class Categoryru(models.Model):
	name =models.CharField(max_length= 255 , verbose_name= "Category ")
	alias =models.SlugField(verbose_name= "alias  Category")

	class Meta():
		verbose_name="Category "
		verbose_name_plural= "Categories"
	def __str__(self):
		return "Category %s" % self.name


class Itemru(models.Model):
	name =models.CharField(max_length= 255 , verbose_name= "Name von Ware")
	price =models.IntegerField(default =0 , verbose_name= "Price")
	image =models.CharField(max_length= 255 , verbose_name="Image")
	alias =models.SlugField(verbose_name= "alias  category")
	categoryru= models.ForeignKey(Categoryru)




	class Meta():
		verbose_name="Name von Ware "
		verbose_name_plural= "Name von Waren"
	def __str__(self):
		return " Name von Ware %s" % self.name


# Create your models here.
