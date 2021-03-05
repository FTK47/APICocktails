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
        results.append(getByIngredient(ingredient)) #Kalder getByIngredient() for hver ingrediens, og indsætter hver liste med cocktail id'er i listen results
    IngNummer = 1
    for result in results:
        if len(result) == 0: #Checker om listen for ingrediensen er tom, hvilket ville betyde at ingrediensen ikke indgår i en eneste af databasens cocktails
            print("Ingrediens " + str(IngNummer) + " er ikke i databasen.")
        IngNummer += 1
    countDict = findDuplicates(results) #Find ud af hvor mange gange hver cocktail går igen i ingredienslisterne
    for id in countDict:
        if countDict[id] > 1: #Hver cocktail skal matche mindst to ingredienser for at det kan være muligt at den kan laves uden andre
            if getById(id)[0]['strIngredient' + str(countDict[id] + 1)] == None: #Hvis cocktailen har flere ingredienser end den matcher, er der ingredienser brugeren mangler
                possibleDrinks.append(id)
    showCocktails(possibleDrinks)

def showCocktails(possibleDrinks):
    if len(possibleDrinks) == 0:
        print('No suitable cocktails found.')
    else:
        for id in possibleDrinks:
            drinkId = getById(id)
            print(' ')
            print(drinkId[0]['strDrink'])
            print(drinkId[0]['strAlcoholic'])
            print(drinkId[0]['strIngredient1'] + ': ' + drinkId[0]['strMeasure1'])
            print(drinkId[0]['strIngredient2'] + ': ' + drinkId[0]['strMeasure2'])
            x = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            for number in x:
                if drinkId[0]['strIngredient' + str(number)] != None:
                    print(drinkId[0]['strIngredient' + str(number)] + ': ' + drinkId[0]['strMeasure' + str(number)])
            print(drinkId[0]['strInstructions'])

def run():
    print('Please write in all the ingredients you have availabe, one at a time. Press enter without writing anything when you are done.')
    ingredients = []
    done = 'No'
    while done == 'No':
        x = input('Write here: ')
        if len(x) > 0:
            ingredients.append(x)
        else:
            search(ingredients)
            done = 'Yes'

run()
