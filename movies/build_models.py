import os
import django
import sys

# init
sys.path.append('/Users/colin/PycharmProjects/iMovies')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iMovies.settings')
django.setup()

import json
from movies.models import *

with open('./build_models_error.log', 'w') as error_log:
    with open('/Users/colin/PycharmProjects/DoubanCrawler/complete_info.json', 'r') as movies_f:
        with open('/Users/colin/PycharmProjects/DoubanCrawler/actor_info.json', 'r') as actors_f:
            movies = json.load(movies_f)
            actors = json.load(actors_f)

            movie_index = 0

            for movie_name, movie_dict in movies.items():

                movie_filter_list = Movie.objects.filter(name=movie_name)
                if movie_filter_list:
                    continue

                movie_index += 1
                print('Add movie: ', movie_index)
                # add a movie
                a_movie = Movie(
                    name        =   movie_dict.get('title', '（电影）'),
                    score       =   float(movie_dict.get('score', '0.0')),
                    vote_count  =   movie_dict.get('vote_count', 0),
                    date        =   movie_dict.get('date', '1000-01-01'),
                    type        =   movie_dict.get('type', ''),
                    region      =   movie_dict.get('region', ''),
                    director    =   movie_dict.get('director', ''),
                    scriptwriter=   movie_dict.get('director', ''),
                    introduction=   movie_dict.get('introduction', '（暂无）'),
                )
                a_movie.save()
                # add comments
                for a_comment_dict in movie_dict['comments']:
                    a_comment = Comment(
                        writer  =   a_comment_dict.get('writer', '（评论者）'),
                        date    =   a_comment_dict.get('date', '1000-01-01'),
                        content =   a_comment_dict.get('content', ''),
                    )
                    a_comment.movie = a_movie
                    a_comment.save()

                # add or update actors
                for a_actor_name in movie_dict['actors_pages']:
                    actor_filter_list = Actor.objects.filter(name=a_actor_name)
                    a_actor = None
                    if not actor_filter_list:
                        # add a new actor
                        a_actor_dict = actors[a_actor_name]
                        a_actor = Actor(
                            name        =   a_actor_dict.get('name', '（演员）'),
                            gender      =   a_actor_dict.get('gender', ''),
                            birthday    =   a_actor_dict.get('birthday', ''),
                            birthplace  =   a_actor_dict.get('birthplace', ''),
                            occupation  =   a_actor_dict.get('occupation', ''),
                            introduction=   a_actor_dict.get('introduction', '（暂无）'),
                        )
                        a_actor.save()
                    else:
                        a_actor = actor_filter_list.first()
                    MovieActor.objects.create(movie=a_movie, actor=a_actor)
                    # for a_co_actor_list in a_actor_dict['coactors']:
                    #     a_co_actor = CoActor(
                    #
                    #     )

            co_actor_index = 0
            # add "co-actors" for every actor
            for a_actor_name, a_actor_dict in actors.items():
                a_actor = Actor.objects.get(name=a_actor_name)
                for a_coactor_info_list in a_actor_dict['coactors']:

                    co_actor_index += 1
                    print('Add CoActor: ', co_actor_index)

                    a_coactor_name = a_coactor_info_list[0]
                    a_coactor_count = a_coactor_info_list[1]
                    a_coactor = CoActor(
                        coactor_id      =   Actor.objects.get(name=a_coactor_name).id,
                        coactor_name    =   a_coactor_name,
                        count           =   a_coactor_count,
                        actor           =   a_actor,
                    )
                    a_coactor.save()


    print("Adding Data Complete!")