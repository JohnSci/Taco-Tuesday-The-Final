import requests

data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
print(data)
season_data = data['seasoning']
print(f'here is some seasons: {season_data}')