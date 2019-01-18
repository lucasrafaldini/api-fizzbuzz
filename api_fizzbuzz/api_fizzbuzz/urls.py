
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

app_name = 'api'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('FizzBuzz', include('api.urls')),
    url('', RedirectView.as_view(url='FizzBuzz')),
]