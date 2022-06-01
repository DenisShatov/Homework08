import requests
import datetime
from pprint import pprint


def search_sof(tag, day):
    date = datetime.datetime.today() - datetime.timedelta(days=day)
    params_sof = {'fromdate': date.strftime("%Y-%m-%d"),
                  'tagged': tag, 'site': 'stackoverflow'}
    url = f'https://api.stackexchange.com/2.3/questions'
    question = []

    response_sof = requests.get(url, params=params_sof)
    if response_sof.status_code == 200:
        for qu in response_sof.json()['items']:
            question.append(qu['link'])
        pprint(f'Ссылки на вопросы за последние {day} дня, которые содержат тэг "Python"{question}')
    else:
        print('Некорректный запрос')


if __name__ == '__main__':
    search_sof('Python', 2)