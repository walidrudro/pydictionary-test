import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input ("Did you mean %s instead Enter Y if yes, or N if no?" % get_close_matches(w, data.keys()) [0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys()) [0]]
        elif yn == "n":
            return "The word doesn't exist. Please type again."
        else:
            return "Invalid Entry"
    else:
        return "The word doesn't exist. Please type again."

word = input("Enter word: ")

output= translate(word)

if type(output) == list:
    for item in output:
        print (item)
else:
    print(output)
