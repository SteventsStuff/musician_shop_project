from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("<str:department_name>/", by_department, name="by_department"),
    path("<str:prod_url>/описание/", product_description, name="product_description"),
    path("<str:prod_url>/описание/", CommentCreateView.as_view, name="product_description"),
    path("<str:prod_url>/описание/liked", add_like, name="add_like"),
    path("<str:prod_url>/описание/disliked", add_dislike, name="add_dislike"),
    path("order/", OrderCreateView.as_view(), name="order"),
    path("update_prices", update_prices, name="db_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
