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

def search(ingredients):
    results = []
    possibleDrinks = []
    for ingredient in ingredients:
        results.append(getByIngredient(ingredient)) #Kalder getByIngredient() for hver ingrediens, og indsætter hver liste i listen results
    pprint.pprint(results)
    for result in results:
        print(len(result))
    countDict = findDuplicates(results)
    pprint.pprint(countDict)
    topscore = max(countDict.values())
    print(topscore)
    for id in countDict:
        if countDict[id] == topscore:
            print(getById(id))



    """
    for list in results:
        for cocktail in list:
            x = 1
            possibleDrink = True
            while x < 15:
                aCocktail = getById(cocktail['idDrink'])
                if aCocktail[0]['strIngredient' + str(x)] == None:
                    if possibleDrink == True:
                        possibleDrinks.append(cocktail['idDrink'])
                        x = 20
                    else:
                        x = 20
                elif aCocktail[0]['strIngredient' + str(x)] not in ingredients:
                    possibleDrink = False
                    x += 1
                else:
                    x += 1
    noResults = "No cocktails using these ingredients could be found."
    if len(possibleDrinks) > 0:
        return possibleDrinks
    else:
        return noResults
    """

print(search(['Vodka', 'Gin']))
#print(getById('11007'))
#print(getByIngredient('Vermouth'))
#print(getByIngredient('Gin'))
#print('Status Code', data.status_code)
#print(jsonData)
#{'strDrink': 'Addison', 'strDrinkThumb': 'https://www.thecocktaildb.com/images/media/drink/yzva7x1504820300.jpg', 'idDrink': '17228'}

#Målet er at brugeren skal kunne skrive alle de ingredienser de har ind, og så få alle de cocktails de kan lave med disse ingredienser. 
