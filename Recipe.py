import requests

data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
print(data)
fact = data['seasoning']
print(f'here is some seasons: {fact}')