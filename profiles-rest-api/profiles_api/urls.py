from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet) #we dont need to specify base_name here because we have queryset in UserProfileViewSet

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
