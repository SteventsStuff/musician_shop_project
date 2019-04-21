from django.http import HttpResponse
from django.shortcuts import render

from .parsers.privatbak_currency_parser import main
from .models import *
import datetime


def index(request):
    store = Store.objects.all()
    departments = Department.objects.all()
    context = {"store": store, "departments": departments}
    return render(request, "store/item_list.html", context)


def by_department(request, department_id):
    store = Store.objects.filter(prod_department=department_id)
    departments = Department.objects.all()
    current_department = Department.objects.get(pk=department_id)
    context = {"store": store, "departments": departments, "current_department": current_department}
    return render(request, "store/by_department.html", context)


def test_cur(request):
    curr_dict = main()

    if len(curr_dict) == 3:
        updated_cur = Currency.objects.all()[0]
        updated_cur.cur_RUB = curr_dict["RUB"]
        updated_cur.cur_USD = curr_dict["USD"]
        updated_cur.cur_EUR = curr_dict["EUR"]
        updated_cur.published_date = datetime.datetime.now()
        updated_cur.save()

        for store_item in Store.objects.all():
            store_item.prod_currency_info = updated_cur
            store_item.save()

    return HttpResponse(str(curr_dict))
