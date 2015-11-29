from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^receitas/$', views.ReceitaList.as_view()),
    url(r'^receitas/(?P<pk>[0-9]+)/$', views.ReceitaDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)