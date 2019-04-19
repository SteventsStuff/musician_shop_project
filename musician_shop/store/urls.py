from django.urls import path
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

from .views import index


urlpatterns = [
    path("", index, name="index"),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]
