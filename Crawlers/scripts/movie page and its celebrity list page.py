import requests
import time
import random
import json
import os

headers = [
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Cookie': '_vwo_uuid_v2=DE0CDB79035AD66D2C52445DE8BFED293|b80324093e44ca931a928eff13f73885; __gads=ID=6af3af30243b952d-229cf6cf5cc30021:T=1599578098:RT=1599588221:S=ALNI_MZatLJL3hMzO3X4RPN0hAKSOAdRaQ; ap_v=0,6.0; __utma=30149280.97342058.1599578097.1599578097.1599588221.2; __utmb=30149280.0.10.1599588221; __utmc=30149280; __utmz=30149280.1599578097.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="108288"; __utma=223695111.1227440182.1599578097.1599578097.1599588221.2; __utmb=223695111.1.10.1599588221; __utmc=223695111; __utmt=1; __utmz=223695111.1599578097.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=2f0a21a7df39da30.1599578097.2.1599588221.1599578118.; _pk_ses.100001.4cf6=*; __yadk_uid=UKXWV4TXsebibsIaNCBRlmYvDV3dCK5B; bid=3BVzOSU9Y3E; viewed="3432592"',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Cookie': 'll="108288"; bid=wBwSXfkxFcQ; _pk_ses.100001.4cf6=*; __utma=30149280.844702231.1599586974.1599586974.1599586974.1; __utmb=30149280.0.10.1599586974; __utmc=30149280; __utmz=30149280.1599586974.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.37483198.1599586974.1599586974.1599586974.1; __utmb=223695111.0.10.1599586974; __utmc=223695111; __utmz=223695111.1599586974.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; __gads=ID=7cc5355255a28faa-220653865fc300e6:T=1599586974:S=ALNI_Mbzsn2f1bPBBtHnd0cuXFiy8600Jw; _vwo_uuid_v2=D8227807ECBF11008702D04B8DB69BEEE|65e264cf4356305f0186020baf3e26fc; _pk_id.100001.4cf6=477fbfb2bc36fa67.1599586973.1.1599588417.1599586973.',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Cookie': 'll="108288"; bid=wBwSXfkxFcQ; _pk_ses.100001.4cf6=*; __utma=30149280.844702231.1599586974.1599586974.1599586974.1; __utmb=30149280.0.10.1599586974; __utmc=30149280; __utmz=30149280.1599586974.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.37483198.1599586974.1599586974.1599586974.1; __utmb=223695111.0.10.1599586974; __utmc=223695111; __utmz=223695111.1599586974.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0; __gads=ID=7cc5355255a28faa-220653865fc300e6:T=1599586974:S=ALNI_Mbzsn2f1bPBBtHnd0cuXFiy8600Jw; _vwo_uuid_v2=D8227807ECBF11008702D04B8DB69BEEE|65e264cf4356305f0186020baf3e26fc; ct=y; _pk_id.100001.4cf6=477fbfb2bc36fa67.1599586973.1.1599588582.1599586973.  s',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        #'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Cookie': '_vwo_uuid_v2=D2B3B56D929A477E0EBA942E194954FEB|8c8f987385824abae526b2c6e1bdd37c; __utma=223695111.420167700.1599588794.1599588794.1599588794.1; __utmb=223695111.0.10.1599588794; __utmc=223695111; __utmz=223695111.1599588794.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=30149280.1130189384.1599588794.1599588794.1599588794.1; __utmb=30149280.0.10.1599588794; __utmc=30149280; __utmz=30149280.1599588794.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _pk_id.100001.4cf6=4524e383566e51d2.1599588794.1.1599588799.1599588794.; _pk_ses.100001.4cf6=*; __gads=ID=e8996a00dcea239f-22a73e6c5cc3009c:T=1599588795:RT=1599588795:S=ALNI_MY8GCyQYqSdeaW5b3mgYFWAFHNmPw; ap_v=0,6.0; bid=LQe5hGNj-Dw; ll="108288"',
    },
    {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'movie.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-us',
        'Connection': 'keep-alive',
        'Cookie': '__utma=30149280.1012709735.1599588933.1599588933.1599588933.1; __utmb=30149280.0.10.1599588933; __utmc=30149280; __utmz=30149280.1599588933.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.557315598.1599588933.1599588933.1599588933.1; __utmb=223695111.0.10.1599588933; __utmc=223695111; __utmz=223695111.1599588933.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=DF104CFAE9C452EC27D68771407A54AE8|41466dd62d00b29f80a1ea0dd7979c55; __gads=ID=6d5fd68592fb5ba6-22cfb99c5fc3007b:T=1599588934:RT=1599588934:S=ALNI_MZo6BPTILTGwvct21zZVLWne2gajg; ap_v=0,6.0; bid=xj7d5q30L3c; ll="108288"; _pk_id.100001.4cf6=c301e5100189e8dc.1599588933.1.1599588933.1599588933.; _pk_ses.100001.4cf6=*',
    }
]

with open('./log.txt', 'a+') as log:
    with open('./movie_index.json', 'r') as f:
        dict = json.load(f)
        i = 0
        for key in dict:
            report = str(i) + ' ' + key
            print(report)
            log.write(report+ '\n')
            i += 1
            if os.path.exists('./subjects/' + dict[key]['title'] + '.html'):
                continue
            random_header_index = random.randint(0, 4)
            random_sleep_time = random.randint(4, 9)
            random_sleep_time2 = random.randint(4, 9)
            r = requests.get(dict[key]['url'], headers=headers[random_header_index], allow_redirects=False, verify=True)
            report = '-- states report: ' + str(r.status_code) + '  url: ' + dict[key]['url'] + '  using header: ' + str(random_header_index) + '  sleep: ' + str(random_sleep_time)
            print(report)
            log.write(report + '\n')
            if r.status_code != 200:
                print('Error!')
                log.write('Error!' + '\n')
                #break
            with open('./subjects/' + dict[key]['title'] + '.html', 'w') as f:
                f.write(r.text)
            time.sleep(random_sleep_time)
            # get celebrities
            r = requests.get(dict[key]['url'] + 'celebrities', headers=headers[random_header_index], allow_redirects=False, verify=True)
            report = '---- states report: ' + str(r.status_code) + '  url: ' + dict[key]['url'] + 'celebrities  using header: ' + str(random_header_index) + '  sleep: ' + str(random_sleep_time2)
            print(report)
            log.write(report + '\n')
            if r.status_code != 200:
                print('Error!')
                log.write('Error!' + '\n')
                #break
            with open('./subjects/' + dict[key]['title'] + '-celebrities.html', 'w') as f:
                f.write(r.text)
            time.sleep(random_sleep_time2)

