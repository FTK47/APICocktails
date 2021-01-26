import requests

users = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007')

print(users.text)
print('Status Code', users.status_code)
