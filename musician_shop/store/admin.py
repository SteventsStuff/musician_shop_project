from django.contrib import admin

from .models import *


class StockAdmin(admin.ModelAdmin):
    list_display = ('pk', 'prod_title', 'prod_materials', 'prod_type', 'prod_manufacturer_id', 'prod_origin_price',
                    'prod_updated_price', 'prod_currency_info', 'prod_department', 'prod_rate', 'prod_counter')
    list_display_links = ('prod_title',)
    list_filter = ('prod_type', 'prod_manufacturer_id', 'prod_department',)
    search_fields = ('prod_title', 'prod_description',)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cur_USD', 'cur_EUR', 'cur_RUB', 'published_date')
    list_display_links = ('cur_USD', 'cur_EUR', 'cur_RUB', 'published_date')


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'manufac_name', 'manufac_type', 'manufac_site', 'manufac_country', 'manufac_city',
                    'manufac_address', 'manufac_email', 'manufac_phone')
    list_display_links = ('manufac_name', 'manufac_country')
    search_fields = ('manufac_name', 'manufac_country', 'manufac_city', 'manufac_email')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cust_first_name', 'cust_last_name', 'cust_address', 'cust_phone', 'cust_email',
                    'product',)
    list_display_links = ('cust_first_name', 'cust_last_name')
    search_fields = ('cust_first_name', 'cust_last_name', 'cust_address', 'cust_email')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'department_name')
    list_display_links = ('department_name',)
    search_fields = ('department_name',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content', 'comment_to', 'published')
    list_display_links = ('content', 'published')
    search_fields = ('published',)


admin.site.register(Store, StockAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Analog)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Comments, CommentsAdmin)
