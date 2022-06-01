import requests


def super_hero(url, names):
    hero_intelligence = {}
    for name in names:
        resp = requests.get(f'{url}{name}')
        for intelligence in resp.json()['results']:
            if intelligence['name'] == name:
                hero_intelligence[name] = int(intelligence['powerstats']['intelligence'])

    print(max(hero_intelligence, key=hero_intelligence.get))


if __name__ == '__main__':
    super_hero('https://superheroapi.com/api/2619421814940190/search/', ['Hulk', 'Captain America', 'Thanos'])

