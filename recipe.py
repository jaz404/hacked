import requests

api_id = "edamam-recipe-search.p.rapidapi.com"
api_key = "6a615ab607msh046da44e29dd6bfp19131bjsn0ae968750ea3"

ingredients = input("Enter a list of ingredients separated by commas: ").split(",")
ingredients_string = "+".join(ingredients)

#response = requests.get("https://edamam-recipe-search.p.rapidapi.com/search?q=" + ingredients_string + "&app_id=" + api_id + "&app_key=" + api_key)


url = "https://edamam-recipe-search.p.rapidapi.com/search"

querystring = {"q":ingredients_string}

headers = {
	"X-RapidAPI-Key": "6a615ab607msh046da44e29dd6bfp19131bjsn0ae968750ea3",
	"X-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

recipes = response.json()['hits']

print("\nHere are the available recipes:")
for recipe in recipes:
  print(recipe["recipe"]["label"])

