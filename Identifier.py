def identify(input_string):
    keywords = ["if", "else", "for", "while", "int", "float", "return", "break"]  
    operators = ["+", "-", "*", "/", "=", "==", "<", ">", "!="] 

    words = input_string.split()
    num_keywords = 0
    num_identifiers = 0
    num_operators = 0

    for word in words:
        if word in keywords:
            num_keywords += 1
        elif word in operators:
            num_operators += 1
        else:
            num_identifiers += 1

    return num_keywords, num_identifiers, num_operators

input_str = "int x = 10; if(x == 5) { x = x + 1; }"
num_keywords, num_identifiers, num_operators = identify(input_str)

print("Number of Keywords:", num_keywords)
print("Number of Identifiers:", num_identifiers)
print("Number of Operators:", num_operators)


