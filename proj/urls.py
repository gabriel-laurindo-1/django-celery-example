from django.conf.urls import handler404, handler500, include, url  # noqa
from django.urls import path
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskapp.urls'))
]
