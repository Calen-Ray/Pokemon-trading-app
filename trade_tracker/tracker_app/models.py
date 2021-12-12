from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    num = models.CharField(max_length=50)
    basic_img_url = models.URLField(max_length=200)
    url_detail = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Type(models.Model):
    type = models.CharField(max_length=20)
    detail_url = models.URLField(max_length=200)
    pokemon = models.ManyToManyField(Pokemon, related_name='types')

    def __str__(self):
        return self.type


class Generations(models.Model):
    name = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon, related_name=("gens"))

    def __str__(self):
        return f'{self.name} | {len(self.pokemon.all())} pokemon'


class Games(models.Model):
    name = models.CharField(max_length=30)
    generations = models.ManyToManyField(Generations, related_name='games')
    pokemon = models.ManyToManyField(Pokemon, related_name='games')

    def __str__(self):
        return f'{self.name} | {len(self.pokemon.all())} pokemon'


class Poke_pics(models.Model):
    img_name = models.CharField(max_length=50)
    img_url = models.URLField(max_length=200)
    pokemon = models.ManyToManyField(Pokemon, related_name='all_pics')
    game = models.ManyToManyField(Games, related_name='all_pics')

    
    def __str__(self):
        return f'{self.pokemon.all()} sprite from {self.game.all()}'





