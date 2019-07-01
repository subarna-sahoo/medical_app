from django.contrib import admin
from django.conf.urls import url, include

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

#ADMIN
    url(r'^admin/', admin.site.urls),

#DJANGO-HOME
    url(r'^$', views.homepage),
    url(r'^next/$', views.nextpage),


#MEDICAL-APP
    url(r'^diseases/', include('medical.urls')),


#PATIENT-APP
    url(r'^patients/', include('patients.urls')),

]


urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)