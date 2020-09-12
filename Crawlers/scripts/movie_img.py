import requests
import time
import random
import json
import os

def alert():
    for j in range(0, 2):
        for i in range(0, 1):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.25, 400))
        time.sleep(1)

headers = [
    {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
]

with open('./error.log', 'w') as error_log:
    with open('./complete_info.json', 'r') as info_file:
        info = json.load(info_file)
        i = 0
        for movie in info:
            i += 1
            small_url = info[movie]['cover_url']
            image_id = small_url.split('/')[-1]
            image_url = 'https://img3.doubanio.com/view/photo/l/public/' + image_id
            #print(image_url)
            report = str(i) + ' ' + movie
            print(report)
            #random_header_index = random.randint(0, 1)
            if os.path.exists('./movie_imgs/' + movie + '.webp'):
                continue
            random_sleep_time = random.random()
            random_header_index = 0
            while True:
                try:
                    r = requests.get(image_url, headers=headers[random_header_index], allow_redirects=False, verify=True)
                    break
                except:
                    alert()
                    time.sleep(2)
            report = '-- states report: ' + str(r.status_code) + '  url: ' + image_url + '  using header: ' + str(random_header_index) + '  sleep: ' + str(random_sleep_time)
            print(report)
            with open('./movie_imgs/' + movie + '.webp', 'wb') as img:
                img.write(r.content)
            time.sleep(random_sleep_time)