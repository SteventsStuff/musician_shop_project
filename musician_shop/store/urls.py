from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("<int:department_id>/", by_department, name="by_department"),
    path("update_database", test_cur, name="db_update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
