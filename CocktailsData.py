import requests, json

def getById(idDrink):
    data = requests.get('https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=' + idDrink)
    if data.status_code == 200 and len(data.text) > 0:
        jsonData = json.loads(data.text)
        return jsonData['drinks']
    else:
        return []

def getByIngredient(ingredient):
    data = requests.get('https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=' + ingredient)
    if data.status_code == 200 and len(data.text) > 0:
        jsonData = json.loads(data.text)
        return jsonData['drinks']
    else:
        return []

def findDuplicates(listOfLists):
    countDict = {}
    for list in listOfLists:
        for cocktail in list:
            if cocktail['idDrink'] in countDict.keys():
                countDict[cocktail['idDrink']] += 1
            else:
                countDict[cocktail['idDrink']] = 1
    return countDict

def search(ingredients):
    results = []
    for ingredient in ingredients:
        results.append(getByIngredient(ingredient))
    findDuplicates(results)

search(['Gin', 'Vodka'])
#print(getById('11007'))
#print(getByIngredient('Vermouth'))
#print(getByIngredient('Gin'))
#print('Status Code', data.status_code)
#print(jsonData)
#{'strDrink': 'Addison', 'strDrinkThumb': 'https://www.thecocktaildb.com/images/media/drink/yzva7x1504820300.jpg', 'idDrink': '17228'}
