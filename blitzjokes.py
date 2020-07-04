import requests
from termcolor import colored
import pyfiglet


def search(ctx, limit):
    url = 'https://icanhazdadjoke.com/search'
    res = requests.get(
        url, headers={'Accept': 'application/json'}, params={"term": f'{ctx}', 'limit': limit})
    data = res.json()
    jokes = [i['joke'] for i in data['results']]
    return jokes


def main():
    print(colored(pyfiglet.figlet_format("Blitz jokes 1.0.0"), color='red'))
    ctx = input('Enter a keyword for the jokes: ').lower()
    count = input('How many jokes do you want?: ')
    if not count:
        count = 5
    res = search(ctx, count)
    if len(res):
        print(
            colored(f'Okay there were {len(res)} jokes about {ctx}...', color='green'))
        data = "\n".join(res)
        return colored(data, color='yellow')
    else:
        return colored(f"Uh oh there weren't any jokes containing {ctx}", color='red')


print(main())
