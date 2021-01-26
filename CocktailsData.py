import requests, json

ingredientOptions = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list')
print(ingredientOptions)

ingredient = 'Gin'

data = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + ingredient)
jsonData = json.loads(data.text)

print('Status Code', data.status_code)
print(jsonData)
