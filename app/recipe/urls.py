from django.urls import(
    path, include
)
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagviewSet)
app_name = 'recipe'

urlpatterns = router.urls
 