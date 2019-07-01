from django.conf.urls import url
from . import views


app_name = "medical"

urlpatterns = [
    url(r'^$', views.disease_list, name="list"),
    url(r'^create/$', views.disease_create, name="create"),
    url(r'^(?P<DrName>[\w-]+)/$',views.disease_detail, name="detail"),
]
