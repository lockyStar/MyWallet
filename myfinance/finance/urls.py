from django.conf.urls import url
from finance.views import home,add_charge,account_status,random_example

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^charges/$', random_example),
    url(r'^charges/(?P<account_id>\d{1,16})/$', account_status, name='status'),
    url(r'^addcharge/(?P<account_id>\d{1,16})/$', add_charge, name='add_charge')
    ]
