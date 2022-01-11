from django.db import models

# Create your models here.
class Human(models.Model):
    human_name = models.CharField(max_length=45)
    human_email = models.EmailField(max_length=300)
    human_age = models.IntegerField(default=0)

    class Meta:
        db_table = 'humans'

    def __str__(self):
        return f"{self.name, self.email, self.age}"

class Dog(models.Model):
    dog_name = models.CharField(max_length=20)
    dog_age = models.IntegerField(default=0)
    human = models.ForeignKey('Human', on_delete = models.CASCADE)

    class Meta:
        db_table = 'dogs'

    def __str__(self):
        return f"{self.name, self.age}"