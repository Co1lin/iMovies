import requests
import time
import random
import json
import os
import traceback

def alert():
    for j in range(0, 2):
        for i in range(0, 5):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.25, 400))
        time.sleep(1)

headers = [
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'bid=xfyMyvl2V4M; _pk_id.100001.4cf6=b25d413d128219b3.1599669653.1.1599669653.1599669653.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.841905148.1599669653.1599669653.1599669653.1; __utmb=30149280.0.10.1599669653; __utmc=30149280; __utmz=30149280.1599669653.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.85428426.1599669653.1599669653.1599669653.1; __utmb=223695111.0.10.1599669653; __utmc=223695111; __utmz=223695111.1599669653.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=1241b297a554137b-22f6bc4567c300c6:T=1599669653:S=ALNI_MZDElIReYa3BoVkSALhSSTMkHxZUA',
        'Referer': 'https://movie.douban.com/subject/1296141/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'bid=0aOxI8aJJz0; _pk_ses.100001.4cf6=*; __utma=30149280.98696514.1599654301.1599654301.1599654301.1; __utmc=30149280; __utmz=30149280.1599654301.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.218269440.1599654301.1599654301.1599654301.1; __utmb=223695111.0.10.1599654301; __utmc=223695111; __utmz=223695111.1599654301.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_t1=1; ap_v=0,6.0; __yadk_uid=UJQGNs4lrAE32FCcK0TOGRSHk9WWNTvf; __gads=ID=3e4ca49a9e6031be:T=1599654302:S=ALNI_MZFLbS5PujkQu-KUaVsAnnirKOjjg; ll="108288"; _vwo_uuid_v2=D00BA2F7FDCC4BDD35098ED3E23812EAA|395996974df75fb54f98ad6c2103d306; _pk_id.100001.4cf6=30f3f958cc1607b2.1599654301.1.1599654846.1599654301.; __utmb=30149280.21.8.1599654846418; RT=s=1599654898136&r=https%3A%2F%2Fmovie.douban.com%2Fcelebrity%2F1341178%2F',
        'Referer': 'https://movie.douban.com/subject/35141706/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'bid=5Itxt2MVjBs; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.906348273.1599655043.1599655043.1599655043.1; __utmb=30149280.0.10.1599655043; __utmc=30149280; __utmz=30149280.1599655043.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.35323146.1599655043.1599655043.1599655043.1; __utmb=223695111.0.10.1599655043; __utmc=223695111; __utmz=223695111.1599655043.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=VWOg0PJ0mHyD6CLqWGAGPQf6leefOqzq; __gads=ID=f21912da1ce88674:T=1599655044:S=ALNI_MYZrJtMaICfzevJhnc-2_Nw7Q9L2A; ll="108288"; _vwo_uuid_v2=D09BCEB49F06536F2BF10C1FA5D70F15C|c557e812344ec99c241fdf3b9f487fb2; _pk_id.100001.4cf6=9aecd0ad9586f50f.1599655043.1.1599655050.1599655043.',
        'Referer': 'https://movie.douban.com/subject/35141706/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Cookie': '__utma=30149280.97342058.1599578097.1599647707.1599655105.6; __utmb=30149280.0.10.1599655105; __utmc=30149280; __utmz=30149280.1599624455.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; __utma=223695111.1227440182.1599578097.1599647707.1599655105.6; __utmb=223695111.3.10.1599655105; __utmc=223695111; __utmz=223695111.1599624455.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_id.100001.4cf6=2f0a21a7df39da30.1599578097.6.1599655112.1599647707.; _pk_ses.100001.4cf6=*; _vwo_uuid_v2=DE0CDB79035AD66D2C52445DE8BFED293|b80324093e44ca931a928eff13f73885; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599655105%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fredir%3Dhttps%253A%252F%252Fmovie.douban.com%252F%22%5D; ap_v=0,6.0; push_doumail_num=0; push_noty_num=0; __gads=ID=6af3af30243b952d-229cf6cf5cc30021:T=1599578098:RT=1599588221:S=ALNI_MZatLJL3hMzO3X4RPN0hAKSOAdRaQ; ll="108288"; __yadk_uid=UKXWV4TXsebibsIaNCBRlmYvDV3dCK5B; bid=3BVzOSU9Y3E; viewed="3432592"',
        'Referer': 'https://movie.douban.com/subject/35141706/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Cookie': '__utma=30149280.1066203333.1599655212.1599655212.1599655212.1; __utmb=30149280.0.10.1599655212; __utmc=30149280; __utmz=30149280.1599655212.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1426419912.1599655212.1599655212.1599655212.1; __utmb=223695111.0.10.1599655212; __utmc=223695111; __utmz=223695111.1599655212.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=7e732da133c6b39b.1599655212.1.1599655218.1599655212.; _pk_ses.100001.4cf6=*; __gads=ID=91ce0065b3623376:T=1599655217:S=ALNI_MaBau3x0oPPdo4qImcJn742NBmnRg; _vwo_uuid_v2=D32D566A306AE569D9CB2407B6B108BD2|59ad2c6e25f9c7e227615ca447536844; __yadk_uid=rY3zgXwmsNSLs0JPI3v9NDGuYunc9BkG; ap_v=0,6.0; bid=Qndsi6cRyys; ll="108288"',
        'Referer': 'https://movie.douban.com/subject/35141706/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
]


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
                    if actor in actors or os.path.exists('./celebrities/' + actor + '.html'):
                        print('---- exists; skip...')
                        continue
                    random_sleep_time = random.randint(1, 2)
                    random_header_index = random.randint(0, len(headers) - 1)
                    actor_url = actor_pages[actor]
                    headers[random_header_index]['Referer'] = info[movie]['url']
                    r = requests.get(actor_url, headers=headers[random_header_index], allow_redirects=False, verify=True)
                    report = '-- states report: ' + str(r.status_code) + '  url: ' + actor_url + '  using header: ' + str(
                        random_header_index) + '  sleep: ' + str(random_sleep_time)
                    print(report)
                    if r.status_code != 200:
                        alert()
                    with open('./celebrities/' + actor + '.html', 'w') as f:
                        f.write(r.text)

                except Exception as e:
                    print('-------- Error:')
                    err = traceback.format_exc()
                    print(err)
                    error_log.write('-------- Error when request actor\'s page:' + report + '\n')
                    error_log.write(err + '\n')
                    alert()
                    continue

                time.sleep(random_sleep_time)
