def get_num_words(book_text):
	num_of_words = 0
	for word in book_text.split():
		num_of_words += 1
	return num_of_words

def get_character_count(book_text):
    character_count = {} # example: {'p': 6121, 'r': 20818, 'o': 25225, ...
    chars_found = set()
    char_count = 0
    # get unique characters
    for char in book_text:
        chars_found.add(char.lower())

    # set all counts to zero and initialize dictionary
    for c in chars_found:
        character_count[c] = 0

    # start setting counts of chars within the book_text string
    for char in book_text:
        temp = character_count[char.lower()]
        character_count[char.lower()] = temp + 1

    #print(character_count)

    return character_count


def print_report(book_text):
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')

    print('----------- Word Count ----------')
    print(f'{get_num_words(book_text)} words found in the document')
    print('--------- Character Count -------')

    char_counts = get_character_count(book_text)
    dictionary_list = []
    # Refactor dictionary into { char: 'e', count: 3 }
    # Each dictionary should have two key-value pairs (see above)
    # Need to return a list of dictionaries. One for each char-count.

    for kv in char_counts:
        new_dict = {}
        new_dict['char'] = kv
        new_dict['num'] = char_counts[kv]
        dictionary_list.append(new_dict)
    
    # Sort by num descending
    dictionary_list.sort(reverse=True,key=sort_on)
    
    # Pretty print
    for d in dictionary_list:
        if (d['char'].isalpha()):
            print(f"{d['char']}: {d['num']}")

    print('============= END ===============')

def sort_on(counts):
    return counts['num']