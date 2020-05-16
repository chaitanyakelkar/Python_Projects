import json
import difflib

data = json.load(open("data.json"))


def translator(word):
    if word in data:
        return data[word]
    elif bool(difflib.get_close_matches(word, data, 1, 0.7)):
        approx = input(f"Did you mean {difflib.get_close_matches(word, data, 1, 0.7)[0]} ? y for yes or n for no: ")
        if approx == "y":
            return difflib.get_close_matches(word, data, 1, 0.7)[0]
        elif approx == "n":
            return "Sorry, we don't have such word"
        else:
            return "We don't understand you"
    else:
        return "We don't understand you"


def user_output_generator(indata):
    output = ""
    if type(indata) == type(""):
        return indata
    else:
        for line in indata:
            output += line
        return output


user_input = input("Enter The Word: ")
print(user_output_generator(translator(user_input)))
