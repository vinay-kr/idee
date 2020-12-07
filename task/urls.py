from django.conf.urls import url
#from .views import CreateUserAPIView, UserRetrieveUpdateAPIView, authenticate_user
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^task', TaskViewSet, basename='task')
router.register(r'^category', CategoryViewSet, basename='category')

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^login/$', authenticate_user),
]

urlpatterns += router.urls