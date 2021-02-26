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
        results.append(getByIngredient(ingredient)) #Kalder getByIngredient() for hver ingrediens, og indsætter hver liste med coktail id'er i listen results
    #pprint.pprint(results)
    #for result in results:
        #print(len(result))
    countDict = findDuplicates(results)
    #pprint.pprint(countDict)5
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

search(['Beer', 'Jack Daniels', 'Amaretto', 'Coffee', 'Root Beer', 'Coca-Cola', 'Lemonade', '7-Up', 'Creme de Cassis', 'Lemon', 'Vodka'])

#Målet er at brugeren skal kunne skrive alle de ingredienser de har ind, og så få alle de cocktails de kan lave med disse ingredienser.
