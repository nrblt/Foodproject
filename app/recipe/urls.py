from recipe import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagviewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = router.urls
