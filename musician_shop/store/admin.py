from django.contrib import admin

from .models import *


class StockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Store)
admin.site.register(Manufacturer)
admin.site.register(Currency)
admin.site.register(Analog)
admin.site.register(Accessories)
admin.site.register(Department)
admin.site.register(Comments)
