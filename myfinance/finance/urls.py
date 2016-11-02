from django.conf.urls import url
from finance.views import home
from finance.views import random_example
from finance.views import add_charge

urlpatterns = [
    url(r'^$', home),
    url(r'^charges/$', random_example),
    url(r'^apply/$', add_charge, name='add_charge')
    ]
