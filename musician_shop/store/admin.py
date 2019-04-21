from django.contrib import admin

from .models import *


class StockAdmin(admin.ModelAdmin):
    list_display = ('pk', 'prod_title', 'prod_img', 'prod_type', 'prod_manufacturer_id', 'prod_description',
                    'prod_origin_price', 'sell_price', 'prod_department', 'prod_currency_info', 'prod_rate')
    list_display_links = ('prod_title', 'prod_description')
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
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Store, StockAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Analog, AnalogAdmin)
admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Comments, CommentsAdmin)
