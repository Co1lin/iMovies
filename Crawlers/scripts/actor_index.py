import requests
import time
import random
import json
import os
import  traceback

def alert():
    for j in range(0, 2):
        for i in range(0, 5):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.25, 400))
        time.sleep(1)

actors = {
    # 'name': {
    #    'name': ,
    #    'gender': ,
    #    'birthday': ,
    #    'birthplace': ,
    #    'occupation': ,
    #    'url': ,
    #    'image_url': ,
    # },
}

with open('./error.log', 'w') as error_log:
    with open('./complete_info.json', 'r') as info_file:
        info = json.load(info_file)
        i = 0
        j = 0
        for movie in info:
            i += 1
            actor_pages = info[movie]['actors_pages']
            for actor in actor_pages:
                try:
                    j += 1
                    report = str(i) + ' , ' + str(j) + '  ' + actor
                    print(report)
                    if actor not in actors:
                        actors[actor] = { }
                        actors[actor]['name'] = actor
                        actors[actor]['url'] = actor_pages[actor]
                        actors[actor]['movies'] = [ ]
                        actors[actor]['coactors'] = {}

                    actors[actor]['movies'].append(movie)

                    for coactor in actor_pages:
                        if coactor != actor:
                            if coactor not in actors[actor]['coactors']:
                                actors[actor]['coactors'][coactor] = 1
                            else:
                                actors[actor]['coactors'][coactor] += 1
                    # if actor in actors:
                    #     actors[actor]['movies'].append(movie)
                    #     print('---- exists; skip...')
                    #     continue
                    # actors[actor] = { }
                    # actor_url = actor_pages[actor]
                    # actors[actor]['name'] = actor
                    # actors[actor]['url'] = actors[actor]
                    # actors[actor]['movies'] = [ movie, ]
                    # actors[actor]['coactors'] = [ ]
                    # for coactor in actor_pages:
                    #     if coactor != actor and coactor not in actors[actor]['coactors']:
                    #         actors[actor]['coactors'].append(coactor)

                    #print(report)

                except Exception as e:
                    print('-------- Error:')
                    err = traceback.format_exc()
                    print(err)
                    error_log.write('-------- Error when processing actor\'s data:' + report + '\n')
                    error_log.write(err + '\n')
                    alert()
                    continue

    with open('actor_index.json', 'w') as f:
        json.dump(actors, f, ensure_ascii=False)

