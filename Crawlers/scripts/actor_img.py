import requests
import time
import random
import json
import os

def alert():
    for j in range(0, 1):
        for i in range(0, 1):
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (0.25, 400))
        time.sleep(0)

headers = [
    {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
]

with open('./error.log', 'w') as error_log:
    with open('./actor_info.json', 'r') as info_file:
        info = json.load(info_file)
        i = 0
        for actor in info:
            i += 1
            small_url = info[actor]['image_url']
            image_id = small_url.split('/')[-1]
            server = 3;
            if i % 2 == 0:
                server = 9
            if image_id == 'avatar':
                image_url = 'https://img3.doubanio.com/f/movie/8dd0c794499fe925ae2ae89ee30cd225750457b4/pics/movie/celebrity-default-medium.png'
            else:
                image_url = 'https://img' + str(server) + '.doubanio.com/view/celebrity/l/public/' + image_id
            #print(image_url)
            report = str(i) + ' ' + actor
            print(report)
            #random_header_index = random.randint(0, 1)
            if os.path.exists('./celebrity_imgs/' + actor + '.webp'):
                continue
            random_sleep_time = random.uniform(0.3, 0.9)
            random_header_index = 0
            while True:
                try:
                    r = requests.get(image_url, headers=headers[random_header_index], allow_redirects=False, verify=True, timeout=3)
                    break
                except Exception as e:
                    alert()
                    if image_url == 'https://img3.doubanio.com/f/movie/8dd0c794499fe925ae2ae89ee30cd225750457b4/pics/movie/celebrity-default-medium.png':
                        image_url == 'https://img9.doubanio.com/f/movie/8dd0c794499fe925ae2ae89ee30cd225750457b4/pics/movie/celebrity-default-medium.png'
                    elif image_url == 'https://img9.doubanio.com/f/movie/8dd0c794499fe925ae2ae89ee30cd225750457b4/pics/movie/celebrity-default-medium.png':
                        image_url == 'https://img3.doubanio.com/f/movie/8dd0c794499fe925ae2ae89ee30cd225750457b4/pics/movie/celebrity-default-medium.png'
                    else:
                        server = 9 if server == 3 else 3
                        image_url = 'https://img' + str(server) + '.doubanio.com/view/celebrity/l/public/' + image_id

                    time.sleep(1.5)
            report = '-- states report: ' + str(r.status_code) + '  url: ' + image_url + '  using header: ' + str(random_header_index) + '  sleep: ' + str(random_sleep_time)
            print(report)
            with open('./celebrity_imgs/' + actor + '.webp', 'wb') as img:
                img.write(r.content)
            time.sleep(random_sleep_time)