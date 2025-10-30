from django.urls import path
from rest_framework.routers import DefaultRouter

from blog.views import LoginView, LogoutView
from blog.viewsets import CategoryViewSet, PostViewSet, CommentViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"profiles", ProfileViewSet)


urlpatterns = router.urls

urlpatterns += [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
