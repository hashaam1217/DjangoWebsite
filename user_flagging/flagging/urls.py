from django.urls import path, re_path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        re_path(r"^api/list/$", views.list, name="list"),
        re_path(r"^api/list/(?P<customer_id>\d+)/$", views.customer, name="customer"),
        ]
