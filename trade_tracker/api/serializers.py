from rest_framework import serializers
from tracker_app import models



class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
        )
        model = models.Type

class NestedGensSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
        )
        model = models.Generations


class NestedGamesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
        )
        model = models.Games


class NestedPokemonSerializer(serializers.ModelSerializer):
    # pics_short = 
    class Meta:
        fields = (
            'name',
            'num',
            'basic_img_url',

        )
        model = models.Pokemon





class PokemonSerializer(serializers.ModelSerializer):
    types_short = NestedTypeSerializer(source='types', many=True)
    gens_short = NestedGensSerializer(source='gens', many=True)
    games_short = NestedGamesSerializer(source='games', many=True)
    # pics_short = 
    class Meta:
        fields = (
            'name',
            'num',
            'basic_img_url',
            'url_detail',
            'types_short',
            'gens_short',
            'games_short',
            # 'len(all_pics)',

        )
        model = models.Pokemon


class TypeSerializer(serializers.ModelSerializer):
    pokemon_short = NestedPokemonSerializer(source='pokemon', many=True)
    # gens_short = NestedGensSerializer(source='gens', many=True)
    # games_short = NestedGamesSerializer(source='games', many=True)
    class Meta:
        fields = (
            'type',
            'detail_url',
            'pokemon_short',
        )
        model = models.Type

class GamesSerializer(serializers.ModelSerializer):
    # types_short = NestedTypeSerializer(source='types', many=True)
    generation_short = NestedGensSerializer(source='generations', many=True)
    pokemon_short = NestedPokemonSerializer(source='pokemon', many=True)
    class Meta:
        fields = (
            'name',
            'generation_short',
            'pokemon_short',
        )
        model = models.Games


class Poke_picsSerializer(serializers.ModelSerializer):
    # types_short = NestedTypeSerializer(source='types', many=True)
    pokemon_short = NestedPokemonSerializer(source='pokemon', many=True)
    games_short = NestedGamesSerializer(source='game', many=True)
    class Meta:
        fields = (
            'img_name',
            'img_url',
            'pokemon_short',
            'games_short',
        )
        model = models.Poke_pics

class GenerationsSerializer(serializers.ModelSerializer):
    # types_short = NestedTypeSerializer(source='types', many=True)
    pokemon_short = NestedPokemonSerializer(source='pokemon', many=True)
    class Meta:
        fields = (
            'name',
            'pokemon_short'
        )
        model = models.Generations
