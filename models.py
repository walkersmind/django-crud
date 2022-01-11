from django.db import models

# Create your models here.

class Menu(models.Model):
	name = models.CharField(max_length=20)

	class Meta:
		db_table = 'menus'

class Category(models.Model):
	name = models.CharField(max_length=20)
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'categories'

class Drink(models.Model):
	korean_name = models.CharField(max_length=100)
	english_name = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey('Category', on_delete=models.CASCADE)

	class Meta:
		db_table = 'drinks'

class Image(models.Model):
	image_url = models.CharField(max_length=2000)
	drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

	class Meta:
		db_table = 'images'
	
class Allergy(models.Model):
	name = models.CharField(max_length=45)

	class Meta:
		db_table = 'allergies'

class AllergyDrink(models.Model):
	allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
	drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'allergyDrinks'

class Nutrition(models.Model):
	one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	caffein_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)

#	size = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	drink = models.ForeignKey('Drink', on_delete=models.CASCADE, null=True)

	class Meta:
		db_table = 'nutritions'
