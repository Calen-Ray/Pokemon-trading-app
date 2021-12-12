from rest_framework import generics, permissions, viewsets
from django.contrib.auth import get_user_model

from .serializers import *
from tracker_app.models import *
# Create your views here.


# class ListPokemon(generics.ListAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

#     filter_backends = [filters.SearchFilter]
#     search_fields = [
#         'number',
#         'name',
#         'caught_by__username',
#         'types__type',
#     ]


# class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer


class GenerationsViewSet(viewsets.ModelViewSet):
    queryset = Generations.objects.all()
    serializer_class = GenerationsSerializer


class Poke_picsViewSet(viewsets.ModelViewSet):
    queryset = Poke_pics.objects.all()
    serializer_class = Poke_picsSerializer

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class CurrentUserView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     def get_object(self):
#         return self.request.user