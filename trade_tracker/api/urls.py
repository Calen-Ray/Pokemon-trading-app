from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import *





router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')
router.register('generations', GenerationsViewSet, basename='generations')
router.register('pics', Poke_picsViewSet, basename='pics')
router.register('games', GamesViewSet, basename='games')


urlpatterns = router.urls + [
    # path('', ListPokemon.as_view()),
    # path('<int:pk>/', DetailPokemon.as_view()),
]
