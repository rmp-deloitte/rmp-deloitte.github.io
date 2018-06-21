from django.db import models
from django.utils import timezone

class Inmate(models.Model):
    """
    Model representing an Inmate.
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    RACE_CHOICES = (
        ('W', 'White'),
        ('B', 'Black'),
        ('I', 'Native American/American Indian'),
        ('H', 'Hispanic'),
        ('A', 'Asian'),
        ('O', 'Other'),
        ('N', '---'),
    )

    inmateNumber = models.CharField(max_length=10, primary_key=True)
    lastName = models.CharField(max_length=50, default='')
    firstName = models.CharField(max_length=50, default='')
    middleName = models.CharField(max_length=50, default='', blank=True, null=True)
    suffix = models.CharField(max_length=50, default='', blank=True, null=True)
    gender = models.CharField(max_length=1, default='', choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    race = models.CharField(max_length=1, default='N', choices=RACE_CHOICES)
    facilityCode = models.CharField(max_length=5, default='')
    facilityName = models.CharField(max_length=90, default='')
    facilityType = models.CharField(max_length=3, default='')
    releaseCode = models.CharField(max_length=5, default='', blank=True, null=True)
    projectedReleaseDate = models.CharField(max_length=11, default='', blank=True, null=True)
    actualReleaseDate = models.CharField(max_length=11, default='')
    caseTags = models.CharField(max_length=250, default='', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.inmateNumber

    def getInmate(self):
        return {
            'inmateNumber' : self.inmateNumber,
            'lastName' : self.lastName,
            'firstName' : self.firstName,
            'middleName' : self.middleName,
            'suffix' : self.suffix,
            'gender' : self.gender,
            'age' : self.age,
            'race' : self.race,
            'facilityCode' : self.facilityCode,
            'facilityName' : self.facilityName,
            'facilityType' : self.facilityType,
            'releaseCode' : self.releaseCode,
            'projectedReleaseDate' : self.projectedReleaseDate,
            'actualReleaseDate' : self.actualReleaseDate,
            'caseTags' : self.caseTags,
            'lastUpdated' : self.lastUpdated,
        }

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this inmate
        """
        return reverse('inmate-detail', args=[str(self.name)])

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.name:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Inmate, self).save(*args, **kwargs)

    class Meta:
        db_table = 'bop_inmates'
