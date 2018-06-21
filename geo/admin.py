from django.contrib import admin
from .models import AOR
from .models import Region
from .models import State
from .models import District
from .models import County
from .models import City

# Register your models here.
admin.site.register(AOR)
admin.site.register(Region)
admin.site.register(State)
admin.site.register(District)
admin.site.register(County)
admin.site.register(City)
