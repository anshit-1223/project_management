from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'users',UsersViewSet)
router.register(r'projects',ProjectsDetailsViewSet)
router.register(r'users',ProjectMembersViewSet)
router.register(r'tasks',TasksViewSet)
router.register(r'comments',CommentsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]