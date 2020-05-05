from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from movierater.movieraterApp import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

schema_view = get_swagger_view(title='API documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_documentation', schema_view)
]

