from django.contrib import admin
from .models import District, County, SubCounty, Parish, PollingStation, Agent, Village

admin.site.register(Village)
admin.site.register(District)
admin.site.register(County)
admin.site.register(SubCounty)
admin.site.register(Parish)
admin.site.register(PollingStation)
admin.site.register(Agent)
