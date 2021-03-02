import requests, json, pprint

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
        return jsonData['drinks'] #Returnerer en liste af drinks der indeholder ingrediensen
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

def getIngredients():
    data = requests.get('https://www.thecocktaildb.com/api/json/v1/1/list.php?i=list')
    if data.status_code == 200 and len(data.text) > 0:
        jsonData = json.loads(data.text)
        return jsonData['drinks']
    else:
        return []

def search(ingredients):
    results = []
    possibleDrinks = []
    for ingredient in ingredients:
        results.append(getByIngredient(ingredient)) #Kalder getByIngredient() for hver ingrediens, og indsætter hver liste med cocktail id'er i listen results
    pprint.pprint(results)
    #for result in results:
        #print(len(result))
    countDict = findDuplicates(results)
    #pprint.pprint(countDict)
    for id in countDict:
        if countDict[id] > 1:
            if getById(id)[0]['strIngredient' + str(countDict[id] + 1)] == None:
                possibleDrinks.append(id)
    #print(possibleDrinks)
    for id in possibleDrinks:
        drinkId = getById(id)
        print(drinkId[0]['strDrink'])
        print(drinkId[0]['strDrinkThumb'])
        print(drinkId[0]['strAlcoholic'])
        print(drinkId[0]['strIngredient1'] + ': ' + drinkId[0]['strMeasure1'])
        print(drinkId[0]['strIngredient2'] + ': ' + drinkId[0]['strMeasure2'])
        x = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for number in x:
            if drinkId[0]['strIngredient' + str(number)] != None:
                print(drinkId[0]['strIngredient' + str(number)] + ': ' + drinkId[0]['strMeasure' + str(number)])
        print(drinkId[0]['strInstructions'])
        print(' ')

    """topscore = max(countDict.values())
    print(topscore)
    for id in countDict:
        if countDict[id] == topscore:
            print(getById(id))"""

search(['Tequila', 'Triple sec', 'Lime juice', 'Salt'])
print(getById('12107'))
print(getIngredients())
