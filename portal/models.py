from django.db import models
from django.utils import timezone

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=50, default='', primary_key=True)
    registrationDate = models.DateTimeField(default=timezone.now)
    url = models.CharField(max_length=250, default='', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this application
        """
        return reverse('application-detail', args=[str(self.name)])

    class Meta:
        db_table = 'applications'
