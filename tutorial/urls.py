from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups',views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api_auth',include('rest_framework.urls', namespace='rest_framework'))
]
