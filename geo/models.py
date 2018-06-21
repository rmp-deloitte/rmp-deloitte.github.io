from django.db import models

class AOR(models.Model):
    """
    Model representing an operational region
    """
    AOR_CHOICES = (
        (1, 'East'),
        (2, 'West'),
    )

    name = models.CharField(max_length=4, default='', choices=AOR_CHOICES, primary_key=True)
    aorId = models.IntegerField(default=0, unique=True)
    centroidX = models.FloatField(null=True, blank=True)
    centroidY = models.FloatField(null=True, blank=True)
    bboxX1Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y2 = models.FloatField(null=True, blank=True)
    bboxX1Y2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the model object
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this area of operation
        """
        return reverse('aor-detail', args=[str(self.name)])

    def get_bound_box(self):
        """
        Returns the bound box for this region
        """
        return (self.bboxX1Y1, self.bboxX2Y1, self.bboxX2Y2, self.bboxX1Y2)

    def get_centroid(self):
        """
        Returns the centroid for this region
        """
        return (self.centroidX, self.centroidY)

    class Meta:
        db_table = 'AreaOfOperations'

class Region(models.Model):
    """
    Model representing an Area of Operation
    """

    REGION_CHOICES = (
        (1, 'Atlantic'),
        (2, 'Capital'),
        (3, 'Central'),
        (4, 'HQ'),
        (5, 'Midwest'),
        (6, 'Mountain'),
        (7, 'Northeast'),
        (8, 'Pacific'),
        (9, 'Southeast'),
        (10, 'Southwest'),
    )

    name = models.CharField(max_length=10, default=1, choices=REGION_CHOICES, primary_key=True)
    regionId = models.IntegerField(default=0, unique=True)
    aor = models.ForeignKey('AOR',on_delete=models.SET_NULL,null=True)
    centroidX = models.FloatField(null=True, blank=True)
    centroidY = models.FloatField(null=True, blank=True)
    bboxX1Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y2 = models.FloatField(null=True, blank=True)
    bboxX1Y2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the model object
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this region
        """
        return reverse('region-detail', args=[str(self.name)])

    def get_bound_box(self):
        """
        Returns the bound box for this region
        """
        return (self.bboxX1Y1, self.bboxX2Y1, self.bboxX2Y2, self.bboxX1Y2)

    def get_centroid(self):
        """
        Returns the centroid for this region
        """
        return (self.centroidX, self.centroidY)

    class Meta:
        db_table = 'regions'

class State(models.Model):
    """
    Model representing a State
    """

    SERVICE_STATUS_CHOICES = (
        (0, 'Operational'),
        (1, 'No Office'),
        (2, 'No Office/No Service'),
    )

    name = models.CharField(max_length=20, default='', primary_key=True)
    stateAbbv = models.CharField(max_length=3, blank=True, null=True)
    stateId = models.IntegerField(default=0, blank=True, null=True, unique=True)
    serviceStatus = models.CharField(max_length=45, default="Operational", choices=SERVICE_STATUS_CHOICES)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    aor = models.ForeignKey('AOR', on_delete=models.SET_NULL, null=True)
    centroidX = models.FloatField(null=True, blank=True)
    centroidY = models.FloatField(null=True, blank=True)
    bboxX1Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y2 = models.FloatField(null=True, blank=True)
    bboxX1Y2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the model object
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this region
        """
        return reverse('state-detail', args=[str(self.name)])

    def get_bound_box(self):
        """
        Returns the bound box for this region
        """
        return (self.bboxX1Y1, self.bboxX2Y1, self.bboxX2Y2, self.bboxX1Y2)

    def get_centroid(self):
        """
        Returns the centroid for this region
        """
        return (self.centroidX, self.centroidY)

    class Meta:
        db_table = 'states'

class District(models.Model):
    """
    Model representing a District
    """

    districtId = models.IntegerField(default=0, unique=True)
    districtCode = models.CharField(max_length=3, default='',primary_key=True)
    name = models.CharField(max_length=45, default='')
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    aor = models.ForeignKey('AOR', on_delete=models.SET_NULL, null=True)
    centroidX = models.FloatField(null=True, blank=True)
    centroidY = models.FloatField(null=True, blank=True)
    bboxX1Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y2 = models.FloatField(null=True, blank=True)
    bboxX1Y2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the model object
        """
        return "District: " + self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this district
        """
        return reverse('district-detail', args=[str(self.name)])


    def get_bound_box(self):
        """
        Returns the bound box for this region
        """
        return (self.bboxX1Y1, self.bboxX2Y1, self.bboxX2Y2, self.bboxX1Y2)

    def get_centroid(self):
        """
        Returns the centroid for this region
        """
        return (self.centroidX, self.centroidY)

    class Meta:
        db_table = 'districts'

class County(models.Model):
    """
    Model representing a County
    """
    countyId = models.CharField(max_length=5, default='', primary_key=True)
    name = models.CharField(max_length=45, default='')
    type = models.CharField(max_length=45, blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True)
    aor = models.ForeignKey('AOR', on_delete=models.SET_NULL, null=True, blank=True)
    centroidX = models.FloatField(null=True, blank=True)
    centroidY = models.FloatField(null=True, blank=True)
    bboxX1Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y1 = models.FloatField(null=True, blank=True)
    bboxX2Y2 = models.FloatField(null=True, blank=True)
    bboxX1Y2 = models.FloatField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the model object
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this county
        """
        return reverse('county-detail', args=[str(self.name)])

    def get_bound_box(self):
        """
        Returns the bound box for this region
        """
        return (self.bboxX1Y1, self.bboxX2Y1, self.bboxX2Y2, self.bboxX1Y2)

    def get_centroid(self):
        """
        Returns the centroid for this region
        """
        return (self.centroidX, self.centroidY)

    class Meta:
        db_table = 'counties'

class City(models.Model):
    """
    Model representing a City
    """

    cityId = models.CharField(max_length=20, primary_key=True, default='')
    name = models.CharField(max_length=45, default='')
    zipcode = models.CharField(max_length=10, default='', blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    county = models.ForeignKey('County', on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    aor = models.ForeignKey('AOR', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        String for representing the model object
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this city
        """
        return reverse('city-detail', args=[str(self.name)])

    def get_coordinates(self):
        """
        Returns the coordinates for this city
        """
        return (self.latitude, self.longitude)

    class Meta:
        db_table = 'cities'
