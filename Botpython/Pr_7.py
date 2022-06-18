def main(x):
    if x[4] == 2009:
        if x[3] == 'TERRA':
            if x[0] == 'JSON5':
                return {1963: 0, 1962: 1}[x[2]]
            elif x[0] == 'NL':
                return 2
        elif x[3] == 'QML':
            if x[1] == 'IDL':
                return {1963: 3, 1962: 4}[x[2]]
            elif x[1] == 'ALLOY':
                return {1963: 5, 1962: 6}[x[2]]
            elif x[1] == 'LEX':
                return {1963: 7, 1962: 8}[x[2]]
    elif x[4] == 1999:
        return {1963: 9, 1962: 10}[x[2]]
    return {1990: 11}[x[4]]

print(main(['NL', 'IDL', 1963, 'QML', 1999]))