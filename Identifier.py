import re

def identify(str):
    keywords = ["if", "else", "for", "while", "int", "float", "return", "break"]  
    operators = ["+", "-", "*", "/", "=", "==", "<", ">", "!="] 
    identifier_pattern = re.compile(r'^[a-zA-Z_]\w*$')

    words = str.split()
    num_keywords = 0
    num_identifiers = 0
    num_operators = 0

    for word in words:
        if word in keywords:
            num_keywords += 1
        elif word in operators:
            num_operators += 1
        elif identifier_pattern.match(word):
            num_identifiers += 1

    return num_keywords, num_identifiers, num_operators

str = input("Enter A String")
num_keywords, num_identifiers, num_operators = identify(str)

print("Number of Keywords:", num_keywords)
print("Number of Identifiers:", num_identifiers)
print("Number of Operators:", num_operators)
