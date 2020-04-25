def main():
    words_in_statement = {}
    statement = input("Statement: ")
    words = statement.split()
    for word in words:
        count = words_in_statement.get(word, 0)
        words_in_statement[word] = count + 1

    words = list(words_in_statement.keys())
    words.sort()

    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, words_in_statement[word]))

main()