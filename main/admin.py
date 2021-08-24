from django.contrib import admin
from .models import Area, CrimeIncident, Comments
# Register your models here.

admin.site.register(Area)
admin.site.register(CrimeIncident)
admin.site.register(Comments)