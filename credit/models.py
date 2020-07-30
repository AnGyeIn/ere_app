from django.db import models

# Create your models here.
class CreditData(models.Model):
    user = models.ForeignKey('lecturebook.Student', on_delete=models.CASCADE, to_field='sNum', related_name='creditData')
    data = models.TextField()
