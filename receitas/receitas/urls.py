from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'receitas', views.ReceitaViewSet)
router.register(r'categorias', views.ReceitaViewSet)
router.register(r'partes', views.ParteViewSet)
router.register(r'ingredientes', views.IngredienteViewSet)
router.register(r'passos', views.PassoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]