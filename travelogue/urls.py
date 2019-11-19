from django.urls import path
from .views import current_user, UserList, LocationViewSet, ReviewViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations', LocationViewSet, base_name='location')
router.register(r'reviews', ReviewViewSet, base_name='review')
router.register(r'comments', CommentViewSet, base_name='comment')

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
]

urlpatterns += router.urls
