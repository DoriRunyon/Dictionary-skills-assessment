"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    words = input_string.split(" ")

    letter_counter = {}

    #count the frequency of letters, and add the key/value pairs to a dict

    for word in words:
        for letter in word:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 1

    list_of_words = []

    #make a list out of every key/value pair in the dict, and put each 'mini list' in
    #the 'list of words'

    for letter, number in letter_counter.iteritems():
        mini_list = [number, letter]
        list_of_words.append(mini_list)

    #sort the 'list of words' so that the list goes from lowest frequency, to highest

    sorted_list = sorted(list_of_words)

    #create a variable which is the "last letter" in the dict (the most frequent or
    #one of the most frequent.)

    last_letter = sorted_list[len(sorted_list)-1]
    most_frequent_letters = []

    #check the list to see if any other letters had the same frequency as the
    #"last letter", if there are any, put them in the list. "Last letter" will be
    #appended to the list last.

    for mini_list in sorted_list:
        if mini_list[0] == last_letter[0]:
            most_frequent_letters.append(mini_list[1])

    return most_frequent_letters


def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    word_length_dict = {}

    #for every word in the list, get the word length. If that "length" is already
    #in the dictionary, add that word to the existing list of words for that "length".
    #If the "length" is not in the dictionary, create a new key/value pair.

    for word in words:
        length = len(word)
        if length in word_length_dict:
            word_length_dict[length].append(word)
        else:
            word_length_dict[length] = [word]

    list_of_tuples = []

    #for every key/value pair in the dictionary, create a new list with two
    #items, length and word list. Then make that list into a tuple and append
    #the tuple to the list of tuples.


    for length, word_list in word_length_dict.iteritems():
        sorted_word_list = sorted(word_list)
        length_and_word_list = [length, sorted_word_list]
        new_tuple = tuple(length_and_word_list)
        list_of_tuples.append(new_tuple)

    return list_of_tuples


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
