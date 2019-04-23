from django.contrib import admin

from .models import *


class StockAdmin(admin.ModelAdmin):
    list_display = ('pk', 'prod_title', 'prod_year', 'prod_materials', 'prod_type', 'prod_manufacturer_id', 'prod_origin_price',
                    'prod_department', 'prod_rate')
    list_display_links = ('prod_title',)
    list_filter = ('prod_type', 'prod_manufacturer_id', 'prod_department', 'prod_rate')
    search_fields = ('prod_title', 'prod_description',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cur_USD', 'cur_EUR', 'cur_RUB', 'published_date')
    list_display_links = ('cur_USD', 'cur_EUR', 'cur_RUB', 'published_date')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'manufac_name', 'manufac_type', 'manufac_site', 'manufac_country', 'manufac_city',
                    'manufac_address', 'manufac_email', 'manufac_phone')
    list_display_links = ('manufac_name', 'manufac_country')
    search_fields = ('manufac_name', 'manufac_country', 'manufac_city', 'manufac_email')


class AnalogAdmin(admin.ModelAdmin):
    pass


class AccessoriesAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'department_name')
    list_display_links = ('department_name',)
    search_fields = ('department_name',)


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Store, StockAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Analog, AnalogAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Comments, CommentsAdmin)
