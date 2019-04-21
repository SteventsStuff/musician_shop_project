from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("<int:department_id>/", by_department, name="by_department"),
    path("update_database", test_cur, name="db_update"),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]
