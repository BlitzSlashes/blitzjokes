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


def generate_jokes():
    view = 'yes'
    while view == 'yes':
        ctx = input('Enter a keyword for the jokes: ').lower()
        count = input('How many jokes do you want?: ')
        if not count:
            count = 5
        res = search(ctx, count)
        if len(res):
            print(
                colored(f'Okay there were {len(res)} jokes about {ctx}...', color='green'))
            data = "\n".join(res)
            print(colored(data, color='yellow'))
            view = input(
                'Would you like to continue browsing the jokes?(yes/no): ')
        else:
            print(
                colored(f"Uh oh there weren't any jokes containing {ctx}", color='red'))
            view = input('Would you like to try again?(yes/no): ')


def options():
    options = ["getjokes"]
    return options


def selectOption(option):
    selection = {
        'getJokes': generate_jokes()
    }
    return selection.get(option)


def main():
    print(colored(pyfiglet.figlet_format("Blitz jokes 1.0.1"), color='red'))
    option = input(colored(
        f'HELLO THERE! What would you like to do?{options()}: ', color='yellow'))
    selectOption(option)
    return colored('Thanks for using Blitz jokes!', color='green')


print(main())
