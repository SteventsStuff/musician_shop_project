from django.http import HttpResponse
from django.shortcuts import render

from .parsers.privatbak_currency_parser import get_privabank_currency
from .models import *
import datetime
import decimal


def index(request):
    store = Store.objects.all()
    departments = Department.objects.all()

    context = {"store": store, "departments": departments}
    return render(request, "store/item_list.html", context)


def by_department(request, department_name):
    departments = Department.objects.all()
    department_id = Department.objects.filter(department_name=department_name).values()[0]['id']
    current_department = Department.objects.get(pk=department_id)
    store = Store.objects.filter(prod_department=department_id)

    context = {"store": store, "departments": departments, "current_department": current_department}
    return render(request, "store/by_department.html", context)


def product_description(request, prod_url):
    manufacturer_id = Store.objects.filter(prod_url=prod_url).values()[0]['prod_manufacturer_id_id']
    current_product = Store.objects.get(prod_url=prod_url)
    prod_manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
    departments = Department.objects.all()
    # prod_price = count_new_price(current_product.pk-1)

    context = {"current_product": current_product, "prod_manufacturer": prod_manufacturer, "departments": departments}
    return render(request, "store/product_description.html", context)


def count_new_price(item_id):
    old_price = Store.objects.all()[item_id].prod_origin_price
    old_currency = Currency.objects.all()[1].cur_USD
    actual_currency = Currency.objects.all()[0].cur_USD
    updated_price = old_price * actual_currency / old_currency

    return f"{updated_price:.2f}"


def update_prices(request):
    curr_dict = get_privabank_currency()

    if len(curr_dict) == 3:
        updated_cur = Currency.objects.all()[0]
        updated_cur.cur_RUB = curr_dict["RUB"]
        updated_cur.cur_USD = curr_dict["USD"]
        updated_cur.cur_EUR = curr_dict["EUR"]
        updated_cur.published_date = datetime.datetime.now()
        updated_cur.save()

        for store_item in Store.objects.all():
            store_item.prod_currency_info = updated_cur
            store_item.prod_updated_price = store_item.prod_origin_price\
                                            * Currency.objects.all()[0].cur_USD \
                                            / Currency.objects.all()[1].cur_USD
            store_item.save()

    return HttpResponse(str(curr_dict))
