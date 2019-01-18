import requests
import json


def pull_data_from_api():
    URL = 'http://localhost:8000/FizzBuzz'
    page = requests.get(URL)
    result = json.loads(page.text)
    Fizz = 0
    Buzz = 0
    FizzBuzz = 0
    normal = 0
    for i in result.values():
        if i == 'Fizz':
            Fizz+=1
        if i == 'Buzz':
            Buzz+=1
        if i == 'FizzBuzz':
            FizzBuzz+=1
        if i != 'Fizz' and i != 'Buzz' and i != 'FizzBuzz':
            normal+=1
    print(result)
    print(Fizz, 'number(s) where Fizz'+'\n',Buzz,'number(s) where Buzz\n',FizzBuzz,'numbers where FizzBuzz',
                            'and'+'\n',normal,'numbers weren\'t Fizz, Buzz or FizzBuzz')

pull_data_from_api()