from json import JSONDecodeError
import requests

number = input("enter a number: ")
try:
    print(int(number)*2)
except LookupError:
    print("Lookup error? This should never happen...")
except ValueError:
    print("Not a valid number")

r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'hello-world'})
try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print("We could not decode the JSON response!")
except KeyError:
    print("We got JSON back from sentiment analysis, but it did not have a key label.")


