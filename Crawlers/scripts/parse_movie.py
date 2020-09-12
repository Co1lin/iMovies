import os
import re
import json
import traceback
from lxml import etree

'''
from HTML:
导演
编剧
剧情简介
短评
[{
    'writer': ,
    'date': ,
    'content': ,
},]

'''

def list_to_string_sep(list):
    res = ' / '.join(
        [
            item.strip()
            for item in list
        ]
    )
    return res

def list_to_string_para(list):
    res = '\n'.join(
        [
            item.strip()
            for item in list
        ]
    )
    return res

DIR = '../DoubanCrawler/'
SUBJ_DIR = DIR + 'subjects/'

new_data = {
    # 'name': {
    #     'title': '',
    #     'score': '',
    #     'vote_count': 0,
    #     'director': ,
    #     'scriptwriter': ,
    #     'introduction': ,
    #     'types': '',    # use space between different types
    #     'regions': '',    # use space between different types
    #     'release_date': '',
    #     'cover_url': '',
    #     'url': '',
    #     'comments': [
    #     ],
    #     'actors': [
    #
    #     ],
    #     'actors_pages': {
    #       'name': ,
    #       'url': ,
    #     }
    # }
}

with open('./error_parse_movie.log', 'w') as error_log:

    with open(DIR + 'new_new_index.json', 'r') as findex:
        old_data = json.load(findex)
        counter = 1
        for movie in old_data:
            # if counter != 15:
            #     counter += 1
            #     continue
            report = str(counter) + ' ' + movie
            print(report)
            # get the html file
            with open(SUBJ_DIR + movie + '.html', 'r') as webpage:
                try:
                    file_str = webpage.read()
                    file_str = bytes(bytearray(file_str, encoding='utf-8'))
                    html = etree.HTML(file_str)
                    #html = etree.parse(SUBJ_DIR + key + '.html', etree.HTMLParser(encoding='utf-8'))
                    director = list_to_string_sep(html.xpath('//a[@rel="v:directedBy"]//text()'))
                    scriptwriter = list_to_string_sep(html.xpath('//*[@id="info"]/span[2]/span[2]/a//text()'))
                    introduction = html.xpath('//span[@class="all hidden"]//text()')
                    if not introduction:
                        introduction = html.xpath('//span[@property="v:summary"]//text()')
                    introduction = list_to_string_para(introduction)
                    comments = []
                    try:
                        for i in range(1, 6):
                            comment = { }
                            comment['writer'] = html.xpath('//*[@id="hot-comments"]/div[' + str(i) + ']/div/h3/span[2]/a/text()')[0].strip()
                            comment['date'] = html.xpath('//*[@id="hot-comments"]/div[' + str(i) + ']/div/h3/span[2]/span[3]/text()')[0].strip()
                            comment['content'] = html.xpath('//*[@id="hot-comments"]/div[' + str(i) + ']/div/p/span/text()')[0].strip()
                            comments.append(comment)
                    except:
                        error_log('Comments are not enough!' + 'in : ' + report + '\n')
                    # print(comments)

                except Exception as e:
                    print('-------- Error when processing the movie info webpage:')
                    err = traceback.format_exc()
                    print(err)
                    error_log.write('-------- Error when processing the movie info webpage:' + report + '\n')
                    error_log.write(err + '\n')
                    continue

            # get urls of actors' pages
            actors_pages = {}
            with open(SUBJ_DIR + movie + '-celebrities.html', 'r') as webpage:
                try:
                    file_str = webpage.read()
                    file_str = bytes(bytearray(file_str, encoding='utf-8'))
                    html = etree.HTML(file_str)
                    actor_link_list = html.xpath('//*[@id="celebrities"]/div[h2/text()="演员 Cast"]//*[@class="celebrity"]/a/attribute::href')
                    actor_name_list = html.xpath('//*[@id="celebrities"]/div[h2/text()="演员 Cast"]//*[@class="celebrity"]/a/attribute::title')
                    # if len(actor_name_list) > 10:
                    #     actor_link_list = actor_link_list[:10]
                    #     actor_name_list = actor_name_list[:10]
                    #
                    # for name in actor_name_list:
                    #     actor_pages[name] =
                    for i in range(0, min(10, len(actor_name_list))):
                        actors_pages[actor_name_list[i]] = actor_link_list[i]


                except Exception as e:
                    print('-------- Error when processing the actor info webpage:')
                    err = traceback.format_exc()
                    print(err)
                    error_log.write('-------- Error when processing the actor info webpage:' + report + '\n')
                    error_log.write(err + '\n')
                    continue

            try:
                # update the new data
                # copy the original data
                new_data[movie] = { }   # create the dict first!
                for key in old_data[movie]:
                    new_data[movie][key] = old_data[movie][key]
                # insert new data
                new_data[movie]['director'] = director
                new_data[movie]['scriptwriter'] = scriptwriter
                new_data[movie]['introduction'] = introduction
                new_data[movie]['comments'] = comments
                new_data[movie]['actors_pages'] = actors_pages
            except Exception as e:
                print('-------- Error when adding new data:')
                err = traceback.format_exc()
                print(err)
                error_log.write('-------- Error when adding new data:' + report + '\n')
                error_log.write(err + '\n')
                continue

            counter += 1

    with open('./complete_info.json', 'w') as output:
        json.dump(new_data, output, ensure_ascii=False)