from django.core.management.base import BaseCommand
import requests
from tracker_app.models import *
import json
from tracker_app.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        # 'https://pokeapi.co/api/v2/pokemon/?offset=00&limit=2000'

        Pokemon.objects.all().delete()
        Type.objects.all().delete()
        Generations.objects.all().delete()
        Games.objects.all().delete()
        Poke_pics.objects.all().delete()



        master_list = [] 
        gen_conversion_table ={
            'generation-i' : 'generation 1', 
            'generation-ii' : 'generation 2', 
            'generation-iii' : 'generation 3', 
            'generation-iv' : 'generation 4', 
            'generation-v' : 'generation 5', 
            'generation-vi' : 'generation 6', 
            'generation-vii' : 'generation 7', 
            'generation-viii' : 'generation 8',
            'generation-viiii' : 'generation 9',
            'generation-x' : 'generation 10',
        }

        # get master list
        response = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=00&limit=100')
        data = response.json()
        poke_list = data['results']

        # go through each pokemon, request detailed info, build a master list. 
        for poke in poke_list:
            detailed_response = requests.get(poke['url'])
            detailed_data = detailed_response.json()

            new_entry = {
            'name' : detailed_data['name'],
            'num' : detailed_data['id'],
            'basic_img_url' : detailed_data['sprites']['other']['home']['front_default'],
            'types' : [type['type'] for type in detailed_data['types']],
            'url_detail' : poke['url'],
            'gen' : list(detailed_data['sprites']['versions'].keys()),
            'games' : detailed_data['sprites']['versions'],
            'caught_by' : False,
            }
            print(f'getting details for {new_entry["name"]}')
            
            master_list.append(new_entry)
            # print(master_list)

        # at this point masterlist is built, time to build objects. 

        for poke in master_list:

            poke_obj = Pokemon()
            poke_obj.name = poke['name']
            poke_obj.num = poke['num']
            poke_obj.basic_img_url = poke['basic_img_url']
            poke_obj.url_detail = poke['url_detail']
            poke_obj.save()
            print(f'created {poke_obj}')
            

            for type in poke['types']:
                # create types
                type_name = type['name']
                type_obj, _ = Type.objects.get_or_create(type=type_name, detail_url=type['url'])
                type_obj.pokemon.add(poke_obj)
                type_obj.save()
                print(f'created or found type object: {type_obj}')


            for gen in poke['gen']:
                # create gens
                gen_name = gen_conversion_table[gen]
                gen_obj, _ = Generations.objects.get_or_create(name=gen_name)
                gen_obj.pokemon.add(poke_obj)
                gen_obj.save()
                print(f'created generation object: {gen_obj.name}')
                
            

            for gen in poke['games'].keys():
                gen_obj = Generations.objects.get(name=gen_conversion_table[gen]) 
                
                for game in poke['games'][gen]:
                    game_obj, _ = Games.objects.get_or_create(name=game)
                    game_obj.pokemon.add(poke_obj)
                    game_obj.generations.add(gen_obj)
                    game_obj.save()

                    for img in poke['games'][gen][game]:
                        # slight issue where some urls are a null field will fix with a if statement. 
                        if poke['games'][gen][game][img] != None:
                            print(f'creating img url object for {poke_obj} in {game_obj}')
                            img_obj, _ = Poke_pics.objects.get_or_create(img_name=img, img_url=poke['games'][gen][game][img])
                            img_obj.pokemon.add(poke_obj)
                            img_obj.game.add(game_obj)
                            img_obj.save()
                        else:
                            print(f'{poke_obj}\'s sprite for {game_obj.name} is null')


'''
            {
                'name': 'bulbasaur', 
                'num': 1, 
                'basic_img_url': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/1.png', 
                'types': [
                    {'name': 'grass', 'url': 'https://pokeapi.co/api/v2/type/12/'}, 
                    {'name': 'poison', 'url': 'https://pokeapi.co/api/v2/type/4/'}
                        ], 
                'url_detail': 'https://pokeapi.co/api/v2/pokemon/1/', 
                'gen': ['generation-i', 'generation-ii', 'generation-iii', 'generation-iv', 'generation-v', 'generation-vi', 'generation-vii', 'generation-viii'], 
                'games': {
                    'generation-i': {
                        'red-blue': { 
                            'back_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/1.png', 
                            'back_gray': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/back/gray/1.png', 
                            'back_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/back/1.png', 
                            'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/1.png', 
                            'front_gray': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/gray/1.png', 
                            'front_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/red-blue/transparent/1.png'
                            }, 
                        'yellow': {
                            'back_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/1.png', 
                            'back_gray': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/back/gray/1.png', 
                            'back_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/back/1.png', 
                            'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/1.png', 
                            'front_gray': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/gray/1.png', 
                            'front_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-i/yellow/transparent/1.png'
                            }
                        }, 
                    'generation-ii': {
                        'crystal': {
                            'back_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/1.png', 
                            'back_shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/back/shiny/1.png', 
                            'back_shiny_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/shiny/1.png', 
                            'back_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/back/1.png', 
                            'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/1.png', 
                            'front_shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/shiny/1.png', 
                            'front_shiny_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/shiny/1.png', 
                            'front_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/crystal/transparent/1.png'
                            }, 
                        'gold': {
                            'back_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/1.png', 
                            'back_shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/back/shiny/1.png', 
                            'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/1.png', 
                            'front_shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/shiny/1.png', 
                            'front_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/gold/transparent/1.png'}, 
                            'silver': {'back_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/1.png', 
                            'back_shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/back/shiny/1.png', 
                            'front_default': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/1.png', 
                            'front_shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/shiny/1.png', 
                            'front_transparent': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-ii/silver/transparent/1.png'
                            }
                        }, 
                'caught_by': False
            }
            
            '''
