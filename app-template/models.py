from django.db import models

# Create your models here.

class Sample(models.Model):

    id = models.IntegerField(primary_key=True)
    sample_string = models.CharField(max_length=32)

    def __repr__(self):
        return f'Sample(id={self.id}, sample_string="{self.sample_string}")'
