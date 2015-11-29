from django.conf.urls import url
import views

urlpatterns = [
    url(r'^receitas/$', views.Receta),
    url(r'^receitas/(?P<pk>[0-9]+)/$', views.snippet_detail),
]