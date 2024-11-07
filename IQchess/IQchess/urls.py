from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chess_app.views import GameViewSet, MoveViewSet, UserProfileViewSet, ChessbotViewSet, AnalysisViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'moves', MoveViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'chessbots', ChessbotViewSet)
router.register(r'analyses', AnalysisViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
