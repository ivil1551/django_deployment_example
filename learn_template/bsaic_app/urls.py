from django.conf.urls import url
from bsaic_app import views

app_name = "bsaic_app"

urlpatterns=[
    url(r"^relative/$", views.relative, name= "relative"),
    url(r"^other/$",views.other , name= "other"),

]
