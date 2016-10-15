from django.conf.urls import url
from finance.views import home
from finance.views import random_account

urlpatterns = [
    url(r'^$', home),
    url(r'^/?charges/?$', random_account)
    ]
