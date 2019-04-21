from django.http import HttpResponse

from .parsers.privatbak_currency_parser import main
from .models import Currency, Store
import datetime


def index(request):
    return HttpResponse("Hello")


def test_cur(request):
    curr_list = main()
    if len(curr_list) == 3:
        updated_cur = Currency.objects.all()[0]
        updated_cur.cur_RUB = curr_list[0][1]
        updated_cur.cur_USD = curr_list[1][1]
        updated_cur.cur_EUR = curr_list[2][1]
        updated_cur.published_date = datetime.datetime.now()
        updated_cur.save()

        for store_item in Store.objects.all():
            store_item.prod_currency_info = updated_cur
            store_item.save()

    return HttpResponse(str(curr_list))
