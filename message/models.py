from django.db import models

# # Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

class Person (models.Model):
    class PersonType (models.TextChoices):
        PARTICIPANT = 'participant' , 'شرکت کننده'
        GUEST = 'guest', 'مهمان'
    first_name = models.CharField(("نام "), max_length=100)
    last_name = models.CharField(("نام خانوادگی"), max_length=100)
    person_type = models.CharField(max_length=20,choices=PersonType.choices,
    default=person_type.PARTICIPANT,
    verbose_name="نوع فرد")
    phone_number = models.CharField(("تلفن همراه"), max_length=15,unique=True)
