import time
import requests
import json
import datetime


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
URL = 'https://api.vk.com/method/wall.get',
v = 5.131
domain = 'ageofmagicgame'
ACCESS_TOKEN = 'd7a3a46ad7a3a46ad7a3a46ad6d4b30244dd7a3d7a3a46ab4bff74260ab801d3e5b5d32'

posts_list = []


def data_collection():
    while True:
        try:
            s = requests.Session()
            r = s.get('https://api.vk.com/method/wall.get', headers=headers, params={
                        'access_token': ACCESS_TOKEN,
                        'v': v,
                        'domain': domain
                        })
            with open('result.json', 'w') as file:
               json.dump(r.json(), file, indent=4, ensure_ascii=False)
            data = r.json()['response']['items']
            items_id = []
            for item in data:
                timestamp = item['date']
                value = datetime.datetime.fromtimestamp(timestamp)
                date_pub = value.strftime('%Y-%m-%d')
                try:
                    if item['attachments'][0]['type']:
                        images = item['attachments'][0]['photo']['sizes'][-1]['url']
                    else:
                        images = 'pass'
                except:
                    pass
                if items_id not in posts_list:
                    posts_list.append(
                        {
                            'id': item['id'],
                            'text': item['text'],
                            'photo': images,
                            'date_pub': date_pub
                        }
                    )
                    items_id.append({'id': item['id']})
                else:
                    pass

            with open('posts_data.json', 'w') as file:
                json.dump(posts_list, file, indent=4, ensure_ascii=False)
            time.sleep(300)
            dt = datetime.datetime.now()
        except:
            print('ошибка парсинга')



def main():
    data_collection()


if __name__ == '__main__':
    main()


