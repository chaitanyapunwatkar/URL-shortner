from django.urls import path
from . import views
app_name = "url"
urlpatterns = [
    path("", views.index, name="home"),
    path("urlShort", views.urlShort, name="urlshort"),
    path("urlCreate", views.urlCreated, name="urlcreate"),
    path("<str:shorts>", views.urlRedirect, name="redirect")
]


