import operator


def get_letter_rack():
    letter_rack = input("What's your letter rack? ")
    return letter_rack.lower()


def calculate_score(word):
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}
    score = 0
    for letter in word:
        score += scores[letter]
    return score


def check_word_from_rack(rack, word):
    rack_list = list(rack)
    letters_scored = 0
    for letter in word:
        for i in range(0, len(rack_list)):
            if rack_list[i] == letter:
                rack_list[i] = '0'
                letters_scored += 1
    if letters_scored == len(word):
        return True
    return False


def main():
    letter_rack = get_letter_rack()
    file = open('sowpods.txt', 'r')
    word_list = []
    while True:
        w = file.readline()
        w = w.rstrip()
        w = w.lower()
        if not w:
            break
        result = check_word_from_rack(letter_rack, w)
        if result == True:
            word_list.append(w)
    word_list_scored = {}
    for word in word_list:
        word_list_scored[word] = calculate_score(word)
    word_list_scored_output = sorted(word_list_scored.items(), key=operator.itemgetter(1))
    word_list_scored_output.reverse()
    for word, score in word_list_scored_output:
        print(word, score)


if __name__ == '__main__':
    main()
