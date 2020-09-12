import json

'''
Wanting key:
    title
    score / vote_count
    types
    regions
    
    release_date
    cover_url
    url
    
    actors

'''

new_dict = {
    # 'name': {
    #     'title': '',
    #     'score': '',
    #     'vote_count': 0,
    #     'types': '',    # use space between different types
    #     'regions': '',    # use space between different types
    #     'release_date': '',
    #     'cover_url': '',
    #     'url': '',
    #     'actors': [
    #
    #     ],
    # }
}

with open("./index.json") as f:
    dict = json.load(f)['movies']
    i = 0
    for movie in dict:
        for i in range(0, len(movie['title'])):
            if movie['title'][i] == '/':
                if i < len(movie['title']) - 1 and movie['title'][i + 1] == ' ':
                    movie['title'] = movie['title'][:i] + '(' + movie['title'][i + 2:]
                else:
                    movie['title'] = movie['title'][:i] + '(' + movie['title'][i + 1:]
                movie['title'] += ')'
        if movie['title'] not in new_dict:
            print(i, '  :   ', movie['title'])
            i += 1
            # save it!
            new_dict[ movie['title'] ] = {
                'title': movie['title'],
                'score': movie['score'],
                'vote_count': movie['vote_count'],
                'release_date': movie['release_date'],
                'types': '',  # use "/" between different types
                'regions': '',  # use "/" between different types
                'cover_url': movie['cover_url'],
                'url': movie['url'],
                'actors': movie['actors']
            }
            for type in movie['types']:
                new_dict[movie['title']]['types'] += (type + ' / ')
            new_dict[movie['title']]['types'] = new_dict[movie['title']]['types'][:-3]
            for region in movie['regions']:
                new_dict[movie['title']]['regions'] += (region + ' / ')
            new_dict[movie['title']]['regions'] = new_dict[movie['title']]['regions'][:-3]

    with open('./movie_index.json', 'w') as new_f:
        json.dump(new_dict, new_f, ensure_ascii=False)
    #     new_f.close()

    # f.close()
