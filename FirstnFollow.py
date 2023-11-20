grammar = {
    'S': ['AB', 'BC'],
    'A': ['a', ''],
    'B': ['b', ''],
    'C': ['c', '']
}

first = {}
follow = {}

def is_terminal(symbol):
    return symbol.islower() or symbol == ''

def compute_first(symbol):
    if symbol in first:
        return first[symbol]

    first_set = set()
    productions = grammar[symbol]

    for production in productions:
        if not production:
            first_set.add('')
        elif is_terminal(production[0]):
            first_set.add(production[0])
        else:
            first_set.update(compute_first(production[0]))

    first[symbol] = first_set
    return first_set

def compute_follow(symbol):
    if symbol in follow:
        return follow[symbol]

    follow_set = set()

    if symbol == 'S':
        follow_set.add('$')

    for non_terminal in grammar:
        productions = grammar[non_terminal]
        for production in productions:
            if symbol in production:
                idx = production.index(symbol)

                while idx < len(production) - 1:
                    next_symbol = production[idx + 1]
                    if is_terminal(next_symbol):
                        follow_set.add(next_symbol)
                        break
                    else:
                        first_of_next = compute_first(next_symbol)
                        follow_set.update(first_of_next - {''})

                        if '' not in first_of_next:
                            break
                    idx += 1

                if idx == len(production) - 1 or '' in compute_first(production[idx + 1]):
                    follow_set.update(compute_follow(non_terminal))

    follow[symbol] = follow_set
    return follow_set

for non_terminal in grammar:
    compute_first(non_terminal)

for non_terminal in grammar:
    compute_follow(non_terminal)

print("First sets:")
for symbol, first_set in first.items():
    print(f'First({symbol}) = {first_set}')

print("\nFollow sets:")
for symbol, follow_set in follow.items():
    print(f'Follow({symbol}) = {follow_set}')
