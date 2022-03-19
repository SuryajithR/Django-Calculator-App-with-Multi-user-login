from django.db import models

# Create your models here.
class teacher(models.Model):

    name = models.CharField(max_length=500, verbose_name='Student Name')
    rno = models.IntegerField(null=True, blank=True,)
    subject1 = models.IntegerField(null=True, blank=True,)
    subject2 = models.IntegerField(null=True, blank=True,)
    subject3 = models.IntegerField(null=True, blank=True,)
    cgpa = models.IntegerField(verbose_name='Percentage')

    def __str__(self):
        return self.name
