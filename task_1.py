import requests


def get_hero_with_max_intelligence(*args):
    mx, name = 0, ''
    for hero in args:
        url = "https://superheroapi.com/api/2619421814940190/search/" + hero
        resp = requests.get(url, timeout=5)
        for i in resp.json()["results"]:
            if i["name"] == hero:
                intelligence = int(i["powerstats"]["intelligence"])
                break
        if intelligence > mx:
            mx = intelligence
            name = hero
    print(name)


get_hero_with_max_intelligence("Hulk", "Captain America", "Thanos")
